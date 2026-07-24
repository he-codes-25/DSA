class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count=0
        for s in range(len(startTime)):
            if startTime[s]<=queryTime and endTime[s]>=queryTime:
                count+=1
        return count