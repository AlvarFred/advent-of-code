
def part1(file):
    rules = []
    updates = []
    update_part = False
    for line in file:
        if line == '\n': 
            update_part = True
            continue
        if update_part:
            updates.append(line)
        else:
            rules.append(line)
    print(rules)
    print(updates)
    pass

def part2(file):
    pass

def main():
    file = open("example.txt", "r")
    print("Part 1: ", part1(file))
    file = open("input.txt", "r")
    print("Part 2: ", part2(file))

if __name__ == "__main__":
    main()