import heapq

def A_star(grid, start, destination):
    def heuristic(cell):
        return abs(cell[0] - destination[0]) + abs(cell[1] - destination[1])
    
    def is_valid_cell(cell):
        x, y = cell
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 1
    
    def neighbors(cell):
        x, y = cell
        possible_neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        return [neighbor for neighbor in possible_neighbors if is_valid_cell(neighbor)]
    
    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    
    while open_set:
        current_g, current = heapq.heappop(open_set)
        
        if current == destination:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]
        
        for neighbor in neighbors(current):
            tentative_g = g_score[current] + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor)
                heapq.heappush(open_set, (f_score, neighbor))
                came_from[neighbor] = current
                
    return None  # No path found

# Inputs:
grid = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
]

start = (0, 0)
destination = (3, 3)

path = A_star(grid, start, destination)
if path:
    print("Optimum path:", path)
    print("Total distance traveled:", len(path) - 1)
else:
    print("No valid path found.")
""" Optimum path: [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3)]
    Total distance traveled: 6"""

grid_2 = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

start_2 = (0, 0)
destination_2 = (4, 4)

path_2 = A_star(grid_2, start_2, destination_2)
if path_2:
    print("Optimum path for grid_2:", path_2)
    print("Total distance traveled:", len(path_2) - 1)
else:
    print("No valid path found for grid_2.")
""" Optimum path for grid_2: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
    Total distance traveled: 8"""

"""The provided code uses the A* algorithm to find the shortest path between a 
    start point and a destination point on a grid, avoiding obstacles. It prioritizes 
    exploring cells based on their actual distance from the start and an estimated 
    distance to the destination (heuristic). The algorithm returns the optimum path 
    from the start to the destination or None if no valid path is found."""

"""Q1b.Think of the plane as a grid (with m x m cells) where a factory or warehouse
will be a cell. The truck can again travel from one cell to another adjacent cell
vertically or horizontally except it can’t travel outside the grid boundary.
Additionally certain cells represent no trespass area where the truck can’t
pass through. Find the optimum solution in this setup again minimising total
distance travelled by the truck."""