class Solution(object):
    def digitSum(self, s, k):
        while len(s)>k and s!=k:
            string=''
            for i in range(0,len(s),k):
                target=list(map(int,s[i:i+k]))
                string=string+str(sum(target))
            print(string)
            s=string
        return s
         