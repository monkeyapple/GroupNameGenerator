from copy import deepcopy
class Solution:
    def permute(self,word):
        permutations=[]
        self.generatePermutations([],word,permutations)
        return permutations
    def generatePermutations(self,running_choices,originalStr,permutations):
        if len(running_choices)==len(originalStr):
            permutations.append(deepcopy(running_choices))
            return
        for i in range(0,len(originalStr)):
            choice =originalStr[i]
            if choice in running_choices:
                continue
            running_choices.append(choice)
            self.generatePermutations(running_choices,originalStr,permutations)
            running_choices.pop()

    def letterCombinations(self):
        self.refList=['bona','exy','seola']
        combination=[]
        if self.refList==None:
            return None

        self.helper("",0,combination)
        return combination
    def helper(self,choices,currentIdx,combinations):
        if currentIdx==len(self.refList):
            combinations.append(choices)
            return
        for i in self.refList[currentIdx]:
            choices+=i
            self.helper(choices,currentIdx+1,combinations)
            choices=choices[:-1]

    def referenceList(self,inputList):
        pass


c=Solution()

print(c.letterCombinations())