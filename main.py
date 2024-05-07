import json
from flask import Flask, jsonify, render_template,request

app = Flask(__name__)

@app.route('/verifylogin', methods=['POST'])
def verifylogin():
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
    with open('users.json', 'r') as f:
        users_data = json.load(f)
        if username in users_data and users_data[username] == password:
            data={'msg':'success','user':'true','password':'false'}   
            return data
        else:
            if username in users_data:
                data={'msg':'error','user':'right','password':'wrong'}   
                return data
            else :
                data={'msg':'error','user':'wrong','password':'wrong'}
                return data

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')

@app.route('/submitproject', methods=['POST'])
def submitproject():
    return jsonify('success')

@app.route('/mainpage', methods=['POST','GET'])
def mainpage():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
