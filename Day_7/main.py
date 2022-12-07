import random
import re
# Written by Jaxon Lee (GidntSquia)
# Advent of Code Day 7
# 12/7/2022
#
# Feel free to take whatever you'd like!

# Commonly used command- 
# nums = [int(s) for s in re.findall(r'\d+', line)]

# Inspiration from:  #https://www.youtube.com/@jonathanpaulson5053
# Put scratch work here.

# This makes a running list of all directories created. Must be reset between
# parts
all_dirs = []
class Directory: 
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.size = 0
        self.my_ls = []
        all_dirs.append(self)
      
    def add_child(self, child):
        self.children.append(child)
    
    def update_size(self):
        self.size = 0
        files = '\n'.join(self.my_ls)
        
        # Sum all the non-directory file sizes
        self.size += sum([int(i) for i in re.findall(r'\d+', files)])
        
        # Sum all the directory file sizes recursively.
        for child_dir in self.children:
            child_dir.update_size()
            self.size += child_dir.size
            
    # "To string" function for debugging. Today's puzzle was very difficult.
    def  __str__(self):
        result = self.name + ": " + str(self.size)
        return result







# This gives the answer to part 1.
def part1():
    # Get input into array
    X = [l.strip() for l in open('Day_7/input.txt')]   
    
    # Split the input into commands + their output
    Q =('\n'.join(X)).split("$ ")

    root_dir = Directory('/', 0)
    curr_dir = root_dir
    for command in Q:
        # Put the command into a nicer format and separate the command and it's
        # output.
        my_commands = [s.rstrip() for s in command.split('\n')]
        if (len(my_commands) > 0):
            if ('cd' in my_commands[0]):
                name = ''.join(my_commands).split(' ')[1]
                if (name == '..'):
                    curr_dir = curr_dir.parent
                # "cd /" is only run at the beginning, and we actually want to
                # ignore it because we already have a root set up outside of the
                # loop. That's what this does.
                elif (name == '/'):
                    pass
                else:
                    parent_dir = curr_dir
                    curr_dir = Directory(name, parent_dir)
                    parent_dir.add_child(curr_dir)
                    
            elif ('ls' in my_commands[0]):
                curr_dir.my_ls =  my_commands[1:]


    # Recursively get sizes of entire tree.
    root_dir.update_size()
    
    solution = 0
    for dir in all_dirs:
        if dir.size <= 100000:
            solution += dir.size
    
    print("Part 1 Solution: " + str(solution))

# This creates a tree from the terminal input and returns the smallest file 
# we could delete to get to 30000000 unused space.
# This gives the answer to part 2.
def part2():  
    # Reset directories from part 1.
    global all_dirs
    all_dirs = []
    
     # Get input into array
    X = [l.strip() for l in open('Day_7/input.txt')]   
    
    # Split the input into commands + their output
    Q =('\n'.join(X)).split("$ ")

    root_dir = Directory('/', 0)
    curr_dir = root_dir
    for command in Q:
        # Put the command into a nicer format and separate the command and it's
        # output.
        my_commands = [s.rstrip() for s in command.split('\n')]
        if (len(my_commands) > 0):
            if ('cd' in my_commands[0]):
                name = ''.join(my_commands).split(' ')[1]
                if (name == '..'):
                    curr_dir = curr_dir.parent
                # "cd /" is only run at the beginning, and we actually want to
                # ignore it because we already have a root set up outside of the
                # loop. That's what this does.
                elif (name == '/'):
                    pass
                else:
                    parent_dir = curr_dir
                    curr_dir = Directory(name, parent_dir)
                    parent_dir.add_child(curr_dir)
                    
            elif ('ls' in my_commands[0]):
                curr_dir.my_ls =  my_commands[1:]


    # Recursively get sizes of entire tree.
    root_dir.update_size()
    
    used_space = root_dir.size

    solution = -1
    for dir in all_dirs:
        if (70000000 - used_space) + dir.size >= 30000000 and (dir.size < solution or solution == -1):
            solution = dir.size
        
    print("Part 2 Solution: " + str(solution))


if __name__ == "__main__":
    print("hello!")
    
    part1()
    part2()
    
    