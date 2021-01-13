class Tree(object):
    def __init__(self):
        self.root = Node(None, None, None, None)

    def createTreeFromFreq(self, freq):
        if len(freq) == 1:
            root = Node(None, None, freq[0][1], freq[0][0])

        elif len(freq) == 2:
            leftChild = Node(None, None, freq[0][1], freq[0][0])
            rightChild = Node(None, None, freq[1][1], freq[1][0])
            self.root = Node(leftChild, rightChild, leftChild.value + rightChild.value, None)

        elif len(freq) > 2:
            for i in range(len(freq)):
                freq[i] = Node(None, None, freq[i][1], freq[i][0])

            while freq:
                if len(freq) == 1:
                    self.root = freq.pop()
                
                else:
                    leftNode = freq.pop(0)
                    rightNode = freq.pop(0)
                    node = Node(leftNode, rightNode, leftNode.value + rightNode.value, None)

                    inserted = False
                    for i in range(len(freq)):
                        if freq[i].value > node.value:
                            freq.insert(i, node)
                            inserted = True
                            break
                    
                    if not inserted:
                        freq.append(node)

    # traverse the tree to check the implementation
    def encoderTraverseTree(self, node):
        if node == None:
            return

        self.encoderTraverseTree(node.leftChild)
        if node.char == "\n":
            print("key : %s , value : %d " %('\\n', node.value))
        else:
            print("key : %s , value : %d " %(node.char, node.value))

        self.encoderTraverseTree(node.rightChild)

    
    def decoderTraverseTree(self, node):
        if node == None:
            return
        self.decoderTraverseTree(node.leftChild)
        if node.char == "\n":
            print("key : %s " %('\\n'))
        else:
            print("key : %s " %(node.char))
        self.decoderTraverseTree(node.rightChild)


    def createTranslater(self):
        code = ''
        node = self.root
        codeDict = {}
        self.createTranslaterHelper(node, code, codeDict)
        return codeDict        

    
    def createTranslaterHelper(self, node, code, codeDict):
        if node == None:
            return

        self.createTranslaterHelper(node.leftChild, code + '0', codeDict)
        if node.char != None:
            codeDict[node.char] = code
        self.createTranslaterHelper(node.rightChild, code + '1', codeDict)

    
    def addNodeFromCode(self, char, code):
        pass

    def reconstructFromDict(self, charToCode):
        
        for char in charToCode.keys():
            code = charToCode[char]
            node = self.root

            for direction in code:

                if direction == "0":
                    if node.leftChild == None:
                        node.leftChild = Node(None, None, None, None)
                    node = node.leftChild
                
                else:
                    if node.rightChild == None:
                        node.rightChild = Node(None, None, None, None)
                    node = node.rightChild
            
            node.char = char


    

class Node(object):
    def __init__(self, leftChild, rightChild, value, char):
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.value = value
        self.char = char
