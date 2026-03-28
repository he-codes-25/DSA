class Solution:
    def capitalizeTitle(self, title: str) -> str:
        t=title.split()
        ans=[]
        for i in t:
            if len(i)>2:
                ans.append(i.capitalize())
            else:
                ans.append(i.lower())
        return " ".join(ans)