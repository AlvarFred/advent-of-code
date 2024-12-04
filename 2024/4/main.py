import numpy as np
import re

def part1(file):
    lines = []
    finds = 0
    for line in file:
        lines.append(list(line.strip()))
        finds += len(re.findall("XMAS",line))
        finds += len(re.findall("SAMX",line))

    matrix = np.array(lines)
    
    diags = [matrix[::-1,:].diagonal(i) for i in range(-matrix.shape[0]+1,matrix.shape[1])]
    diags.extend(matrix.diagonal(i) for i in range(matrix.shape[1]-1,-matrix.shape[0],-1))


    for n in diags:
        line = ''.join(n.tolist())
        finds += len(re.findall("XMAS",line))
        finds += len(re.findall("SAMX",line))
    
    for row in matrix.transpose():
        line = ''.join(row.tolist())
        finds += len(re.findall("XMAS",line))
        finds += len(re.findall("SAMX",line))
    return finds


def part2(file):
    lines = []
    total = 0
    
    for line in file:
        lines.append(line)
    # Don't need to search the first and last row and column 
    for i in range(1,len(lines)-1):
        for j in range(1,len(lines[i])-2):
            if lines[i][j] == "A":
                diagonal = lines[i-1][j-1] + 'A' + lines[i+1][j+1]
                if diagonal == "SAM" or diagonal == "MAS":
                    diagonal = lines[i+1][j-1] + 'A' + lines[i-1][j+1]
                    if diagonal == "SAM" or diagonal == "MAS":
                        total += 1
    return total 
            
def main():
    file = open("input.txt", "r")
    print("Part 1: ", part1(file))
    file = open("input.txt", "r")
    print("Part 2: ", part2(file))

if __name__ == "__main__":
    main()