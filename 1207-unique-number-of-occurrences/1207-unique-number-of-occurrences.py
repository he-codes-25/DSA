class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occor=[]
        for a in set(arr):
            if arr.count(a) in occor:
                return False
            occor.append(arr.count(a))
        return True