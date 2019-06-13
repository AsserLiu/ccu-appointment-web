from flask import Flask,request,render_template
import csv
import datetime
import time
import smtplib
from email.mime.text import MIMEText
app = Flask(__name__)
app.debug = True

weekday = {'TUE':'星期二', 'THU':'星期四', 'next_TUE':'下星期二', 'next_THU':'下星期四'}

@app.route('/')
@app.route('/index.html')
def index():
	return render_template('index.html')

@app.route('/form.html',methods = ['POST','GET'])
def show_form():
    return render_template('form.html')

@app.route('/imformation.html')
def show_imformation():
    return render_template('imformation.html')

@app.route('/time.html')
def show_time():
    return render_template('time.html')

@app.route('/service.html')
def show_service():
    return render_template('service.html')

@app.route('/deal.py',methods = ['POST'])
def getData():
    name = request.form.get('name')
    ID = request.form.get('studentid')
    sex = request.form.get('sex')
    dept = request.form.get('dept')
    time = request.form.get('time')
    email = request.form.get('email')
    phone = str(request.form.get('cellphone'))

    d = datetime.datetime.now()
    if(((d.weekday() == 1 and d.time().hour >= 11) or d.weekday() == 2) and time == 'TUE'):
        return render_template('fail.html')
    elif(((d.weekday() == 3 and d.time().hour >= 11) or (d.weekday() >= 4 and d.weekday() <= 5)) and (time == 'TUE' or time == 'THU')):
        return render_template('fail.html')

    flag = False
    path = 'list/' + str(dept) + '-' + str(time) + '.csv'
    i = 0
    with open(path,'r',newline = '\n') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            i += 1
    if(i < 20):
        with open(path,'a',newline = '\n') as csvfile:
            w = csv.writer(csvfile)
            w.writerow([name,ID,sex,email,phone])
            flag = True
    if(flag == False):
        return render_template('fail.html')
    sender = 'asser520@gmail.com'
    password = 'f6789gbbn'
    message = str(name) + '同學，您在' + weekday[time] + '已預約成功，請準時到達衛保組看診。'
    msg = MIMEText(message)
    msg['Subject'] = '預約成功通知'
    msg['From'] = sender
    msg['To'] = email

    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.login(sender,password)
    server.send_message(msg)
    server.quit()
    print('Email send')
    return render_template('form.html')

if __name__ == '__main__':
	app.run()
