certoraRun MeetingSchedulerBug1.sol:MeetingScheduler --verify MeetingScheduler:meetings.spec \
--solc ~/solc/0.8.7/solc-macos \
--rule monotonousIncreasingNumOfParticipants \
--msg "monotonousIncreasingNumOfParticipants is fixed"