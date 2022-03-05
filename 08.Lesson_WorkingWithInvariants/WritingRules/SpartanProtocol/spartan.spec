methods {
    getToken0DepositAddress() returns (address) envfree
    getToken1DepositAddress() returns (address) envfree
    balanceOf(address) returns (uint256) envfree
    totalSupply() returns (uint256) envfree
}

rule tokensAmountIncreases(method f) {
    address token0 =  getToken0DepositAddress();
    address token1 = getToken1DepositAddress();

    require token0 != token1;

    uint256 token0Amount_before = balanceOf(token0);
    uint256 token1Amount_before = balanceOf(token1);

    env e;
    calldataarg args;
    f(e,args);

    uint256 token0Amount_after = balanceOf(token0);
    uint256 token1Amount_after = balanceOf(token1);

    assert (token0Amount_after > token0Amount_before && token1Amount_after > token1Amount_before)
            => (f.selector == add_liquidity().selector);

}

rule tokensAmountDecreases(method f) {
    address token0 =  getToken0DepositAddress();
    address token1 = getToken1DepositAddress();

    require token0 != token1;

    uint256 token0Amount_before = balanceOf(token0);
    uint256 token1Amount_before = balanceOf(token1);

    env e;
    calldataarg args;
    f(e,args);

    uint256 token0Amount_after = balanceOf(token0);
    uint256 token1Amount_after = balanceOf(token1);

    assert (token0Amount_after < token0Amount_before && token1Amount_after < token1Amount_before)
            => (f.selector == remove_liquidity(uint256).selector);

}

ghost sum_of_all_funds() returns uint256{
    // for the constructor - assuming that on the constructor the value of the ghost is 0
    init_state axiom sum_of_all_funds() == 0;
}

// fails and helps to find the bug
invariant totalFunds_GE_to_sum_of_all_funds()
    totalSupply() >= sum_of_all_funds()

