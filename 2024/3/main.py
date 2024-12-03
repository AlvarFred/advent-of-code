import re

def part1(file):
    total = 0
    for line in file:
        matches = re.findall("mul\(([0-9]{1,3},[0-9]{1,3})\)", line)
        for match in matches:
            numbers = match.split(",")
            total += int(numbers[0]) * int(numbers[1])
    return total

def part2(file):
    total = 0
    enabled = True
    for line in file:
        matches = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", line)
        for match in matches:
            if match == "do()": 
                enabled = True
                continue        
            if match == "don't()": 
                enabled = False
                continue
            if enabled:
                numbers = match[4:-1].split(",")
                total += int(numbers[0]) * int(numbers[1])
    return total

def main():
    file = open("input.txt", "r")
    print("Part 1: ", part1(file))
    file = open("input.txt", "r")
    print("Part 2: ", part2(file))

if __name__ == "__main__":
    main()