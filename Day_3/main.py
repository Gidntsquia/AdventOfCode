import re
# Written by Jaxon Lee (GidntSquia)
# Advent of Code Day 3
# 12/??/2022
#
# Feel free to take whatever you'd like!

# Commonly used command- 
# nums = [int(s) for s in re.findall(r'\d+', line)]

    
# This figures out which letter is in the first and second half of each line, 
# and then adds that letter's value to the solution sum. a-z have 1-26 and A-Z 
# have 27-52
# This gives the answer to part 1.
def part1():
    f = open('Day_3/input.txt')
    solution = 0

    # This runs the code on all the lines of the input. 
    for line in f.readlines():
        # Split the line in half to get the contents of each compartment.
        first_compartment, second_compartment = line[:len(line)//2], line[len(line)//2:]
        
        # Find the overlap with sets and itersection
        overlap = set(first_compartment).intersection(second_compartment).pop()
        
        # Branch between lower and uppercase letters
        if (re.match(r'[a-z]', overlap)):
            solution += ord(overlap) - ord('a') + 1
        else:
            solution += ord(overlap) - ord('A') + 27
    
    print("Part 1 Solution: " + str(solution))
    f.close()

# 
# This gives the answer to part 2.
def part2():
    f = open('Day_3/input.txt')
    solution = 0
    members = ["", "", ""]
    member_count = 0
    

    # This runs the code on all the lines of the input. 
    for line in f.readlines():
        # Keep track of each member in each group. Make sure to get rid of the 
        # newline character at the end with "strip".
        members[member_count] = line.strip()
        member_count += 1
        
        # Once we have the full group, find out which element is in all three
        # rucksacks. 
        if (member_count == 3):
            member_count = 0
            # Find the overlap with sets and itersection
            overlap = set(members[0]).intersection(members[1]).intersection(members[2]).pop()
            # Branch between lower and uppercase letters
            if (re.match(r'[a-z]', overlap)):
                solution += ord(overlap) - ord('a') + 1
            else:
                solution += ord(overlap) - ord('A') + 27
    
    print("Part 2 Solution: " + str(solution))
    f.close()


if __name__ == "__main__":
    print("hello!")
    
    
    part1()
    part2()
    