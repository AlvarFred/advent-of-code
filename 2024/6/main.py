

def part1(file):
    guard_pos = []
    dir = 0 # 0: up, 1: right, 2: down, 3: left
    obstacles = {}
    # check if obs infornt
    # if yes turn right
    # else check if forward is out; if yes exit
    # if no go forward
    y = 0
    x = 0
    for line in file:
        print(line)
        x = 0
        for c in line:
            if c == "#":
                obstacles[f"{x},{y}"] = True
            elif c == "^":
                guard_pos = [x,y]
            x += 1
        y += 1
    print(x,y)
    
    print(obstacles)
    print(guard_pos)
    visited = []
    visited.append(f"{guard_pos}")
    while(True):
        print(guard_pos)
        if dir == 4: dir = 0
        # Up
        if dir == 0:
            if guard_pos[1] == 0:
                break
            if f"{guard_pos[0]},{guard_pos[1]-1}" in obstacles:
                dir += 1
            else:
                visited.append(f"{guard_pos}")
                guard_pos[1] -= 1
        # Right
        if dir == 1:
            if guard_pos[0] == x-1:
                break
            if f"{guard_pos[0]+1},{guard_pos[1]}" in obstacles:
                dir += 1
            else:
                visited.append(f"{guard_pos}")

                guard_pos[0] += 1
        # Down
        if dir == 2:
            if guard_pos[1] == y-1:
                break
            if f"{guard_pos[0]},{guard_pos[1]+1}" in obstacles:
                dir += 1
            else:
                visited.append(f"{guard_pos}")

                guard_pos[1] += 1
        # Left
        if dir == 3:
            if guard_pos[0] == 0:
                break
            if f"{guard_pos[0]-1},{guard_pos[1]}" in obstacles:
                dir += 1
            else:
                visited.append(f"{guard_pos}")

                guard_pos[0] -= 1
        
    visited = list(dict.fromkeys(visited))
    return(len(visited) +1)

    

def part2(file):
    pass

def main():
    file = open("input.txt", "r")
    print("Part 1: ", part1(file))
    file = open("input.txt", "r")
    print("Part 2: ", part2(file))

if __name__ == "__main__":
    main()