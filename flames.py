from flask import Flask,render_template,request
import time


ismatch = False


def getUserInput():
    name1 = input("please enter your name: ")
    name2 = input("please enter your partner name: ")
    print("")
    print("we are going to calculate FLAMES for "+name1+" and " + name2)
    print("")
    print("Calculating.Please wait..............................................")
    time.sleep(2)
    return name1, name2


def convertStringToList(na):
    na1 = str(na[0])
    name1 = na1.strip()
    name2 = na[1]
    nametolist1 = list(name1)
    nametolist2 = list(name2)
    return nametolist1, nametolist2


def getUniqueCharacters(na):
    name1 = na[0]
    name2 = na[1]
    lengthName1 = int(len(name1))
    global ismatch
    ismatch = False
    matchingletters = []
    nonmatchingletters = []
    # print("nameList1: "+str(name1))
    # print("nameList2: "+str(name2))

    for x in range(lengthName1):
        x = 0
        # print(name1[x])
        lengthName2 = int(len(name2))
        for y in range(lengthName2):
            if name1[x] == name2[y]:
                matchingletters.append(name2[y])
                name1.pop(x)
                name2.pop(y)
                ismatch = True
                # print("ismatch: "+str(ismatch))
                # print("inLoop matchingList"+str(matchingletters))
                # print("inLoop name1List"+str(name1))
                # print("inLoop name1List2" + str(name2))
                break
            else:
                ismatch = False
                # print("ismatch: "+str(ismatch))
        if ismatch == False:
            nonmatchingletters.append(name1[x])
            name1.pop(x)
        if len(name2) == 0 and len(name1) > 0:
            nonmatchingletters.extend(name1)
            break
    #         print("nonMatching" + str(nonmatchingletters))
    # print("final match : "+str(matchingletters))
    # print("final nonmatch : "+str(nonmatchingletters))
    # print("final Name 2 : "+str(name2));
    totalLength = int(len(nonmatchingletters)+len(name2))
    # print("Final Length : "+str(totalLength))
    return totalLength

def splitandjoin(selectedchar,iterationvalue):
    splitstring = iterationvalue.split(selectedchar)
    concatedStrong = splitstring[1]+splitstring[0]
    return concatedStrong


def doFlames(totalLength):
    flamesstring = "FLAMES"
    length1 = int(totalLength%6)
    getcharacter1 = flamesstring[length1-1]
    iteration1 = splitandjoin(getcharacter1, flamesstring)
    # print("iteration1" + str(iteration1))
    length2 = int(totalLength % 5)
    getcharacter2 = iteration1[length2 - 1]
    iteration2 = splitandjoin(getcharacter2,iteration1)
    # print("iteration2" + str(iteration2))
    length3 = int(totalLength % 4)
    getcharacter3 = iteration2[length3-1]
    iteration3 = splitandjoin(getcharacter3, iteration2)
    # print("iteration3" + str(iteration3))
    length4 = int(totalLength % 3)
    getcharacter4 = iteration3[length4 - 1]
    iteration4 = splitandjoin(getcharacter4, iteration3)
    # print("iteration4" + str(iteration4))
    length5 = int(totalLength % 2)
    getcharacter5 = iteration4[length5 - 1]
    iteration5 = splitandjoin(getcharacter5, iteration4)
    # print("iteration5" + str(iteration5))
    return iteration5


def getFlamesValue(finalcharacter,na):
    name1 = na[0]
    name2 = na[1]
    if finalcharacter == "F":
        return name1 +" and "+name2+" are FRIENDS"
    if finalcharacter == "L":
        return name2 +" is in LOVE with "+name1
    if finalcharacter == "A":
        return name2 +" is ATTRACTED to "+name1
    if finalcharacter == "M":
        return name1 +" will get MARRIED to "+name2
    if finalcharacter == "E":
        return name1 +" and "+name2+" are ENIMIES"
    if finalcharacter == "S":
        return name1 +" and "+name2+" are SISTERS/BROTHERS"


def validateNames(na):
    name1 = na[0];
    name2 = na[1];
    length1 = len(name1)
    length2 = len(name2)
    # print("last letter:"+str(name1[length1-1]))


def main():
    app = Flask(__name__)
    @app.route('/')
    def index():
        return render_template("flamesForm.html")
    @app.route('/', methods = ['post'])
    def getvalue():
        fname = request.form['YourName']
        sname = request.form['PartnerName']
        names = fname, sname
        namestolist = convertStringToList(names)
        validateNames(namestolist)
        totalLength = getUniqueCharacters(namestolist)
        finalcharacter = doFlames(totalLength)
        flamesresult = getFlamesValue(finalcharacter, names)
        print(flamesresult)
        return flamesresult
    app.run()
    # names = getUserInput()
    # namestolist = convertStringToList(names)
    # validateNames(namestolist)
    # totalLength = getUniqueCharacters(namestolist)
    # finalcharacter = doFlames(totalLength)
    # flamesresult = getFlamesValue(finalcharacter,names)
    # print("")
    # print(flamesresult)
    # print("")
    # print("")
    playagain = input("Enter 'Y' to play again else press any key to exit: ")

    if playagain == "Y" or playagain == "y":
        main()
    else:
        print("Thanks for playing !!")



main()
