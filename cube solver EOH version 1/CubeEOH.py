import heapq
import time

class Cube:
    def __init__(self, state):
        self.state = state

    def is_solved(self):
        # Check if the cube is solved
        # Here, you would compare the current state of the cube with the solved state
        # and return True if they are the same, indicating that the cube is solved.
        # Otherwise, return False.

        solved_state = "RRRRRRRRRGGGGGGGGGWWWWWWWWWOOOOOOOOOBBBBBBBBBYYYYYYYYY"
        return self.state == solved_state

    def get_neighbors(self):
        # Generate all possible next states from the current state
        neighbors = []
      
        return neighbors


    def get_edges(self):
        #This condition is necessary to handle scenarios where the cube state may be incomplete or not properly formatted,
        #ensuring that the program does not encounter index out-of-range 
        if len(self.state) >= 19:
            edges = [
                #access string elements using indexing
                self.state[9], self.state[10], self.state[11],
                self.state[18], '', self.state[12],
                self.state[17], self.state[16], self.state[15],
            ]
            return edges
        else:
            return []

    def get_edge_orientation_heuristic(self):
        # Calculate the edge-orientation heuristic value for the current state
        edges = self.get_edges()
        orientations = [edge.get_orientation() for edge in edges]
        # A solved cube has all edges oriented the same way (0), so count how many edges need to be rotated
        # orientation != 0 filters out correctly oriented edges and only returns mis-oriented edge values
        return sum([orientation for orientation in orientations if orientation != 0])

    #object equality and hashability are important when using comparing and storing CUbe class in sets
    
    #overrides = to support comparison b/w cubes
    def __eq__(self, other):
        return self.state == other.state
    
    #hashes strings of cube states
    def __hash__(self):
        return hash(str(self.state))


def a_star_solver(cube):
    open_set = [(0, cube)]  # priority queue (store f-score,cube)
    closed_set = set()
    move_count = 0  # Number of moves taken to solve the cube
    solution_moves = []
    start_time = time.time()  # Start time for measuring the solving time

    while open_set:
        _, current = heapq.heappop(open_set)  # pop the cube with the lowest f-score
        if current.is_solved():
            end_time = time.time()  # End time for measuring the solving time
            solving_time = end_time - start_time  # Calculate the solving time
            return True, move_count, solution_moves, solving_time

        closed_set.add(current)

        for neighbor_state in current.get_neighbors():
            neighbor = Cube(neighbor_state)

            if neighbor in closed_set:
                continue

            # Calculate g-score and h-score
            g_score = current.get_g_score() + 1
            h_score = neighbor.get_edge_orientation_heuristic()
            f_score = g_score + h_score

            for i, (_, neighbor_in_open_set) in enumerate(open_set):
                if neighbor == neighbor_in_open_set and f_score >= neighbor_in_open_set.get_f_score():
                    break
            else:
                move_count += 1  # Increment the move count
                heapq.heappush(open_set, (f_score, neighbor))

    end_time = time.time()  # End time for measuring the solving time
    solving_time = end_time - start_time  # Calculate the solving time
    return False, move_count, solution_moves, solving_time



def retrieve_edges_from_string(cube_string):
    edges = [
        cube_string[9], cube_string[10], cube_string[11],
        cube_string[18], '', cube_string[12],
        cube_string[17], cube_string[16], cube_string[15],
    ]
    return edges
