
def part1(file):
    updates = []
    solution = []
    update_part = False
    for line in file:
        if line == '\n': 
            update_part = True
            continue
        if update_part:
            updates.append(line)
        else:
            numbers = line.strip().split("|")
            index0 = None
            if numbers[1] not in solution:
                print(numbers[1], " is added")
                # indexes[numbers[1]] = len(solution)
                solution.append(numbers[1])
            if numbers[0] in solution:
                index0 = solution.index(numbers[0])
                if index0 > solution.index(numbers[1]):
                    del solution[index0]
                    print(numbers[0], " deleted at: ", index0)
                else: continue
            print(numbers[0], " is added")

            solution.insert(solution.index(numbers[1]), numbers[0])
            # indexes[numbers[0]] = indexes[numbers[1]]
            # indexes[numbers[1]] += 1

            # print (numbers)

    total = 0
    for update in updates:
        update_list = update.strip().split(',')
        # print(update_list)
        if is_ordered_subsequence(update_list, solution):
            total += int(update_list[len(update_list) // 2])
        # print (update_list, is_ordered_subsequence(update_list, solution))
    print(solution)
    return total

def is_ordered_subsequence(sub, main):
    it = iter(main)
    return all(item in it for item in sub)
    

def part2(file):
    pass

def main():
    file = open("input.txt", "r")
    print("Part 1: ", part1(file))
    file = open("input.txt", "r")
    print("Part 2: ", part2(file))

if __name__ == "__main__":
    main()