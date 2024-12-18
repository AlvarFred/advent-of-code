

def part1(file):
    guard_pos = []
    
   # 0: up, 1: right, 2: down, 3: left
    obstacles = {}
    # check if obs infornt
    # if yes turn right
    # else check if forward is out; if yes exit
    # if no go forward
    y = 0
    x = 0
    for line in file:
        x = 0
        for c in line:
            if c == "#":
                obstacles[f"{x},{y}"] = True
            elif c == "^":
                guard_pos = [x,y]
            x += 1
        y += 1
    visited = list(dict.fromkeys(find_way(guard_pos,obstacles,x,y)))
    return(len(visited) + 1)

def find_way(guard_pos,obstacles,x,y):
    visited = []
    dir = 0 
    visited.append(f"{guard_pos[0]},{guard_pos[1]}")
    while(True):
        if dir == 4: dir = 0
        # Up
        if dir == 0:
            if guard_pos[1] == 0:
                break
            if f"{guard_pos[0]},{guard_pos[1]-1}" in obstacles:
                dir += 1
            else:
                visited.append(f"{guard_pos[0]},{guard_pos[1]}")
                guard_pos[1] -= 1
        # Right
        if dir == 1:
            if guard_pos[0] == x-1:
                break
            if f"{guard_pos[0]+1},{guard_pos[1]}" in obstacles:
                dir += 1
            else:
                visited.append(f"{guard_pos[0]},{guard_pos[1]}")

                guard_pos[0] += 1
        # Down
        if dir == 2:
            if guard_pos[1] == y-1:
                break
            if f"{guard_pos[0]},{guard_pos[1]+1}" in obstacles:
                dir += 1
            else:
                visited.append(f"{guard_pos[0]},{guard_pos[1]}")

                guard_pos[1] += 1
        # Left
        if dir == 3:
            if guard_pos[0] == 0:
                break
            if f"{guard_pos[0]-1},{guard_pos[1]}" in obstacles:
                dir += 1
            else:
                visited.append(f"{guard_pos[0]},{guard_pos[1]}")

                guard_pos[0] -= 1
    return visited
    

    

def part2(file):
    guard_start_pos = []
    # 0: up, 1: right, 2: down, 3: left
    dir = 0 
    obstacles = {}
    
    y = 0
    x = 0
    for line in file:
        x = 0
        for c in line:
            if c == "#":
                obstacles[f"{x},{y}"] = True
            elif c == "^":
                guard_start_pos = [x,y]
            x += 1
        y += 1
   
    total = 0
    guard_pos = []
    print(guard_start_pos)
    try_pos = find_way(guard_start_pos.copy(),obstacles,x,y)
    # del try_pos[0]
    try_pos = list(dict.fromkeys(try_pos))
    print(len(try_pos))
    i = 0
    print(try_pos)
    # try_pos = try_pos[4115:]
    for pos in try_pos:
        # print(i)
        i += 1
        positions  = pos.split(",")
        # print(positions)
        if f"{positions[0]},{positions[1]}" in obstacles: continue
        obstacles[f"{positions[0]},{positions[1]}"] = True
        
        visited = []
        guard_pos = guard_start_pos.copy()
        # print(len(obstacles))

        dir = 0
        # visited.append(f"{guard_pos},{dir}")
        while(True):
            if dir == 4: dir = 0
            # print(positions)
            # print(guard_pos, dir)
            # print()
            if f"{guard_pos},{dir}" in visited:
                print(positions)
                total +=1
                break
            # Up
            if dir == 0:
                if guard_pos[1] == 0:
                    break
                if f"{guard_pos[0]},{guard_pos[1]-1}" in obstacles:
                    dir += 1
                else:
                    visited.append(f"{guard_pos},{dir}")

                    guard_pos[1] -= 1
            # Right
            elif dir == 1:
                if guard_pos[0] == x-1:
                    break
                if f"{guard_pos[0]+1},{guard_pos[1]}" in obstacles:
                    dir += 1
                else:
                    visited.append(f"{guard_pos},{dir}")
                    guard_pos[0] += 1
            # Down
            elif dir == 2:
                if guard_pos[1] == y-1:
                    break
                if f"{guard_pos[0]},{guard_pos[1]+1}" in obstacles:
                    dir += 1
                else:
                    visited.append(f"{guard_pos},{dir}")
                    guard_pos[1] += 1
            # Left
            elif dir == 3:
                if guard_pos[0] == 0:
                    break
                if f"{guard_pos[0]-1},{guard_pos[1]}" in obstacles:
                    dir += 1
                else:
                    visited.append(f"{guard_pos},{dir}")

                    guard_pos[0] -= 1
        del obstacles[f"{positions[0]},{positions[1]}"]

    return(total)

def main():
    file = open("input.txt", "r")
    print("Part 1: ", part1(file))
    file = open("example.txt", "r")
    print("Part 2: ", part2(file))

if __name__ == "__main__":
    main()