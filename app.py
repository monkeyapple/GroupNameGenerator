from flask import Flask, session,render_template,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Length
from copy import deepcopy
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
    return render_template('index.html',form=form)


@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
