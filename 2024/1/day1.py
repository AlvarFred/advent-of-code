import math

def part1():
    list1 = []
    list2 = []
    file = open("input.txt", "r")
    for line in file:
        numbers = line.split()
        list1.append(int(numbers[0]))
        list2.append(int(numbers[1]))
    list1.sort()
    list2.sort()
    total = 0
    for i in range(len(list1)):
        total += abs(list1[i] - list2[i])
    return total

def part2():
    list1 = []
    list2 = []
    file = open("input.txt", "r")
    for line in file:
        numbers = line.split()
        list1.append(int(numbers[0]))
        list2.append(int(numbers[1]))
    total = 0
    for i in range(len(list1)):
        total += list1[i] * list2.count(list1[i])
    return total


def main():
    print("Part 1: ", part1())
    print("Part 2: ", part2())

if __name__ == "__main__":
    main()
