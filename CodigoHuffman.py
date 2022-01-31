class Nodes:  
    
    def __init__(self, probability, symbol, left = None, right = None):  
        self.probability = probability  
        self.symbol = symbol  
        self.left = left  
        self.right = right  
        self.code = ''  
              
codes = dict() 

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

