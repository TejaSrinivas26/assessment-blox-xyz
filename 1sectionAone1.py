def calculate_manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def find_optimal_warehouse_location(factories):
    min_total_distance = float('inf')
    optimal_location = None

    for x in range(min(x for x, y in factories), max(x for x, y in factories) + 1):
        for y in range(min(y for x, y in factories), max(y for x, y in factories) + 1):
            total_distance = sum(calculate_manhattan_distance(x, y, fx, fy) for fx, fy in factories)
            if total_distance < min_total_distance:
                min_total_distance = total_distance
                optimal_location = (x, y)

    return optimal_location

# inputs:
factories = [(15, 3), (4, 2), (7, 5)]
optimal_warehouse_location = find_optimal_warehouse_location(factories)
print("Optimal Warehouse Location:", optimal_warehouse_location) #(7, 3)

factories_2 = [(1, 1), (2, 2), (3, 3), (4, 4)]
optimal_warehouse_location_2 = find_optimal_warehouse_location(factories_2)
print("Optimal Warehouse Location:", optimal_warehouse_location_2) #(2, 2)

factories_3 = [(0, 0), (3, 1), (2, 4), (5, 3)]
optimal_warehouse_location_3 = find_optimal_warehouse_location(factories_3)
print("Optimal Warehouse Location:", optimal_warehouse_location_3) #(2, 1)


"""The provided code finds the optimal location for a warehouse based on the Manhattan distance to a list of factory locations. Here's a shorter and simpler explanation:

    The calculate_manhattan_distance function computes the Manhattan distance between two points given their (x, y) coordinates.

    The find_optimal_warehouse_location function takes a list of factory locations and iterates through possible warehouse locations to find the one that minimizes the total Manhattan distance to all factories.

    It initializes min_total_distance to positive infinity and optimal_location to None.

    The function iterates through all possible warehouse locations by considering the minimum and maximum x and y coordinates found in the factory list.

    For each candidate warehouse location, it calculates the total distance from that location to all factories by summing up the Manhattan distances between each factory and the warehouse.

    If the total distance for the current candidate location is less than the current minimum distance (min_total_distance), it updates min_total_distance to the new minimum and sets optimal_location to the current candidate location.

    After considering all possible warehouse locations, the function returns the coordinates of the optimal warehouse location that minimizes the total distance to all factories.

    The example usage demonstrates how to find the optimal warehouse location for a list of factory locations [(15, 3), (4, 2), (7, 5)] and prints the result."""


"""You are given cartesian coordinates of n factories in a plane producing some items
    that need to be stored in a warehouse.
    a. A transport truck begins its journey from the warehouse and it can travel
    along any horizontal or vertical line. After collecting items from a factory, the
    truck needs to return to the warehouse and deposit the items before visiting
    another factory. Find the strategic location of the warehouse such that the
    total distance truck needs to travel in order to collect items from all the
    factories is minimised."""