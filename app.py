from flask import Flask, session,render_template,redirect,url_for,request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Length,Regexp
from copy import deepcopy
from algorithm import Solution
import json

app=Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'

###################################################
##################### Form #######################
###################################################
class InputForm(FlaskForm):
    name1=StringField('Name1',validators=[Length(max=8),Regexp('^[a-zA-Z]*$',message="Inputs must contain only english letters")])
    name2=StringField('Name2',validators=[Length(max=8),Regexp('^[a-zA-Z]*$',message="Inputs must contain only english letters")])
    name3=StringField('Name3',validators=[Length(max=8),Regexp('^[a-zA-Z]*$',message="Inputs must contain only english letters")])
    name4=StringField('Name4',validators=[Length(max=8),Regexp('^[a-zA-Z]*$',message="Inputs must contain only english letters")])
    name5=StringField('Name5',validators=[Length(max=8),Regexp('^[a-zA-Z]*$',message="Inputs must contain only english letters")])
    name6=StringField('Name6',validators=[Length(max=8),Regexp('^[a-zA-Z]*$',message="Inputs must contain only english letters")])

    submit=SubmitField('Generate')


###################################################
###################### View #######################
###################################################

@app.route('/',methods=['GET','POST'])
def index():
    #import dict
    with open('wordDict.json') as json_file:
        wordDict=json.load(json_file)
    form=InputForm()
    if form.validate_on_submit():

        session['name1']=form.name1.data
        session['name2']=form.name2.data
        session['name3']=form.name3.data
        session['name4']=form.name4.data
        session['name5']=form.name5.data
        session['name6']=form.name6.data
        session['inputDisplay']='+'.join(list(filter(lambda x:x!='',
        [form.name1.data,form.name2.data,form.name3.data,form.name4.data,form.name5.data,form.name6.data])))

###########Execute algorithm##############

        #eliminate duplicated characters in a single word
        name1=''.join(set([i.lower() for i in[session['name1']]]))
        name2=''.join(set([i.lower() for i in[session['name2']]]))
        name3=''.join(set([i.lower() for i in[session['name3']]]))
        name4=''.join(set([i.lower() for i in[session['name4']]]))
        name5=''.join(set([i.lower() for i in[session['name5']]]))
        name6=''.join(set([i.lower() for i in[session['name6']]]))

        #eliminate duplicated words and '' in list
        inputList=set([name1,name2,name3,name4,name5,name6])
        inputList=list(filter(lambda item:item!='',inputList))


        solution=Solution()
        combinations=solution.letterCombinations(inputList)
        results=[]
        for i in combinations:
            permutationResult=solution.permute(i)
            results.extend(list(permutationResult))
        dictList=[i for i in results if i in wordDict]
        dictResult = {wordDict[item][0]:item for item in dictList}
        # order the result by word frequncy
        sortdictResult = dict(sorted(dictResult.items(), key=lambda item: item[1]))
        session['result']=sortdictResult
        return redirect(url_for('index'))
    return render_template('index.html',form=form,results=session.get('result',None),wordDict=wordDict,inputDisplay=session.get('inputDisplay',None))

@app.route('/result')
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)
