class Nodes:  
    
    def __init__(self, probability, symbol, left = None, right = None):  
        self.probability = probability  
        self.symbol = symbol  
        self.left = left  
        self.right = right  
        self.code = ''  
              
codes = dict()
def CalculateFreq(data):
    symbols = dict()
    for item in data:
        if symbols.get(item) == None:
            symbols[item] = 1
        else:
            symbols[item] += 1
    return symbols


def Processing(node, value=''):
    newValue = value + str(node.code)

    if (node.left):
        Processing(node.left, newValue)
    if (node.right):
        Processing(node.right, newValue)

    if (not node.left and not node.right):
        codes[node.symbol] = newValue

    return codes


def OutputEncoded(data, coding):
    encodingOutput = []
    for element in data:
        encodingOutput.append(coding[element])

    string = ''.join([str(item) for item in encodingOutput])
    return string

def FunctionEncoding(data):
    symbolWithProbs = CalculateFreq(data)
    symbols = symbolWithProbs.keys()
    probabilities = symbolWithProbs.values()

    print("\nSymbols: ", symbols, "\n")

    print("Probabilities: ", probabilities, "\n")

    nodes = []

    for symbol in symbols:
        nodes.append(Nodes(symbolWithProbs.get(symbol), symbol))

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.probability)
        right = nodes[0]
        left = nodes[1]
        left.code = 0
        right.code = 1

        newNode = Nodes(left.probability + right.probability, left.symbol + right.symbol, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    functionEncoding = Processing(nodes[0])
    print("Symbols with codes", functionEncoding, "\n")
    encodedOutput = OutputEncoded(data, functionEncoding)
    return encodedOutput, nodes[0]


def FunctionDecoding(encodedData, huffmanTree):
    treeHead = huffmanTree
    decodedOutput = []
    for x in encodedData:
        if x == '1':
            huffmanTree = huffmanTree.right
        elif x == '0':
            huffmanTree = huffmanTree.left
        try:
            if huffmanTree.left.symbol == None and huffmanTree.right.symbol == None:
                pass
        except AttributeError:
            decodedOutput.append(huffmanTree.symbol)
            huffmanTree = treeHead

    string = ''.join([str(item) for item in decodedOutput])
    return string

while True:
    try:

        
        entry = input("To exit enter: out \nEnter a text: ")
        if entry == "out":
            break

        if all (c.isalpha() or c ==" "  for c in entry):
            encoding, tree = FunctionEncoding(entry)  
            
            print("\tEncoded output: ", encoding, "\n")  
            print("\tDecoded Output: ", FunctionDecoding(encoding, tree),"\n")


    except :
        print("Try again")
        continue

