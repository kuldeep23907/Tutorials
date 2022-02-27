certoraRun ERC20Fixed.sol:ERC20 --verify ERC20:ERC20.spec \
--solc ~/solc/0.8.0/solc-macos \
--optimistic_loop \
--send_only \
--msg "$1"