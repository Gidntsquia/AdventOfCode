import re
# Written by Jaxon Lee (GidntSquia)
# Advent of Code Day 6
# 12/6/2022
#
# Feel free to take whatever you'd like!

# Commonly used command- 
# nums = [int(s) for s in re.findall(r'\d+', line)]

    
# This finds the first series of 4 different characters and returns the index of
# the last character in that series.
# This gives the answer to part 1.
def part1():
    f = open('Day_6/input.txt')
    solution = 0
    
    # Make sure to strip the line of input to get rid of the new line character
    # at the end.
    test_str = f.readline().strip()
    four_char_windows = [test_str[i: i + 4] for i in range(len(test_str))]
    
    flag = True
    for my_str in four_char_windows:
        if flag:
            new_str = my_str
            for i in range(4):
                new_str, popped = new_str[:-1], new_str[-1]
                if popped in new_str:
                    break
                else:
                    if len(new_str) == 0:
                        # Add 4 to index to get correct "ending" character value
                        solution = four_char_windows.index(my_str) + 4
                        flag = False
        
                
    
    print("Part 1 Solution: " + str(solution))
    f.close()

# This finds the first series of 14 different characters and returns the index of
# the last character in that series.
# This gives the answer to part 2.
def part2():
    f = open('Day_6/input.txt')
    solution = 0
    
    # Make sure to strip the line of input to get rid of the new line character
    # at the end.
    test_str = f.readline().strip()
    fourteen_char_windows = [test_str[i: i + 14] for i in range(len(test_str))]
    
    flag = True
    for my_str in fourteen_char_windows:
        if flag:
            new_str = my_str
            for i in range(14):
                new_str, popped = new_str[:-1], new_str[-1]
                if popped in new_str:
                    break
                else:
                    if len(new_str) == 0:
                        # Add 14 to index to get correct "ending" character value
                        solution = fourteen_char_windows.index(my_str) + 14
                        flag = False
            
    
    print("Part 2 Solution: " + str(solution))
    f.close()


if __name__ == "__main__":
    print("hello!")
    
    part1()
    part2()
    
    