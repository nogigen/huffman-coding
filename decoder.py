from tree import Tree

# reconstruct the huffman tree from the table (translator.txt)
file = open("translator.txt", "r")
charToCode = {}
for line in file:
    line = line.rstrip().rsplit(" ", 1)
    char = line[0]
    code = line[1]

    if char == "\\n":
        charToCode["\n"] = code
        
    else:
        charToCode[char] = code


tree = Tree()
tree.reconstructFromDict(charToCode)
#tree.decoderTraverseTree(tree.root)

# decrpyt the message
file = open("encryptedMessage.txt", "r")
encrypedMessage = file.read().rstrip()
file.close()


decryptedMessage = ""
node = tree.root
for code in encrypedMessage:
    # if node is a leaf or if it has a char (its the same thing, you can check one of them, just an implementation detail)

    if code == "0":
        node = node.leftChild
    else:
        node = node.rightChild
    
    if node and node.char:
        decryptedMessage = decryptedMessage + node.char
        node = tree.root

# write decryptedMessage to a file
file = open("decryptedMessage.txt", "w")
file.write(decryptedMessage)
file.close()