# Advent Of Code 2022 🎄
My code for December 2022's [Advent of Code](https://adventofcode.com) puzzles. All my solutions are in Python 3.10.1.

## Today's Solution! (Day 13) 🤗...[🏃](https://replit.com/@Gidntsquia/TodaysAoCSolution-Jaxon#main.py)
```
# Written by Jaxon Lee (GidntSquia)
# Advent of Code Day 13
# 12/13/2022
#
# Feel free to take whatever you'd like!
import functools
    
# This tells if two lists are in the "correct" order
def helper(left, right):
    i = 0
    if left == [] and right == []:
        return (1, False)

    for i in range(len(left)):
        if i >= len(right):
            # Not in right order
            return (0, True)
        
        match left[i], right[i]:
            case int(l), int(r):
                if l < r:
                    return (1, True)
                elif l == r:
                    continue
                elif l > r:
                    # wrong order
                    return (0, True)
            case list(l), list(r):
                result, is_done = helper(l, r)
                if (is_done):
                    return (result, True)
                else:
                    continue
            case list(l), int(r):
                result, is_done = helper(l, [r])
                if (is_done):
                    return (result, True)
                else:
                    continue
            case int(l), list(r):
                result, is_done = helper([l], r)
                if (is_done):
                    return (result, True)
                else:
                    continue
    if (len(right) > len(left)):
        return (1, True)
    else:
        return (1, False)

# This uses helper to compare two lists for ordering purposes.
def compare(list1, list2):
    result, is_done = helper(list1, list2)
    if result == 1:
        return -1
    else:
        return 1
                
# This tells us the number of correct orderings of the packet pairs and 
# where manually placed in markers lie after sorting.
# This gives the answer to part 1 and part 2.
def solutions():
    s1 = 0
    s2 = 0
    X = [l.strip() for l in open('Day_13/input.txt')]
    Q = '\n'.join(X).split('\n\n')
    T = []
    pair_num = 1
    for pair in Q:
        left, right = pair.split('\n')
        left, right = eval(left), eval(right)
        T.append(left)
        T.append(right)
        result, is_done = helper(left, right)
        s1 += pair_num * result
        pair_num += 1
        
    # Add the markers needed for part 2
    T.append([[2]])
    T.append([[6]])
    
    T = sorted(T, key=functools.cmp_to_key(lambda x,y: compare(x,y)))

    index = 1
    for elem in T:
        if elem == [[2]]:
            start = index
        elif elem == [[6]]:
            end = index
        index += 1

    s2 = start * end
    
    print("Part 1 Solution: " + str(s1))
    print("Part 2 Solution: " + str(s2))
    


if __name__ == "__main__":
    print("hello!")
    
    solutions()
```

## Quickstart 🚀
```
git clone https://github.com/Gidntsquia/AdventOfCode
```
## Code Structure 📁
The code is broken up as follows:

- [📁](Day_13)`Day_*`: Solutions for each day of advent of code. Click to be taken to today's solution
    - [📋](Day_13/input.txt)`input.txt`: My puzzle input for today (Everyone's is different!)
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
