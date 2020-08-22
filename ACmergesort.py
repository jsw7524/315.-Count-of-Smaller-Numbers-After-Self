class Inversion(object):
    def __init__(self,n,idx):
        self.num=n
        self.index=idx
        self.inversion=0
        

class Solution(object):
    def __init__(self):
        self.count=-1
        
    def msort3(self,x):
        if len(x) < 2:
            self.count+=1
            return [Inversion(x,self.count)]
            
        result = []
        mid = int(len(x) / 2)
        y = self.msort3(x[:mid])
        z = self.msort3(x[mid:])
        i = 0
        j = 0
        while i < len(y) and j < len(z):
            if y[i].num <= z[j].num:
                result.append(z[j])
                j += 1
            else:
                y[i].inversion+=len(z)-j
                result.append(y[i])
                i += 1
        result += y[i:]
        result += z[j:]
        return result

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if None == nums:
            return []
        if 0==len(nums):
            return []
        answer= self.msort3(nums)
        answer.sort(key=lambda i: i.index)
        return [ x.inversion for x in answer]

sln=Solution()
assert [2,1,1,0]==sln.countSmaller([5,2,6,1])
assert [5,3,5,1,2,1,1,0]==sln.countSmaller([5,3,8,2,3,2,6,1])
assert [2,1,2,1,0]==sln.countSmaller([5,3,8,6,1])
assert [0]==sln.countSmaller([5])
assert []==sln.countSmaller([])    