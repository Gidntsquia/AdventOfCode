# Advent Of Code 2022 🎄
My code for December 2022's [Advent of Code](https://adventofcode.com) puzzles. All my solutions are in Python 3.10.1.

## Today's Solution! (Day 10) 🤗...[🏃](https://replit.com/@Gidntsquia/TodaysAoCSolution-Jaxon#main.py)
```
import math
# Written by Jaxon Lee (GidntSquia)
# Advent of Code Day 12
# 12/12/2022
#
# Feel free to take whatever you'd like!
    
# Gives the shortest path up the mountain from S.
# This gives the answer to part 1.
def part1():
    solution = 0
    X = [l.strip() for l in open('Day_12/input.txt')]
    Q = []
    for line in X:
        line_of_chars = []
        for i in range(len(line)):
            line_of_chars.append(line[i:i+1])
        Q.append(line_of_chars)
    
    for row in range(len(Q)):
        for col in range(len(Q[0])):
            if Q[row][col] == "S":
                start_pos = (row,col)
                Q[row][col] = "a"
            elif Q[row][col] == "E":
                end_pos = (row,col)
                Q[row][col] = "z"
        
    # Shortest path alg
    distances = [[math.inf for i in range(len(Q[0]))] for i in range(0,len(Q))]
    starty, startx = start_pos
    distances[starty][startx] = 0
    W = []
    W.append(start_pos)
    
    while len(W) > 0:
        pos = W.pop(0)
        (y, x) = pos
        
        directions = []
        
        # Go through each possible direction
        directions.append((y - 1, x))
        directions.append((y + 1, x))
        directions.append((y, x - 1))
        directions.append((y, x + 1))
        
        old_height = ord(Q[y][x])
        for direction in directions:
            new_y, new_x = direction
            if (new_y >= 0 and new_y < len(Q) and new_x >= 0 and new_x < len(Q[0])):
                if (distances[new_y][new_x] == math.inf):
                    new_height = ord(Q[new_y][new_x])
                    if (new_height - old_height <= 1):
                        distances[new_y][new_x] = distances[y][x] + 1
                        if (new_y, new_x) == end_pos:
                            solution = distances[new_y][new_x]
                            break
                            
                        W.append((new_y, new_x))
    print("Part 1 Solution: " + str(solution))

# Gives the shortest path up the mountain from S or any point with elevation "a".
# This gives the answer to part 2.
def part2():
    solution = 0
    X = [l.strip() for l in open('Day_12/input.txt')]
    Q = []
    for line in X:
        line_of_chars = []
        for i in range(len(line)):
            line_of_chars.append(line[i:i+1])
        Q.append(line_of_chars)
        
    starts = []
    for row in range(len(Q)):
        for col in range(len(Q[0])):
            if Q[row][col] == "S" or Q[row][col] == "a":
                starts.append( (row,col))
                Q[row][col] = "a"
            elif Q[row][col] == "E":
                end_pos = (row,col)
                Q[row][col] = "z"
                
    # Shortest path alg
    distances = [[math.inf for i in range(len(Q[0]))] for i in range(0,len(Q))]
    
    W = []
    for start in starts:
        starty, startx = start
        distances[starty][startx] = 0
        W.append(start)
    
    while len(W) > 0:
        pos = W.pop(0)
        (y, x) = pos
    
        directions = []
        
        # Go through each possible direction
        directions.append((y - 1, x))
        directions.append((y + 1, x))
        directions.append((y, x - 1))
        directions.append((y, x + 1))
        
        old_height = ord(Q[y][x])
        for direction in directions:
            new_y, new_x = direction
            if (new_y >= 0 and new_y < len(Q) and new_x >= 0 and new_x < len(Q[0])):                
                if (distances[new_y][new_x] == math.inf):
                    new_height = ord(Q[new_y][new_x])
                    if (new_height - old_height <= 1):
                        distances[new_y][new_x] = distances[y][x] + 1
                        
                        # This means we've found the end position. Could exit
                        # the while loop here.
                        if (new_y, new_x) == end_pos:
                            solution = distances[new_y][new_x]
                        W.append((new_y, new_x))
    
    print("Part 2 Solution: " + str(solution))

if __name__ == "__main__":
    print("hello!")
    
    part1()
    part2()
```

## Quickstart 🚀
```
git clone https://github.com/Gidntsquia/AdventOfCode
```
## Code Structure 📁
The code is broken up as follows:

- [📁](Day_12)`Day_*`: Solutions for each day of advent of code. Click to be taken to today's solution
    - [📋](Day_12/input.txt)`input.txt`: My puzzle input for today (Everyone's is different!)
    - [🏃](https://replit.com/@Gidntsquia/TodaysAoCSolution-Jaxon#main.py)`main.py`: Solution file. Run to get puzzle solution for today (make sure to put in your unique input)
- [📁](Template)`Template`: Template for solutions. Feel free to take it
    - [📋](Template/input.txt)`input.txt`: Empty file where you can put in the day's puzzle input 
    - [🏃](Template/main.py)`main.py`: Skeleton of a python file where you can put in the day's puzzle solution.


---------------
You can participate here:
https://adventofcode.com/

Join my private leaderboard! It has some UMD students 🐢

Link- https://adventofcode.com/2022/leaderboard/private

Code- 2114573-258bdd82
