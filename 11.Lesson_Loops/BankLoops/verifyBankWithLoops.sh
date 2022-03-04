certoraRun BankWithLoops.sol:Bank --verify Bank:Loops.spec \
--solc ~/solc/0.7.6/solc-macos \
--optimistic_loop \
--loop_iter 2 \
--msg "$1"