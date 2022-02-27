certoraRun MeetingSchedulerBug3.sol:MeetingScheduler --verify MeetingScheduler:meetings.spec \
--solc ~/solc/0.8.7/solc-macos \
--rule startBeforeEnd \
--msg "startBeforeEnd is fixed"
