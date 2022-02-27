certoraRun MeetingSchedulerBug4.sol:MeetingScheduler --verify MeetingScheduler:meetings.spec \
--solc ~/solc/0.8.7/solc-macos \
--rule checkStartedToStateTransition \
--msg "checkStartedToStateTransition is fixed"