from flask import Flask, render_template,redirect,url_for
from flask_wtf import FlaskForm
from wtform import StringField,SubmitField
from wtforms.validators import Length
from copy import deepcopy
import json

app=Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'
###################################################
################# Algorithm #######################
###################################################
class Solution:
    def __init__(self):
        with open('cleanedDict.json') as json_file:
            self.dictRef=json.load(json_file)

#Step1: Got combinations from given words

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

###################################################
##################### Form #######################
###################################################
class InputForm(FlaskForm):
    name1=StringField('Name1',validators=[Length(min=8)])
    name2=StringField('Name2',validators=[Length(min=8)])
    name3=StringField('Name3',validators=[Length(min=8)])
    name4=StringField('Name4',validators=[Length(min=8)])
    name5=StringField('Name5',validators=[Length(min=8)])
    name6=StringField('Name6',validators=[Length(min=8)])
    name7=StringField('Name7',validators=[Length(min=8)])
    name8=StringField('Name8',validators=[Length(min=8)])
    submit=SubmitField('Generate')


###################################################
###################### View #######################
###################################################
@app.route('/',methods=['GET','POST'])
def index():
    form=InputForm()
    if form.validate_on_submit():
        session['name1']=form.name1.data
        session['name2']=form.name2.data
        session['name3']=form.name3.data
        session['name4']=form.name4.data
        session['name5']=form.name5.data
        session['name6']=form.name6.data
        session['name7']=form.name7.data
        session['name8']=form.name8.data
        return redirect(url_for('result'))
    return rentder_template('index.html',form=form)


@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
