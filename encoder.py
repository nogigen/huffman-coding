from operator import itemgetter
from tree import Tree
import copy
import sys


def getIndexFromFreq(freq, key):
    for i,data in enumerate(freq):
        if data[0] == key:
            return i

def createFreqTable(counterDict):
    freq = []

    for key in counterDict.keys():
        freq.append( (key, counterDict[key]) )

    freq.sort(key=itemgetter(1))
    
    return freq

def encode(inputFilename):

    
    file = open(inputFilename, "r")

    message = file.read().rstrip()
    
    charCounter = {}
    for ch in message:
        if type(ch) == "int":
            ch = str(ch)

        if ch in charCounter:
            charCounter[ch] = charCounter[ch] + 1
        else:
            charCounter[ch] = 0
    file.close()

    freq = createFreqTable(charCounter)
    

    # test, https://www.codesdope.com/course/algorithms-huffman-codes/#:~:text=Huffman%20code%20is%20a%20data,characters%20appearing%20in%20a%20file.&text=Now%20if%20we%20use%20characters,100%20characters%20of%20the%20file.
    #freq = [('c', 5),('d', 10),('e', 11),('f', 12),('b', 20),('a', 42)]
    freqToTree = copy.deepcopy(freq)
    tree = Tree()
    tree.createTreeFromFreq(freqToTree)
    codeDict = tree.createTranslater()
    
    encryptedMessage = ""
    for ch in message:
        encryptedMessage = encryptedMessage + codeDict[ch]

    file = open("encryptedMessage.txt", "w")
    file.write(encryptedMessage)
    file.close()
    

    file = open("translator.txt", "w")
    for key in codeDict.keys():
        if key == '\n':
            line = "%s %s" %('\\n', codeDict[key])
        else :
            line = "%s %s" %(key, codeDict[key])
        file.write(line + "\n")
    file.close()
    

    file = open("statistics.txt", "w")
    initialBits = len(message) * 8

    numberOfBitsEncrypted = 0
    numberOfBitsTable = 0

    for char in codeDict.keys():
        index = getIndexFromFreq(freq, char)
        numberOfBitsEncrypted = numberOfBitsEncrypted + len(codeDict[char]) * freq[index][1]
        numberOfBitsTable = numberOfBitsTable + 8 + len(codeDict[char])

    encryptedBits = numberOfBitsEncrypted + numberOfBitsTable

    file.write("The number of bits in the initial message is : %d\n" %(initialBits))
    file.write("The number of bits in the encrypted message is : %d\n" %(numberOfBitsEncrypted))
    file.write("The number of bits needed for the create the translation table is : %d\n" %(numberOfBitsTable))
    file.write("So, total bits needed to do this encryption is : %d\n" %(encryptedBits))
    file.write("compression ratio is %f \n" %(initialBits/encryptedBits))
    file.write("space saving is %f" %(1 - encryptedBits/initialBits))

    file.close()




argList = list(sys.argv)
filename = argList[1]
encode(filename)


