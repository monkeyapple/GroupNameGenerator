
#Step1: Got combinations from given words
    def letterCombinations(self,inputList):
        combination=[]
        if inputList==None:
            return None
        self.helper("",0,combination)
        return combination
    def helper(self,choices,currentIdx,combinations):
        if currentIdx==len(inputList):
            combinations.append(choices)
            return
        for i in inputList[currentIdx]:
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

#Step3:Search in dictionary
    def searchInDict(self,permutations,dictRef):
        result=[]
        for i in permutations:
            if i in dictRef:
                result.append(i)
        return result

c=Solution()
combinations=list(set(c.letterCombinations()))

result=[]
for i in combinations:
    permutationResult=list(c.permute(i))
    result.extend(permutationResult)
result=list(set(result))

print(c.searchInDict(result,c.dictRef))

# from copy import deepcopy
# import json
# class Solution:
#     def __init__(self):
#         with open('cleanedDict.json') as json_file:
#             self.dictRef=json.load(json_file)
#
# #Step1: Got combinations from given words
#
#     def letterCombinations(self):
#         self.refList=['bona','exy','seola']
#         combination=[]
#         if self.refList==None:
#             return None
#         self.helper("",0,combination)
#         return combination
#     def helper(self,choices,currentIdx,combinations):
#         if currentIdx==len(self.refList):
#             combinations.append(choices)
#             return
#         for i in self.refList[currentIdx]:
#             choices+=i
#             self.helper(choices,currentIdx+1,combinations)
#             choices=choices[:-1]
#
# #Step2:Got permutations of each combination
#
#     def permute(self,word):
#         permutations=set()
#         self.generatePermutations([],word,permutations)
#         return permutations
#     def generatePermutations(self,running_choices,originalStr,permutations):
#         if len(running_choices)==len(originalStr):
#             permuStr=(''.join(running_choices))
#             permutations.add(permuStr)
#             # permutations.add(deepcopy(running_choices))
#             return
#         for i in range(0,len(originalStr)):
#             choice =originalStr[i]
#             if choice in running_choices:
#                 continue
#             running_choices.append(choice)
#             self.generatePermutations(running_choices,originalStr,permutations)
#             running_choices.pop()
#
# #Step3:Search in dictionary
#     def searchInDict(self,permutations,dictRef):
#         result=[]
#         for i in permutations:
#             if i in dictRef:
#                 result.append(i)
#         return result
#
# c=Solution()
# combinations=list(set(c.letterCombinations()))
#
# result=[]
# for i in combinations:
#     permutationResult=list(c.permute(i))
#     result.extend(permutationResult)
# result=list(set(result))
#
# print(c.searchInDict(result,c.dictRef))
#
