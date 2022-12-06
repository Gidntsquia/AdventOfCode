import re
# Written by Jaxon Lee (GidntSquia)
# Advent of Code Day 1
# 12/6/2022
#
# Feel free to take whatever you'd like!

# Commonly used command- 
# nums = [int(s) for s in re.findall(r'\d+', line)]

    
# This gets the elf with the highest calories.
# This gives the answer to part 1.
def part1():
    f = open('Day_1/input.txt')
    solution = 0
    max = 0
    running = 0
    
    input = f.read().split("\n\n")
    for string in input:
        if (len(string) > 0): 
            for i in string.split("\n"):
                try:
                    running += int(i)
                except:
                    pass
            
            if running > max:
                max = running
            running = 0
            
    solution = max
    print("Part 1 Solution: " + str(solution))
    f.close()

# This gets the elves with the top 3 calories.
# This gives the answer to part 2.
def part2():
    f = open('Day_1/input.txt')
    solution = 0
    max = [0, 0, 0]
    running = 0
    
    input = f.read().split("\n\n")
    for string in input:
        if (len(string) > 0): 
            for i in string.split("\n"):
                try:
                    running += int(i)
                except:
                    pass
            
            if running > max[-3]:
                max.append(running)
                max.sort()
            running = 0
            
    solution = sum(max[-3:])
    print("Part 2 Solution: " + str(solution))
    f.close()


if __name__ == "__main__":
    print("hello!")
    
    
    part1()
    part2()
    
    