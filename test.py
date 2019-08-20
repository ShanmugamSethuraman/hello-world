from flask import Flask,render_template,request,g

fname = ""
sname = ""

app = Flask(__name__)

@app.route('/')
def shan():
    # return "shan"
    g.homepage = render_template("flamesForm.html")
    return g.homepage
@app.route('/' , methods = ["POST"])
def getvalue():
    g.fname = request.form['YourName']
    g.sname = request.form['PartnerName']
    print(g.fname, g.sname)
    return g.fname+g.sname

def runapp():
    print("printapp entry")
    app.run()
    print("printapp exit")
    return

def main():
    print("entry")
    runapp()
    # testfn = request.form['YourName']
    print(testfn)
    print("test00111")

main()
