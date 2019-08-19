import requests
import  bs4 as bs
import lark


def main():
    pagedata = requests.get("https://coinmarketcap.com/currencies/nav-coin/")
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


main()
