import heapq

# Define the possible movements (up, down, left, right)
movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def calculate_heuristic(cell, goal):
    # Manhattan distance heuristic
    return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])

def calculate_f_score(cell, goal, cost):
    # f-score = cost + heuristic
    return cost + calculate_heuristic(cell, goal)

def generate_neighbors(cell, maze):
    # Generate neighboring cells
    neighbors = []
    for movement in movements:
        x, y = cell[0] + movement[0], cell[1] + movement[1]
        if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
            neighbors.append((x, y))
    return neighbors
def reconstruct_path(came_from, current):
    # Reconstruct the path from start to goal
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.insert(0, current)
    return path

def a_star(maze, start, goal):
    # Initialize open and closed lists
    open_list = []
    closed_list = set()
    came_from = {}

    # Initialize cost and f-score for start cell
    cost = 0
    f_score = calculate_f_score(start, goal, cost)

    # Enqueue start cell
    heapq.heappush(open_list, (f_score, start))

    while open_list:
        # Dequeue cell with lowest f-score
        f_score, current = heapq.heappop(open_list)

        # Check if goal is reached
        if current == goal:
            return reconstruct_path(came_from, current)
        
        # Mark cell as visited
        closed_list.add(current)

        # Generate neighbors
        for neighbor in generate_neighbors(current, maze):
            # Calculate cost and f-score for neighbor
            new_cost = cost + 1
            new_f_score = calculate_f_score(neighbor, goal, new_cost)

            # Check if neighbor is not visited or has better f-score
            if neighbor not in closed_list or new_f_score < calculate_f_score(neighbor, goal, cost):
                came_from[neighbor] = current
                heapq.heappush(open_list, (new_f_score, neighbor))
                cost = new_cost

    # No path found
    return None


# Example usage
maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
goal = (4, 4)

path = a_star(maze, start, goal)
if path:
    print("Path found:", path)
else:
    print("No path found")


