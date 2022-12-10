# Advent Of Code 2022 🎄
My code for December 2022's [Advent of Code](https://adventofcode.com) puzzles. All my solutions are in Python.

## Today's Solution! (Day 10) 🤗
```
import math
# Written by Jaxon Lee (GidntSquia)
# Advent of Code Day 10
# 12/10/2022
#
# Feel free to take whatever you'd like!
  
# This gets the signal strength during the cycles asked for in the question.
# This gives the answer to part 1.
def part1():
    solution = 0
    X = [l.strip() for l in open('Day_10/input.txt')]
   
    cycles = 0
    x_val = 1
    all_x_vals = []
    
    for line in X:
        words = line.split()
        match words[0]:
            case "noop":
                cycles +=1
                all_x_vals.append(x_val)
            case "addx":
                cycles += 1
                all_x_vals.append(x_val)
                
                cycles += 1
                all_x_vals.append(x_val)
                x_val += int(words[1])
    solution = all_x_vals[19]*20+all_x_vals[59]*60+all_x_vals[99]*100+all_x_vals[139]*140+all_x_vals[179]*180+all_x_vals[219]*220
    
    print("Part 1 Solution: " + str(solution))

# This updates the pixels array in part 2.
def update_pixels(pixels, x_val, cycles):
    row = int((cycles - 1) / 40)
    position = (cycles - 1) - 40 * row
    if (abs(x_val - position) <= 1):
        pixels[row][position] = "#"

# This uses to the "X" value to draw a picture on a simulated CRT screen.
# This gives the answer to part 2.
def part2():
    solution = 0
    X = [l.strip() for l in open('Day_10/input.txt')]
   
    cycles = 0
    x_val = 1
    pixels = [["." for i in range(40)] for i in range(6)] 

    for line in X:
        words = line.split()
        match words[0]:
            case "noop":
                cycles +=1 
                update_pixels(pixels, x_val, cycles)
            case "addx":
                cycles += 1
                update_pixels(pixels, x_val, cycles)
                
                cycles += 1
                update_pixels(pixels, x_val, cycles)
                
                x_val += int(words[1])
    for i in range(len(pixels)):
        pixels[i] = ''.join(pixels[i])
    pixels = '\n'.join(pixels)
    
    solution = pixels
    
    # The solution is "PZGPKPEB"
    print("Part 2 Solution:\n " + str(solution))


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

- [📁](Day_10)`Day_*`: Solutions for each day of advent of code. Click to be taken to today's solution
    - [📋](Day_10/input.txt)`input.txt`: My puzzle input for today (Everyone's is different!)
    - [🏃](Day_10/main.py)`main.py`: Solution file. Run to get puzzle solution for today (make sure to put in your unique input)
- [📁](Template)`Template`: Template for solutions. Feel free to take it
    - [📋](Template/input.txt)`input.txt`: Empty file where you can put in the day's puzzle input 
    - [🏃](Template/main.py)`main.py`: Skeleton of a python file where you can put in the day's puzzle solution.


---------------
You can participate here:
https://adventofcode.com/

Join my private leaderboard! It has some UMD students 🐢

Link- https://adventofcode.com/2022/leaderboard/private

Code- 2114573-258bdd82
