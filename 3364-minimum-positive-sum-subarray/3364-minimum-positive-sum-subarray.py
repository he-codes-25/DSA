class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        m=None
        for n in range(l,r+1):
            for i in range(len(nums)-n+1):
                target=sum(nums[i:i+n])
                if target>0:
                    if m==None:
                        m=target
                    else:
                        m=min(target,m)
        print(m)
        if m==None or m==0:
            return -1
        return m
            
        