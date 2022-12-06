import re
# Written by Jaxon Lee (GidntSquia)
# Advent of Code Day 2
# 12/6/2022
#
# Feel free to take whatever you'd like!

# Commonly used command- 
# nums = [int(s) for s in re.findall(r'\d+', line)]

    
# This gives my score given X means rock, Y means paper, and Z means scizzors.
# A means my opponent plays rock, B means paper, and C means scizzors. 
# This gives the answer to part 1.
def part1():
    f = open('Day_2/input.txt')
    solution = 0

    move_dict = {
        "A" : 1,
        "B" : 2,
        "C" : 3,
        "X" : 1,
        "Y" : 2,
        "Z" : 3,
        ("A", "X") : 3,
        ("A", "Y") : 6,
        ("A", "Z") : 0,
        ("B", "X") : 0,
        ("B", "Y") : 3,
        ("B", "Z") : 6,
        ("C", "X") : 6,
        ("C", "Y") : 0,
        ("C", "Z") : 3,
        
    }
    # This runs the code on all the lines of the input. 
    for line in f.readlines():
        moves = [str(s) for s in re.findall(r'[A-CX-Z]', line)]
        solution += move_dict[moves[1]] + move_dict[(moves[0],moves[1])]
    
    print("Part 1 Solution: " + str(solution))
    f.close()

# This gives my total score given that X means lose, Y means draw, and Z means win.
# This gives the answer to part 2.
def part2():
    f = open('Day_2/input.txt')
    solution = 0
    move_dict = {
        "A" : 1,
        "B" : 2,
        "C" : 3,
        "X" : 1,
        "Y" : 2,
        "Z" : 3,
        ("A", "X") : 0 + 3,
        ("A", "Y") : 3 + 1,
        ("A", "Z") : 6 + 2,
        ("B", "X") : 0 + 1,
        ("B", "Y") : 3 + 2,
        ("B", "Z") : 6 + 3,
        ("C", "X") : 0 + 2,
        ("C", "Y") : 3 + 3,
        ("C", "Z") : 6 + 1,
        
    }
    # This runs the code on all the lines of the input. 
    for line in f.readlines():
        moves = [str(s) for s in re.findall(r'[A-CX-Z]', line)]
        solution += move_dict[(moves[0],moves[1])]
        
        
    print("Part 2 Solution: " + str(solution))
    f.close()


if __name__ == "__main__":
    print("hello!")
    
    
    part1()
    part2()
    
    