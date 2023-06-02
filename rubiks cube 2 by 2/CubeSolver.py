import heapq


class Cube:
    SOLVED_STATE = "RWOGRWOG"

    def __init__(self, state):
        self.state = state

    def is_solved(self):
        return self.state == self.SOLVED_STATE

    def get_neighbors(self):
        neighbors = []

        # Rotate the top face clockwise
        cube_copy = Cube(self.rotate_top_clockwise())
        neighbors.append(cube_copy)

        # Rotate the top face counterclockwise
        cube_copy = Cube(self.rotate_top_counter_clockwise())
        neighbors.append(cube_copy)

        # Rotate the right face clockwise
        cube_copy = Cube(self.rotate_right_clockwise())
        neighbors.append(cube_copy)

        # Rotate the right face counterclockwise
        cube_copy = Cube(self.rotate_right_counter_clockwise())
        neighbors.append(cube_copy)

        return neighbors

    def rotate_top_clockwise(self):
        state = self.state
        new_state = state[0:2] + state[6] + state[3:6] + state[7] + state[11:13] + state[8:11] + state[13:]
        return new_state

    def rotate_top_counter_clockwise(self):
        state = self.state
        new_state = state[0:2] + state[5] + state[2:5] + state[6] + state[10:12] + state[7:10] + state[12:]
        return new_state

    def rotate_right_clockwise(self):
        state = self.state
        new_state = state[0] + state[1:3] + state[6] + state[4:7] + state[11] + state[7:10] + state[3:4] + state[12:]
        return new_state

    def rotate_right_counter_clockwise(self):
        state = self.state
        new_state = state[0] + state[2:4] + state[6] + state[4:7] + state[3] + state[7:10] + state[10:11] + state[12:]
        return new_state

    def get_manhattan_distance(self):
        distance = 0
        for i in range(8):
            if self.state[i] != self.SOLVED_STATE[i]:
                distance += 1
        return distance

    def __lt__(self, other):
        return self.get_manhattan_distance() < other.get_manhattan_distance()

#A* implementation
def A_star_algorithm(cube, target):
    if cube.state == target:
        return []

    queue = [(cube.get_manhattan_distance(), 0, cube)]
    heapq.heapify(queue)
    visited = set()

    while queue:
        _, moves, current_cube = heapq.heappop(queue)
        visited.add(current_cube.state)

        for neighbor in current_cube.get_neighbors():
            if neighbor.state == target:
                return moves + 1

            if neighbor.state not in visited:
                visited.add(neighbor.state)
                heapq.heappush(queue, (neighbor.get_manhattan_distance() + moves + 1, moves + 1, neighbor))

    return -1

'''
def solve_cube(cube):
    moves = get_move_to(cube, cube.SOLVED_STATE)

    if moves == -1:
        print("Unable to solve the cube.")
    else:
        print(f"Solved the cube in {moves} moves.")


if __name__ == "__main__":
    # Test the solver
    test_cube = Cube("RWOGRWOG")
    solve_cube(test_cube)
'''