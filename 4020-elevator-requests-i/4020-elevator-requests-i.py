class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        current=0
        ans=0
        for r in requests:
            ans+=abs(current-r)
            current=r
        return ans