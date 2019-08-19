from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def shan():
    # return "shan"
    return render_template("flamesForm.html")
    print("test01")
@app.route('/' , methods = ["POST"])
def getvalue():
    fname = request.form['YourName']
    sname = request.form['PartnerName']
    print(fname, sname)
    return fname,sname


app.run(debug=True)
