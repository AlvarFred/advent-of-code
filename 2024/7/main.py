

def part1(file):
    total = 0
    for line in file:
        parts = line.split()
        result = int(parts[0][:-1])
        numbers = list(map(int,parts[1:]))
        
        if calc(result, numbers[0], numbers[1:]):
            total += result
    return total

def calc(result,first, list):
    if first > result: return False
    if not list:
        return first == result
    if calc(result,first * list[0], list[1:]):
        return True
    else:
        return calc(result,first + list[0], list[1:])

# takes two numbers
# adds and multiply
# index?    

def part2(file):
    total = 0
    for line in file:
        parts = line.split()
        result = int(parts[0][:-1])
        numbers = list(map(int,parts[1:]))
        
        if calc2(result, numbers[0], numbers[1:]):
            total += result
    return total

def calc2(result,first, list):
    if first > result: return False
    if not list:
        return first == result
    if calc2(result,first * list[0], list[1:]):
        return True
    elif calc2(result,first + list[0], list[1:]):
        return True
    else:
        concat = int(str(first) + str(list[0]))
        return calc2(result, concat, list[1:])

def main():
    file = open("input.txt", "r")
    print("Part 1: ", part1(file))
    file = open("input.txt", "r")
    print("Part 2: ", part2(file))

if __name__ == "__main__":
    main()