from flask import Flask, session,render_template,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Length
from copy import deepcopy
from algorithm import Solution
import json

app=Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'

###################################################
##################### Form #######################
###################################################
class InputForm(FlaskForm):
    name1=StringField('Name1',validators=[Length(max=8)])
    name2=StringField('Name2',validators=[Length(max=8)])
    name3=StringField('Name3',validators=[Length(max=8)])
    name4=StringField('Name4',validators=[Length(max=8)])
    name5=StringField('Name5',validators=[Length(max=8)])
    name6=StringField('Name6',validators=[Length(max=8)])
    name7=StringField('Name7',validators=[Length(max=8)])
    name8=StringField('Name8',validators=[Length(max=8)])
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
        session['name7']=form.name7.data
        session['name8']=form.name8.data

###########Execute algorithm##############

        #eliminate duplicated characters in a single word
        name1=''.join(set([i.lower() for i in[session['name1']] if i.isalpha()]))
        name2=''.join(set([i.lower() for i in[session['name2']] if i.isalpha()]))
        name3=''.join(set([i.lower() for i in[session['name3']] if i.isalpha()]))
        name4=''.join(set([i.lower() for i in[session['name4']] if i.isalpha()]))
        name5=''.join(set([i.lower() for i in[session['name5']] if i.isalpha()]))
        name6=''.join(set([i.lower() for i in[session['name6']] if i.isalpha()]))
        name7=''.join(set([i.lower() for i in[session['name7']] if i.isalpha()]))
        name8=''.join(set([i.lower() for i in[session['name8']] if i.isalpha()]))
        #eliminate duplicated words and '' in list
        inputList=set([name1,name2,name3,name4,name5,name6,name7,name8])
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
        # session['length']=len(session['result'])

        return redirect(url_for('index'))
    return render_template('index.html',form=form,results=session.get('result',None),wordDict=wordDict)

@app.route('/result')
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)
