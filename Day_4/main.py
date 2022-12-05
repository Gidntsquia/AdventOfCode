import re
    
    
# This gets the number of assignment pairs that completely overlap.
# This gives the answer to part one. 
def get_subsection_count():
    f = open('Day_4/input.txt')
    count = 0
    # This runs the code on all the lines of the input. 
    for line in f.readlines():
        # This extracts the numbers from each line and puts it in a nice array.
        nums = [int(s) for s in re.findall(r'\d+', line)]
        if nums[0] <= nums[2] and nums[1] >= nums[3]:
            count += 1
        elif nums[0] >= nums[2] and nums[1] <= nums[3]:
            count +=1
    print("Completely overlapping: " + str(count))
    f.close()
    
# This gets the number of assignment pairs that overlap at all.
# This gives the answer to part one. 
def get_overlap_count():
    f = open('Day_4/input.txt')
    count = 0
    # This runs the code on all the lines of the input. 
    for line in f.readlines():
        # This extracts the numbers from each line and puts it in a nice array.
        nums = [int(s) for s in re.findall(r'\d+', line)]
        if nums[2] in range(nums[0], nums[1]+1) or nums[3] in range(nums[0], nums[1]+1):
            count += 1
        elif nums[0] in range(nums[2], nums[3]+1) or nums[1] in range(nums[2], nums[3]+1):
            count += 1
    print("Somewhat overlapping: " + str(count))
    f.close()
        

if __name__ == "__main__":
    print("hello!")
    
    get_subsection_count()
    get_overlap_count()
    
    