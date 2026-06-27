class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n=len(nums)
        nu=[]
        for i in range(n):
            if nums[i] not in nu:
                nu.append(nums[i])
        print(nu)
        o=len(nu)
        nu.sort()
        print(nu)
        if o==1:
            return nu[0]
        elif o==2:
            return nu[1]
        else:
            return nu[o-3]
        
