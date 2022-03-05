methods {
    balanceOf(address account) returns (uint256) envfree
    getTotalFeesEarnedPerShare() returns uint256 envfree
    getUserRewards(address) returns uint256 envfree
    getUserFeesCollectedPerShare(address) returns uint256 envfree
}

rule totalFeesEarnedPerShareMonotonousIncrease(method f) {
    uint256 totalSharesAccumulator_before = getTotalFeesEarnedPerShare();

    env e;
    calldataarg arg;
    f(e, arg);

    uint256 totalSharesAccumulator_after = getTotalFeesEarnedPerShare();

    assert totalSharesAccumulator_before <= totalSharesAccumulator_after;
}

rule userRewardseNotDecreasing(method f) {
    calldataarg arg;
    env e;
    address user;
    require user != 0;
    uint256 userRewards_before = getUserRewards(user);

    f(e, arg);

    uint256 userRewards_after = getUserRewards(user);

    assert userRewards_before <= userRewards_after;
}

// fail, helps in the finding the bug
rule LPtokenBurnBug(method f) {
    address user;
    require user != 0;
    uint256 balance_before = balanceOf(user);

    env e;
    calldataarg arg;
    f(e, arg);

    uint256 balance_after = balanceOf(user);
    uint256 userFeesCollectedPerShare = getUserFeesCollectedPerShare(user);
    uint256 totalFeesEarnedPerShare = getTotalFeesEarnedPerShare();

    assert balance_after != balance_before => userFeesCollectedPerShare == totalFeesEarnedPerShare;
}