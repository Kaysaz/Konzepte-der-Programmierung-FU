import random as rd

keys = [chr(i) for i in range(ord('0'),ord('9')+1)]+[chr(i) for i in range(ord('A'),ord('Z')+1)]+[chr(i) for i in range(ord('a'),ord('z')+1)]
    
def generateDict():
    values = keys.copy()
    rd.shuffle(values)
    return(dict([(keys[i],values[i]) for i in range(0,len(keys))]))
    
def generateTestFUMatrix():
    matrix = []
    for i in range(0,9):
        line =[]
        for j in range(0,9):
            line.append(rd.choice(keys))
        matrix.append(line)
    return(matrix) 

def generateTestFUDict():
    wb = {}
    for i in [chr(i) for i in range(ord('A'),ord('I')+1)]:
        for j in [chr(i) for i in range(ord('1'),ord('9')+1)]:
            wb[i+j] = rd.choice(keys)
    return(wb)
