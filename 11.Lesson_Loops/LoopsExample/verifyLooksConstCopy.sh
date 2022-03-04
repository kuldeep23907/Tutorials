certoraRun Loops.sol:Loops --verify Loops:LoopsUnrolling.spec \
--solc ~/solc/0.8.12/solc-macos \
--rule const_loop_correct \
--optimistic_loop \
--loop_iter 10
--msg "$1"