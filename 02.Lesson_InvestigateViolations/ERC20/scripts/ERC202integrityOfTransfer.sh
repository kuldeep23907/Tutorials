certoraRun ERC20Bug2.sol:ERC20 --verify ERC20:ERC20.spec \
--solc ~/solc/0.8.0/solc-macos \
--optimistic_loop \
--rule integrityOfTransfer \
--msg "integrityOfTransfer to be fixed now"

