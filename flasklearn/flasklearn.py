from flask import Flask
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required


app = Flask(__name__)
app.config['SECRET_KEY']='hard to guess string'   #app.config字典可以用来储存框架/扩展和程序本身的配置变量

class NameForm(Form):
    name = StringField('What is your name?',validators=[Required()]) #name的文本字段  Required表示验证函数 `
    #StringField 表示属性为text的《input》元素
    submit = SubmitField('Submit')   #submit的提交按钮
    #SubmitField表示为提交的元素

@app.route('/')
def hello_world():
    return 'Hello World!'





if __name__ == '__main__':
    app.run()
