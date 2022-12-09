# Advent Of Code 2022 🎄
My code for December 2022's [Advent of Code](https://adventofcode.com) puzzles. All my solutions are in Python.

## Today's Solution! (Day 8) 🤗
```
import re
# Written by Jaxon Lee (GidntSquia)
# Advent of Code Day 8
# 12/8/2022
#
# Feel free to take whatever you'd like!

# Commonly used command- 
# nums = [int(s) for s in re.findall(r'\d+', line)]

    
# This finds the number of trees that are visible from outside the forest.
# This gives the answer to part 1.
def part1():
    X = [l.strip() for l in open('Day_8/input.txt')] 
    count = 0
    accounted_for = set([])
    
    # Start from left and look right
    my_row = 0
    for row in X:
        heights = [int(i) for i in row]
        my_col = 0
        biggest = -1
        for height in heights:
            if biggest < height:
                biggest = height
                if not (my_row, my_col) in accounted_for:
                    count+= 1
                    accounted_for.add((my_row, my_col))
                
            my_col += 1
        my_row += 1

    # Start from right and look left
    my_row = 0
    for row in X:
        heights = [int(i) for i in row]
        heights.reverse()

        my_col = 0
        biggest = -1
        for height in heights:
            if biggest < height:
                biggest = height
                if not (my_row, len(X[0]) - 1 - my_col) in accounted_for:
                    count+= 1
                    accounted_for.add((my_row, len(X[0]) - 1 - my_col))
            my_col += 1
            
        my_row += 1
        
    # Turn list of lines into 2d array of characters
    Q = [list(line) for line in X]
    
    # Start from top and look down
    for col in range(0, len(Q[0])):
        heights = []
        for row in range(0, len(Q)):
            heights.append(int(Q[row][col]))
        biggest = -1
        my_row = 0
        for height in heights:
            if biggest < height:
                biggest = height
                if not (my_row, col) in accounted_for:
                    count+= 1
                    accounted_for.add((my_row, col))
                    
            my_row += 1
                
    # Start from the bottom and look up
    for col in range(0, len(Q[0])):
        heights = []
        for row in range(0, len(Q)):
            heights.append(int(Q[row][col]))
        heights.reverse()

        biggest = -1
        my_row = 0
        for height in heights:
            # Row is correct, but columns are flipped
            if biggest < height:
                biggest = height
                if not (len(Q) - 1 - my_row, col) in accounted_for:
                    count+= 1
                    accounted_for.add((len(Q) - 1 - my_row, col))
            my_row +=1
    
    solution = count
        
    print("Part 1 Solution: " + str(solution))


# This finds the "optimal" treehouse location by finding the tree that can see
# the most trees horizontally/vertically.
# This gives the answer to part 2.
def part2():
    X = [l.strip() for l in open('Day_8/input.txt')] 
    Q = [list(line) for line in X]
    
    scenics = []
    # Go through each row/col index and find its scenic score
    for row in range(0, len(Q)):
        for col in range(0, len(Q[0])):
            my_height = Q[row][col]
            
            # 0 is left, 1 is right, 2 is up, and 3 is down.
            scores = [0, 0, 0, 0]
           
             # Go left
            for col_travel in range(col - 1, -1, -1):
                if (Q[row][col_travel] < my_height):
                    scores[0] += 1
                # View is blocked
                else:
                    scores[0] += 1
                    break
             # Go right
            for col_travel in range(col + 1, len(Q[0]), 1):
                if (Q[row][col_travel] < my_height):
                    scores[1] += 1
                # View is blocked
                else:
                    scores[1] += 1
                    break
            # Go up
            for row_travel in range(row - 1, -1, -1):
                if (Q[row_travel][col] < my_height):
                    scores[2] += 1
                # View is blocked
                else:
                    scores[2] += 1
                    break
            # Go down
            for row_travel in range(row + 1, len(Q), 1):
                if (Q[row_travel][col] < my_height):
                    scores[3] += 1
                # View is blocked
                else:
                    scores[3] += 1
                    break
                
            # Calculate scenic scores based on score of each direction.
            scenic_score = scores[0] * scores[1] * scores[2] * scores[3]
            scenics.append(scenic_score)
            
    solution = max(scenics)

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

- [📁](Day_8)`Day_*`: Solutions for each day of advent of code. Click to be taken to today's solution
    - [📋](Day_8/input.txt)`input.txt`: My puzzle input for today (Everyone's is different!)
    - [🏃](Day_8/main.py)`main.py`: Solution file. Run to get puzzle solution for today (make sure to put in your unique input)
- [📁](Template)`Template`: Template for solutions. Feel free to take it
    - [📋](Template/input.txt)`input.txt`: Empty file where you can put in the day's puzzle input 
    - [🏃](Template/main.py)`main.py`: Skeleton of a python file where you can put in the day's puzzle solution.


---------------
You can participate here:
https://adventofcode.com/

Join my private leaderboard! It has some UMD students 🐢

Link- https://adventofcode.com/2022/leaderboard/private

Code- 2114573-258bdd82
