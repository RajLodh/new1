from flask import Flask, render_template,request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

print("i am learning GIT")
@app.route('/data',methods = ['GET','POST'])
def data():
    user_data = request.form
    print(user_data)

    #return  "Data Captured"
if __name__ == '__main__':
     app.run(debug=True)