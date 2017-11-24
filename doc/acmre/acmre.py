#coding utf-8
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from acmsumdb import ACMREdb
from zhj import myre

app = Flask(__name__)


@app.route('/') #装饰器告诉flask 哪个URL才能出发我们的函数
def show():
    webGetDb = ACMREdb()
    allInformation = webGetDb.querydbAll()
    return render_template('show.html',allInformation = allInformation)


@app.route('/re',methods=['GET','POST'])
def re():
    if request.method == 'POST':
        dict = {}
        dict['xuehao']=request.form['xuehao']
        dict['zhjmm']=request.form['zhjmm']
        dict['xywmm']=request.form['xywmm']
        myre(dict)
        return render_template('RE.html')

    return render_template('cinInfor.html')


@app.route('/add',methods=['GET', 'POST'])
def add():  #添加信息
    if request.method == 'POST':
            dict = {}  #使用字典时不要忘记声明字典
            dict['id'] = request.form['num']
            dict['name'] = request.form['name']
            dict['dlnuojname'] = request.form['dlnuojname']
            dict['hduojname'] = request.form['hduojname']
            dict['vojname'] = request.form['vojname']
            dict['codeforcename'] = request.form['codeforcename']

            if dict['id'] == '':
                return redirect("https://www.baidu.com")
            else:
                addDb = ACMREdb()
                addDb.insertdb(dict)

            return redirect(url_for('show'))
        #except:
            #return redirect("https://www.baidu.com")

    return render_template('postInformation.html')

@app.route('/<name>')
def bugbug(name):
    return name





if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)
