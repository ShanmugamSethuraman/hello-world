import requests
import bs4 as bs
from flask import Flask,render_template,request
import sys

def main():
    app = Flask(__name__)
    @app.route('/')
    def index():
        return render_template("cryptoCoinHomePage.html")
    @app.route('/', methods=['post'])
    def getvalue():
        coinname = request.form['coinName']
        # return "<h1>" + flamesresult + "</h1>"
        pagedata = requests.get("https://coinmarketcap.com/currencies/"+coinname+"/")
        # print(pagedata.text) #.find("price",0,10000000000000000))
        soup = bs.BeautifulSoup(pagedata.text,'lxml')
        # print(str(soup.find_all('script')[11].text))
        pricejson = str(soup.find_all('script')[11].text)
        split1 = pricejson.split('{',2)[2]
        # print(str(split1))
        split2 = split1.split(',',10)[1]
        # print(str(split2))
        split3 = split2.split(':',10)[1]
        print(str(split3))
        return "<h1>" + split3 + "</h1>"
    @app.route('/',methods=['post'])
    def test():
        return "shantest"
    app.run()

main()
