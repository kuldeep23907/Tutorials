certoraRun MeetingSchedulerBug2.sol:MeetingScheduler --verify MeetingScheduler:meetings.spec \
--solc ~/solc/0.8.7/solc-macos \
--rule checkPendingToCancelledOrStarted \
--msg "checkPendingToCancelledOrStarted is fixed"