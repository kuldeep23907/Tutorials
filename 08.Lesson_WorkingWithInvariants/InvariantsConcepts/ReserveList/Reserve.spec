methods {
     // Gets the token saved in underlyingList mapping according to input index
    getTokenAtIndex(uint256 index) returns (address) envfree

    // Gets the ID saved in reserved mapping according to input token id
    getIdOfToken(address token) returns (uint256) envfree

    // Gets the count of underlying assets in the list
    getReserveCount() returns (uint256) envfree

    // Adds a reserve to the list and updates its details
    addReserve(address token, address stableToken, address varToken, uint256 fee) envfree

    // Removes a specified reserve from the list.
    removeReserve(address token) envfree
}

rule listsAreCorelated(method f, address token, uint256 tokenId) {

    uint256 tokenIdC = getIdOfToken(token);
    address tokenC =  getTokenAtIndex(tokenId);

    assert ((tokenId != 0 && token != 0) => 
    (tokenIdC == tokenId <=> tokenC == token))
    || (tokenId == 0 && tokenC == token => tokenIdC == tokenId);
    
}

rule injectiveTokenIds(method f, address token1, address token2) {
    require token1 != token2;

    uint256 token1Id_before = getIdOfToken(token1);
    uint256 token2Id_before = getIdOfToken(token2);

    require token1Id_before != token2Id_before;

    env e;
    calldataarg args;
    f(e,args);

    uint256 token1Id_after = getIdOfToken(token1);
    uint256 token2Id_after = getIdOfToken(token2);

    assert token1Id_after == 0 && token2Id_after == 0 => f.selector == removeReserve(address).selector || token1Id_after != token2Id_after;
}

rule noTokenAtIndexGEtoReserveCounter(method f, uint256 tokenId) {

    require tokenId != 0;
    uint256 reserveCount_before = getReserveCount();
    require tokenId < reserveCount_before;

    env e;
    calldataarg args;
    f(e,args);

    uint256 reserveCount_after = getReserveCount();

    assert reserveCount_after == 0 => tokenId == 0 || reserveCount_after > tokenId;
}

rule nonViewMethodUpdateReserveCounterBy1only(method f) {

    uint256 reserveCount_before = getReserveCount();

    env e;
    calldataarg args;
    f(e,args);

    uint256 reserveCount_after = getReserveCount();

    assert reserveCount_after == reserveCount_before + 1 => f.selector == addReserve(address,address,address,uint256).selector;
    assert reserveCount_after == reserveCount_before - 1 => f.selector == removeReserve(address).selector;
}

rule independencyOfTokens(address token1, address token2) {
    require token1 != 0 && token2 !=0;
    require token1 != token2;

    uint256 token2Id_before = getIdOfToken(token2);

    removeReserve(token1);

    uint256 token2Id_after = getIdOfToken(token2);

    assert token2Id_after == token2Id_before;
}



