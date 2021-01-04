from operator import itemgetter
class Tree(Object):
    pass

class Node(Object):
    pass


def createTree(freq):
    pass

def createFreqTable(counterDict):
    freq = []

    for key in counterDict.keys():
        freq.append( (key, counterDict[key]) )

    freq.sort(key=itemgetter(1))

    return freq

def encoder():

    file = open("message.txt", "r")

    message = file.read()
    
    charCounter = {}
    for ch in message:
        if type(ch) == "int":
            ch = str(ch)

        if ch in charCounter:
            charCounter[ch] = charCounter[ch] + 1
        else:
            charCounter[ch] = 0
    file.close()

    createFreqTable(charCounter)


encoder()

