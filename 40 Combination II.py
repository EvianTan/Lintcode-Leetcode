'''
candidates.sort()
        self.res = []
        self.dfs(candidates, target, 0, [])
        return self.res
    
    def dfs(self, candidates, target, start, valuelist):
        length = len(candidates)
        if target == 0 and valuelist not in self.res:
            return self.res.append(valuelist)
        for i in range(start, length):
            if target < candidates[i]:
                return 
            self.dfs(candidates, target-candidates[i], i+1, valuelist+[candidates[i]])
            '''

            class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.res = []
        self.dfs(candidates, target, 0, [])
        return self.res
    
    def dfs(self, candidates, target, start, valuelist):
        length = len(candidates)
        if target == 0 and valuelist not in self.res:
            return self.res.append(valuelist)
        for i in range(start, length):
            if target < candidates[i]:
                return 
            self.dfs(candidates, target-candidates[i], i+1, valuelist+[candidates[i]])