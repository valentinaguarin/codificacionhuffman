class Nodes:  
    
    def __init__(self, probability, symbol, left = None, right = None):  
        self.probability = probability  
        self.symbol = symbol  
        self.left = left  
        self.right = right  
        self.code = ''  
              
codes = dict()

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

