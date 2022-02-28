
methods {

    getPointsOfContender(address contender) returns(uint256) envfree

    hasVoted(address voter) returns(bool) envfree

    getWinner() returns(address, uint256) envfree

    getFullVoterDetails(address voter) returns(uint8 age, bool registered, bool voted, uint256 vote_attempts, bool black_listed) envfree
    
    getFullContenderDetails(address contender) returns(uint8 age, bool registered, uint256 points) envfree

    registerVoter(uint8 age) returns (bool)

    registerContender(uint8 age) returns (bool)

    vote(address first, address second, address third) returns(bool)
}

definition unRegisteredVoter(address voter) returns bool =  !getVoterRegistrationStatusOnly(voter) && getVoterAgeOnly(voter) == 0 && getVoterVoteAttemptsOnly(voter) == 0 && !getVoterVoteBlockedOnly(voter) && !getVoterVotedOnly(voter);
definition registeredYetVotedVoter(address voter) returns bool = getVoterRegistrationStatusOnly(voter) && !getVoterVotedOnly(voter) && getVoterVoteAttemptsOnly(voter) == 0 && !getVoterVoteBlockedOnly(voter);
definition legitRegisteredVotedVoter(address voter) returns bool = getVoterRegistrationStatusOnly(voter) && getVoterVotedOnly(voter) && !getVoterVoteBlockedOnly(voter) && 0 < getVoterVoteAttemptsOnly(voter) && getVoterVoteAttemptsOnly(voter) < 3;
definition getVoterBlocked(address voter) returns bool = getVoterRegistrationStatusOnly(voter) && getVoterVotedOnly(voter) && getVoterVoteBlockedOnly(voter) &&  getVoterVoteAttemptsOnly(voter) >= 3;

function contendersPoint(address contender) returns uint256 {
    uint256 points = getPointsOfContender(contender);
    return points;
}

function getVoterAgeOnly(address voter) returns uint8 {
    uint8 age; bool voterReg; bool voted; uint256 vote_attempts; bool blocked;
    age, voterReg, voted, vote_attempts, blocked = getFullVoterDetails(voter);
    return age;
}
function getVoterVoteAttemptsOnly(address voter) returns uint256 {
    uint8 age; bool voterReg; bool voted; uint256 vote_attempts; bool blocked;
    age, voterReg, voted, vote_attempts, blocked = getFullVoterDetails(voter);
    return vote_attempts;
}

function getVoterRegistrationStatusOnly(address voter) returns bool {
    uint8 age; bool voterReg; bool voted; uint256 vote_attempts; bool blocked;
    age, voterReg, voted, vote_attempts, blocked = getFullVoterDetails(voter);
    return voterReg;
}

function getVoterVoteBlockedOnly(address voter) returns bool {
    uint8 age; bool voterReg; bool voted; uint256 vote_attempts; bool blocked;
    age, voterReg, voted, vote_attempts, blocked = getFullVoterDetails(voter);
    return blocked;
}

function getVoterVotedOnly(address voter) returns bool {
    uint8 age; bool voterReg; bool voted; uint256 vote_attempts; bool blocked;
    age, voterReg, voted, vote_attempts, blocked = getFullVoterDetails(voter);
    return voted;
}

// Checks that a voter's "registered" mark is changed correctly - 
// If it's false after a function call, it was false before
// If it's true after a function call, it either started as true or changed from false to true via registerVoter()
rule registeredCannotChangeOnceSet(method f, address voter){
    env e; calldataarg args;
    uint256 age; bool voterRegBefore; bool voted; uint256 vote_attempts; bool blocked;
    age, voterRegBefore, voted, vote_attempts, blocked = getFullVoterDetails(voter);
    f(e, args);
    bool voterRegAfter;
    age, voterRegAfter, voted, vote_attempts, blocked = getFullVoterDetails(voter);

    assert (!voterRegAfter => !voterRegBefore, "voter changed state from registered to not registered after a function call");
    assert (voterRegAfter => 
        ((!voterRegBefore && f.selector == registerVoter(uint8).selector) || voterRegBefore), 
            "voter was registered from an unregistered state, by other function then registerVoter()");
}

// Checks that each voted contender receieves the correct amount of points after each vote
rule correctPointsIncreaseToContenders(address first, address second, address third){
    env e;
    uint256 firstPointsBefore = contendersPoint(first);
    uint256 secondPointsBefore = contendersPoint(second);
    uint256 thirdPointsBefore = contendersPoint(third);

    vote(e, first, second, third);
    uint256 firstPointsAfter = contendersPoint(first);
    uint256 secondPointsAfter = contendersPoint(second);
    uint256 thirdPointsAfter = contendersPoint(third);
    
    assert (firstPointsAfter - firstPointsBefore == 3, "first choice receieved other amount than 3 points");
    assert (secondPointsAfter - secondPointsBefore == 2, "second choice receieved other amount than 2 points");
    assert ( thirdPointsAfter- thirdPointsBefore == 1, "third choice receieved other amount than 1 points");

}

// Checks that a blocked voter cannot get unlisted
rule onceBlockedNotOut(method f, address voter){
    env e; calldataarg args;
    uint256 age; bool registeredBefore; bool voted; uint256 vote_attempts; bool blocked_before;
    age, registeredBefore, voted, vote_attempts, blocked_before = getFullVoterDetails(voter);
    require blocked_before => registeredBefore;
    f(e, args);
    bool registeredAfter; bool blocked_after;
    age, registeredAfter, voted, vote_attempts, blocked_after = getFullVoterDetails(voter);
    
    assert blocked_before => blocked_after, "the specified user got out of the blocked users' list";
}

// Checks that a contender's point count is non-decreasing
rule contendersPointsNondecreasing(method f, address contender){
    env e; calldataarg args;
    uint8 age; bool registeredBefore; uint256 pointsBefore;
    age, registeredBefore, pointsBefore = getFullContenderDetails(contender);
    require pointsBefore > 0 => registeredBefore; 
    f(e,args);
    bool registeredAfter; uint256 pointsAfter;
    age, registeredAfter, pointsAfter = getFullContenderDetails(contender);

    assert (pointsAfter >= pointsBefore);
}

