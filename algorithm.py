class Solution():
    #Step1: Got combinations from given words
    def letterCombinations(self,inputList):
        combination=set()
        if inputList==None:
            return None
        self.inputList=inputList
        self.helper("",0,combination)
        return combination
    def helper(self,choices,currentIdx,combinations):
        if currentIdx==len(self.inputList):
            combinations.add(choices)
            return
        for i in self.inputList[currentIdx]:
            choices+=i
            self.helper(choices,currentIdx+1,combinations)
            choices=choices[:-1]

    #Step2:Got permutations of each combination
    def permute(self,word):
        permutations=set()
        self.generatePermutations([],word,permutations)
        return permutations
    def generatePermutations(self,running_choices,originalStr,permutations):
        if len(running_choices)==len(originalStr):
            permuStr=(''.join(running_choices))
            permutations.add(permuStr)
            # permutations.add(deepcopy(running_choices))
            return
        for i in range(0,len(originalStr)):
            choice =originalStr[i]
            if choice in running_choices:
                continue
            running_choices.append(choice)
            self.generatePermutations(running_choices,originalStr,permutations)
            running_choices.pop()
