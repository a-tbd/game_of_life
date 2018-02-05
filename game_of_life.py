'''
Simple game of life with three letters instead of two
Cycles through the three letters
'''
import random
import curses

lifeforms = ['W', 'A', 'Y']
gameboard = [[0 if random.random() < .8 else 1 for i in range(0,10)] for j in range(0,10)]



def number_neighbors(gameboard):
    neighbor_count = [[0 for i in range(0,10)] for j in range(0,10)]

    for row in range(len(gameboard)):
        for col in range(len(gameboard[row])):
            num_alive = 0
            neighbors = get_neighbors(row, col)
            for neighbor in neighbors:
                num_alive += neighbor

            neighbor_count[row][col] = num_alive
    return neighbor_count

def update(gameboard, neighbor_count):
    for row in range(len(neighbor_count)):
        for col in range(len(neighbor_count[row])):
            if neighbor_count[row][col] <= 1:
                gameboard[row][col] = 0
            elif neighbor_count[row][col] >= 4:
                gameboard[row][col] = 0
            elif neighbor_count[row][col] == 3:
                gameboard[row][col] = 1

    return gameboard

def get_neighbors(row, col):
    neighbors = []
    for dr in [-1,0,1]:
        for dc in [-1,0,1]:
            if row + dr >= 0 and row + dr < 10 and col + dc >= 0 and col + dc < 10 and not (dc == 0 and dr == 0):
                neighbors.append(gameboard[row+dr][col+dc])
    return neighbors


def main(gameboard):
    for i in range(10):
        neighbor_count = number_neighbors(gameboard)
        gameboard = update(gameboard, neighbor_count)
        for line in gameboard:
        	print(line)
        print()

if __name__ == '__main__':
    main(gameboard)

