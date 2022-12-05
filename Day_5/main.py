import re
# Written by Jaxon Lee (GidntSquia)
# 12/5/22


if __name__ == "__main__":
    print("hello!")
    stacks = []
    
    # Add stacks 1-9 and also stack 0 (which we will ignore).
    for i in range(0, 10):
        stacks.append([])
    
    # Add the stacks in the picture to lists. 
    stacks[1].extend(['G', 'T', 'R', 'W'])
    stacks[2].extend(['G', 'C', 'H', 'P', 'M', 'P', 'S', 'V', 'W'])
    stacks[3].extend(['C', 'L', 'T', 'S', 'G', 'M'])
    stacks[4].extend(['J', 'H', 'D', 'M', 'W', 'R', 'F'])
    stacks[5].extend(['P','Q', 'L', 'H', 'S', 'W', 'F', 'J'])
    stacks[6].extend(['P', 'J', 'D', 'N', 'F', 'M', 'S'])
    stacks[7].extend(['Z', 'B', 'D', 'F', 'G', 'C', 'S', 'J'])
    stacks[8].extend(['R', 'T', 'B'])
    stacks[9].extend(['H', 'N', 'W', 'L', 'C'])

    f = open('Day_5/input.txt')
    
    # Get rid of the picture at the beginning of the input.
    for i in range(0, 11):
        next(f)

    for line in f.readlines():
        # Read commands.
        # First number in command is # of crates to move. Maintain order (part 2)
        # Second number in command is start location
        # Third number in command to end location
        nums = [int(s) for s in re.findall(r'\d+', line)]
        num_crates = min(nums[0], len(stacks[nums[1]]))
        crates_to_move = stacks[nums[1]][-num_crates:]
        stacks[nums[1]] = stacks[nums[1]][:-num_crates]
        stacks[nums[2]].extend(crates_to_move)
        
    for stack in stacks:
        print(stack)
            
    f.close()