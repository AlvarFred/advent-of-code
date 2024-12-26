

def part1(file):
    for line in file:
        id = 0
        disk = []
        sorting_steps = 0
        total_empty = 0
        for i in range(0,len(line),2):
            blocks = int(line[i])
            if i == len(line) - 1:
                empty_blocks = 0
            else:
                empty_blocks = int(line[i+1])
            file_blocks = [str(id) for i in range(blocks)]
            file_blocks.extend(['.' for i in range(empty_blocks)])
            disk.extend(file_blocks)
            sorting_steps += blocks
            total_empty += empty_blocks
            id += 1
        print(disk)
        blocks_to_be_moved = []
        for i in range(1,total_empty+1):
            if disk[-i] != '.':
                blocks_to_be_moved.append(disk[-i])
                # disk[-i] = '.'

        print(blocks_to_be_moved)
        sorted_disk = []
        for i in range(sorting_steps):
            if disk[i] == '.':
                sorted_disk.append(blocks_to_be_moved.pop(0))
            else:
                sorted_disk.append(disk[i])
        # Add . to the end, not necessary for solution
        # sorted_disk += "".join(['.' for i in range(total_empty)])
        checksum = 0
        for i in range(len(sorted_disk)):
            checksum += i * int(sorted_disk[i])
        print(sorted_disk)

        return checksum
    

def part2(file):
    pass

def main():
    file = open("input.txt", "r")
    print("Part 1: ", part1(file))
    file = open("example.txt", "r")
    print("Part 2: ", part2(file))

if __name__ == "__main__":
    main()