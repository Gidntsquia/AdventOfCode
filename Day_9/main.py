import re
import math
import sys
# Written by Jaxon Lee (GidntSquia)
# Advent of Code Day 9
# 12/9/2022
#
# Feel free to take whatever you'd like!


def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)  

def move(position, change):
    return tuple(sum(x) for x in zip(position, change))

# This gives the number of squares that the "tail" visited.
# This gives the answer to part 1.
def part1():
    solution = 0
    X = [l.strip() for l in open('Day_9/input.txt')]
    h_pos = (0, 0)
    t_pos = (0, 0)
    moves = {
        'R': (0, 1),
        'L': (0, -1),
        'U': (1, 0),
        'D': (-1, 0)
    }
    
    visited = set([])
    
    visited.add(t_pos)
    # Four moves
    for commands in X:
        words = commands.split()
        direction = words[0]
        change = moves[direction]
        for i in range(0, int(words[1])):
            h_pos = move(h_pos, change)
            (hx, hy) = h_pos
            (tx, ty) = t_pos
            distance = (hx - tx, hy - ty)
            match distance:
                case (2, 0):
                    t_pos = move(t_pos, moves['U'])
                case (-2, 0):
                    t_pos = move(t_pos, moves['D'])
                case (0, 2):
                    t_pos = move(t_pos, moves['R'])
                case (0, -2):
                    t_pos = move(t_pos, moves['L'])
                case (1, 2) | (2, 1):
                    t_pos = move(t_pos, moves['U'])
                    t_pos = move(t_pos, moves['R'])
                case (-1, 2) | (-2, 1):
                    t_pos = move(t_pos, moves['D'])
                    t_pos = move(t_pos, moves['R'])
                case (1, -2) | (2, -1):
                    t_pos = move(t_pos, moves['U'])
                    t_pos = move(t_pos, moves['L'])
                case (-1, -2) | (-2, -1):
                    t_pos = move(t_pos, moves['D'])
                    t_pos = move(t_pos, moves['L'])
                case _:
                    pass 
            visited.add(t_pos)
        
            
    solution = len(visited)
   
    
    print("Part 1 Solution: " + str(solution))

# This gives the number of squares that the 9th (last) tail finished.
# This gives the answer to part 2.
def part2():
    solution = 0
    X = [l.strip() for l in open('Day_9/input.txt')]
    rope_positions = [(0,0) for i in range(0, 10)]
    print(rope_positions)
    moves = {
        'R': (0, 1),
        'L': (0, -1),
        'U': (1, 0),
        'D': (-1, 0)
    }
    
    visited = set([])
    
    visited.add((0,0))
    # Four moves
    for commands in X:
        words = commands.split()
        direction = words[0]
        change = moves[direction]
        for i in range(0, int(words[1])):
            rope_positions[0] = move(rope_positions[0], change)
            (hx, hy) = rope_positions[0]
            
            for i in range(1, 10):
                
                (tx, ty) = rope_positions[i]
                distance = (hx - tx, hy - ty)
                match distance:
                    case (2, 0):
                        rope_positions[i] = move(rope_positions[i], moves['U'])
                    case (-2, 0):
                        rope_positions[i] = move(rope_positions[i], moves['D'])
                    case (0, 2):
                        rope_positions[i] = move(rope_positions[i], moves['R'])
                    case (0, -2):
                        rope_positions[i] = move(rope_positions[i], moves['L'])
                    case (1, 2) | (2, 1) | (2, 2):
                        rope_positions[i] = move(rope_positions[i], moves['U'])
                        rope_positions[i] = move(rope_positions[i], moves['R'])
                    case (-1, 2) | (-2, 1) | (-2, 2):
                        rope_positions[i] = move(rope_positions[i], moves['D'])
                        rope_positions[i] = move(rope_positions[i], moves['R'])
                    case (1, -2) | (2, -1) | (2, -2):
                        rope_positions[i] = move(rope_positions[i], moves['U'])
                        rope_positions[i] = move(rope_positions[i], moves['L'])
                    case (-1, -2) | (-2, -1) | (-2, -2):
                        rope_positions[i] = move(rope_positions[i], moves['D'])
                        rope_positions[i] = move(rope_positions[i], moves['L'])
                    case _:
                        pass 
                (hx, hy) = rope_positions[i]
            
            visited.add(rope_positions[9])
        
            
    solution = len(visited)

    
    print("Part 2 Solution: " + str(solution))


if __name__ == "__main__":
    print("hello!")
    
    
    part1()
    part2()
    
    