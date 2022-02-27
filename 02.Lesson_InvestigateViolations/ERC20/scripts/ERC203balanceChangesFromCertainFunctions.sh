certoraRun ERC20Bug3.sol:ERC20 --verify ERC20:ERC20.spec \
--solc ~/solc/0.8.0/solc-macos \
--optimistic_loop \
--rule balanceChangesFromCertainFunctions \
--msg "balanceChangesFromCertainFunctions to be fixed now"

