# Advent Of Code 2022 🎄
My code for December 2022's [Advent of Code](https://adventofcode.com) puzzles. All my solutions are in Python 3.10.1.

## Today's Solution! (Day 10) 🤗...[🏃](https://replit.com/@Gidntsquia/TodaysAoCSolution-Jaxon#main.py)
```
import re
# Written by Jaxon Lee (GidntSquia)
# Advent of Code Day 11
# 12/11/2022
#
# Feel free to take whatever you'd like!
  
class Monkey:
    
      def __init__(self, items, operation, test, true_target, false_target):
        self.items = items
        self.operation = operation#lambda num: num * 10
        self.divisor = test # lambda num:
        self.true_target = true_target
        self.false_target = false_target
        self.num_inspections = 0
        
# 
# This gives the answer to part 1.
def part1():
    
    all_monkeys = []
    solution = 0
    X = [l.strip() for l in open('Day_11/input.txt')]
    Q = '\n'.join(X)
    Q = Q.split("\n\n")
    
    i = 0
    for lines in Q:
        monkey_data = lines.split('\n')
        
        items = list(map(int, re.findall(r'\d+', monkey_data[1])))
        """
        match i:
            case 0:
                operation = lambda x: x * 19
            case 1:
                operation = lambda x: x + 6
            case 2:
                operation = lambda x: x * x
            case 3:
                operation = lambda x: x + 3
        """
        match i:
            case 0:
                operation = lambda x: x * 17
            case 1:
                operation = lambda x: x + 2
            case 2:
                operation = lambda x: x + 1
            case 3:
                operation = lambda x: x + 7
            case 4:
                operation = lambda x: x * x
            case 5:
                operation = lambda x: x + 8
            case 6:
                operation = lambda x: x * 2
            case 7:
                operation = lambda x: x + 6
        i += 1
        divisor = int(re.search(r'\d+', monkey_data[3]).group())
        
        #test = lambda x: x % divisor == 0
        #print(test(2080))
        true_target = int(re.search(r'\d+', monkey_data[4]).group())
        
        false_target = int(re.search(r'\d+', monkey_data[5]).group())

        
        all_monkeys.append( Monkey(items, operation, divisor, true_target, false_target))
        #print(items, operation, test, true_target, false_target )
    rounds = 20
    for i in range(0,rounds):
        for monkey in all_monkeys:
            for i in range(len(monkey.items)):
                monkey.num_inspections += 1
                item = monkey.items[i]
                monkey.items[i] = monkey.operation(item)
                monkey.items[i] = monkey.items[i] // 3
                
                #print(item, monkey.items[i], monkey.divisor,  monkey.items[i] % monkey.divisor == 0, monkey.true_target, monkey.false_target)
                if monkey.items[i] % monkey.divisor == 0:
                    all_monkeys[monkey.true_target].items.append(monkey.items[i])
                else:
                    all_monkeys[monkey.false_target].items.append(monkey.items[i])
            monkey.items = []
    all_inspections = []
    for monkey in all_monkeys:
        all_inspections.append(monkey.num_inspections)
        #print(monkey.items)
    all_inspections.sort()
    solution = all_inspections[-2] * all_inspections[-1]
    
    print("Part 1 Solution: " + str(solution))

# 
# This gives the answer to part 2.
def part2():
    solution = 0
    X = [l.strip() for l in open('Day_11/input.txt')]
     
    all_monkeys = []
    solution = 0
    X = [l.strip() for l in open('Day_11/input.txt')]
    Q = '\n'.join(X)
    Q = Q.split("\n\n")
    
    i = 0
    for lines in Q:
        monkey_data = lines.split('\n')
        
        items = list(map(int, re.findall(r'\d+', monkey_data[1])))
        """
        match i:
            case 0:
                operation = lambda x: x * 19
            case 1:
                operation = lambda x: x + 6
            case 2:
                operation = lambda x: x * x
            case 3:
                operation = lambda x: x + 3
        """
        match i:
            case 0:
                operation = lambda x: x * 17
            case 1:
                operation = lambda x: x + 2
            case 2:
                operation = lambda x: x + 1
            case 3:
                operation = lambda x: x + 7
            case 4:
                operation = lambda x: x * x
            case 5:
                operation = lambda x: x + 8
            case 6:
                operation = lambda x: x * 2
            case 7:
                operation = lambda x: x + 6
        i += 1
        divisor = int(re.search(r'\d+', monkey_data[3]).group())
        
        #test = lambda x: x % divisor == 0
        #print(test(2080))
        true_target = int(re.search(r'\d+', monkey_data[4]).group())
        
        false_target = int(re.search(r'\d+', monkey_data[5]).group())

        
        all_monkeys.append( Monkey(items, operation, divisor, true_target, false_target))
        #print(items, operation, test, true_target, false_target )
    total_mod = 1
    for monkey in all_monkeys:
        total_mod *= monkey.divisor 
    rounds = 10000
    for i in range(0,rounds):
        for monkey in all_monkeys:
            for i in range(len(monkey.items)):
                monkey.num_inspections += 1
                item = monkey.items[i]
                monkey.items[i] = monkey.operation(item)
                monkey.items[i] = monkey.items[i]
                monkey.items[i] = monkey.items[i] % total_mod
                
                #print(item, monkey.items[i], monkey.divisor,  monkey.items[i] % monkey.divisor == 0, monkey.true_target, monkey.false_target)
                if monkey.items[i] % monkey.divisor == 0:
                    all_monkeys[monkey.true_target].items.append(monkey.items[i])
                else:
                    all_monkeys[monkey.false_target].items.append(monkey.items[i])
            monkey.items = []
    all_inspections = []
    for monkey in all_monkeys:
        all_inspections.append(monkey.num_inspections)
        #print(monkey.items)
    all_inspections.sort()
    solution = all_inspections[-2] * all_inspections[-1]

    
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

- [📁](Day_10)`Day_*`: Solutions for each day of advent of code. Click to be taken to today's solution
    - [📋](Day_10/input.txt)`input.txt`: My puzzle input for today (Everyone's is different!)
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
