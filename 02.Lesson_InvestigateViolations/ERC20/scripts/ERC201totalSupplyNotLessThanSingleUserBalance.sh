certoraRun ERC20Bug1.sol:ERC20 --verify ERC20:ERC20.spec \
--solc ~/solc/0.8.0/solc-macos \
--optimistic_loop \
--rule totalSupplyNotLessThanSingleUserBalance \
--msg "totalSupplyNotLessThanSingleUserBalance to be fixed now"
