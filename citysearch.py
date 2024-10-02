import numpy as np
import random

def nearest_neighbor(dist_matrix, start_city):
    tour = [start_city]
    visited = set([start_city])
    while len(tour) < len(dist_matrix):
        current_city = tour[-1]
        next_city = np.argmin([dist_matrix[current_city, i] if i not in visited else np.inf for i in range(len(dist_matrix))])
        tour.append(next_city)
        visited.add(next_city)
    tour.append(start_city)  # close tour
    return tour

def two_opt(tour, dist_matrix):
    improved = True
    while improved:
        improved = False
        for i in range(len(tour) - 2):
            for j in range(i + 2, len(tour)):
                new_tour = tour[:i] + list(reversed(tour[i:j])) + tour[j:]
                if sum([dist_matrix[new_tour[k], new_tour[k + 1]] for k in range(len(new_tour) - 1)]) < sum([dist_matrix[tour[k], tour[k + 1]] for k in range(len(tour) - 1)]):
                    tour = new_tour
                    improved = True
    return tour

def tsp(dist_matrix):
    start_city = random.randint(0, len(dist_matrix) - 1)
    tour = nearest_neighbor(dist_matrix, start_city)
    tour = two_opt(tour, dist_matrix)
    return tour

# Example usage
dist_matrix = np.array([[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]])
print(tsp(dist_matrix))
