# import commonFunctions
ismatch = False

def getUserInput():
    name1 = input("please enter your name: ")
    name2 = input("please enter your partner name: ")
    print("we are going to calculate FLAMES for "+name1+" and " + name2)
    return name1, name2


def convertStringToList(na):
    name1 = na[0]
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


def doFlames(totalLength):
    flamesnumber = int(totalLength%6)
    # print("flamesNumber : "+str(flamesnumber))
    flamesvalue = getFlamesValue(flamesnumber)
    return flamesvalue


def getFlamesValue(flamesnumber):
    if flamesnumber == 1:
        return "Friends"
    if flamesnumber == 2:
        return "Lovers"
    if flamesnumber == 3:
        return "Affection"
    if flamesnumber == 4:
        return "Marriage"
    if flamesnumber == 5:
        return "Enemies"
    if flamesnumber == 0:
        return "Sisters"


def validateNames(na):
    name1 = na[0];
    name2 = na[1];
    length1 = len(name1)
    length2 = len(name2)
    print("last letter:"+str(name1[length1-1]))


def main():

    names = getUserInput()
    namestolist = convertStringToList(names)
    validateNames(namestolist)
    totalLength = getUniqueCharacters(namestolist)
    flamesOutput = doFlames(totalLength)
    print("")
    print("FLAMES result for '"+str(names[0])+"' and '"+str(names[1])+"' is ---->  "+flamesOutput)
    print("")
    playagain = input("Enter 'Y' to play again else press any key to exit: ")

    if playagain == "Y" or playagain == "y":
        main()
    else:
        print("Thanks for playing !!")


main()

