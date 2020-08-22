class BinaryIndexedTree(object):
    def __init__(self,d):
        self.Data=d
        self.lenData=len(self.Data)
        self.BIT=[0] * (self.lenData+1)
        self.InitilizeBIT()
    
    def LowBit(self,x):
        return x&(-x)
    
    def InitilizeBIT(self):
        for i,d in enumerate(self.Data):
            self.BIT[i+1]=self.Data[i]
        for x in range(1,len(self.BIT)):
            y=x+self.LowBit(x)
            if y <= self.lenData:
                self.BIT[y]+=self.BIT[x]

    def Query(self,x):
        sumQuery=0
        i=x
        while i > 0 :
            sumQuery+=self.BIT[i]
            i-=self.LowBit(i)
        return sumQuery
    
    def Update(self, index, val):
        i=index
        while i <= self.lenData:
            self.BIT[i]+=val
            i+=self.LowBit(i)
            
class Solution(object):
    def Ranking(self, nums):
        numsDict={}
        numsSorted=sorted(nums)
        count=1
        for n in numsSorted:
            if n not in numsDict:
                numsDict[n]=count
                count+=1
        tmp=[numsDict[i] for i in nums]        
        return (numsDict,tmp)
    
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==0:
            return []
        rankMapper,nums_ranked=self.Ranking(nums)
        BIT=BinaryIndexedTree([0]*(max(rankMapper.values())+1))
        answer=[]
        for n in nums:
            answer.append(BIT.Query(rankMapper[n]-1))
            BIT.Update(rankMapper[n],1)
        return answer


sln=Solution()
assert [1,0]==sln.countSmaller([-1,-2])
assert []==sln.countSmaller([])
assert [0]==sln.countSmaller([1])
assert [0]==sln.countSmaller([2])
assert [0,0]==sln.countSmaller([1,2])
assert [0,0]==sln.countSmaller([1,2])
assert [1,0]==sln.countSmaller([2,1])
assert [3,1,1,0]==sln.countSmaller([5,2,2,1])
assert [2,1,1,0]==sln.countSmaller([5,2,6,1])
assert [1,0,1,0]==sln.countSmaller([-1,-2,1,-1])
assert [2,0,4,1,10,6,6,3,1,0,1,0,3,1,1,0]==sln.countSmaller([-1,-2,1,-1,5,2,2,1,-1,-2,1,-1,5,2,2,1])









