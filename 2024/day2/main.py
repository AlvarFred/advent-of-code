
def part1():   
    safe_reports = 0
    file = open("input.txt","r")
    for line in file:
        levels = line.split()
        print(levels)
        inc = True
        safe = True
     
        for i in range(len(levels) - 1):
            diff = int(levels[i]) - int(levels[i + 1])
            if abs(diff) > 3 or abs(diff) < 1:
                safe = False
                break
            if i == 0 and diff > 0:
                inc = False
            if inc and diff > 0: 
                safe = False
                break
            elif not inc and diff < 0:
                safe = False
                break
        if safe:
            safe_reports += 1
    return safe_reports

def part2():
    safe_reports = 0
    file = open("input.txt","r")
    for line in file:
        levels = line.split()
        
        for i in range(len(levels) + 1):
            levels_copy = levels.copy()
            if i > 0: del levels_copy[i - 1]
            inc = True
            safe = True
            for j in range(len(levels_copy) - 1):
                diff = int(levels_copy[j]) - int(levels_copy[j + 1])
                if abs(diff) > 3 or abs(diff) < 1:
                    safe = False
                    break
                if j == 0 and diff > 0:
                    inc = False
                if inc and diff > 0: 
                    safe = False
                    break
                elif not inc and diff < 0:
                    safe = False
                    break
            if safe:
                safe_reports += 1
                break
    return safe_reports
def main():
    print("Part 1: ", part1())
    print("Part 2: ", part2())


if __name__ == "__main__":
    main()