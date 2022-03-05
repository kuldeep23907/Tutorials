
methods {
	ballAt() returns uint256 envfree
}

invariant neverReachPlayer4() 
	ballAt() != 4 && ballAt() != 3

rule neverReachPlayer4Rule(method f) {
	env e;
	uint256 ballAt_before = ballAt();
	require ballAt_before != 3 && ballAt_before != 4;
    f(e);
	uint256 ballAt_after = ballAt();
    assert ballAt_after != 4;
}