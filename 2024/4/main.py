import numpy as np
import re

regex = "XMAS|SAMX"

def part1(file):
    lines = []
    finds = 0
    for line in file:
        lines.append(list(line.strip()))
        finds += len(re.findall("XMAS",line))
        finds += len(re.findall("SAMX",line))
    # print(lines)
    matrix = np.array(lines)
    diags = [matrix[::-1,:].diagonal(i) for i in range(-matrix.shape[0]+1,matrix.shape[1])]

    # Now back to the original array to get the upper-left-to-lower-right diagonals,
    # starting from the right, so the range needed for shape (x,y) was y-1 to -x+1 descending.
    diags.extend(matrix.diagonal(i) for i in range(matrix.shape[1]-1,-matrix.shape[0],-1))

    # Another list comp to convert back to Python lists from numpy arrays,
    # so it prints what you requested.
    for n in diags:
        line = ''.join(n.tolist())
        finds += len(re.findall("XMAS",line))
        finds += len(re.findall("SAMX",line))
    
    for row in matrix.transpose():
        line = ''.join(row.tolist())
        finds += len(re.findall("XMAS",line))
        finds += len(re.findall("SAMX",line))
    return finds

# -1,-1 +1,-1
#-1,+1 +1,+1
#
def part2(file):
    lines = []
    for line in file:
        lines.append(line)

    for i in range(1,len(lines)-1):
        for j in range(1,len(lines[i])-1):
            if lines[i][j] == "A":
                diagonal = lines[i-1][j-1] + 'A' + lines[j+1][i+1]
                print(diagonal)    
            

def main():
    file = open("input.txt", "r")
    print("Part 1: ", part1(file))
    file = open("example.txt", "r")
    print("Part 2: ", part2(file))

if __name__ == "__main__":
    main()