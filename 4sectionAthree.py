def distance(point1, point2):
    # Calculate the Euclidean distance between two points.
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) ** 0.5

def find_unit_distance_pairs(points):
    # Sort points based on x-coordinate.
    points.sort(key=lambda p: p[0])

    n = len(points)
    unit_distance_pairs = []

    # Iterate through each point.
    for i in range(n):
        # Check points with x-coordinate within one unit distance.
        for j in range(i + 1, n):
            if points[j][0] - points[i][0] <= 1:
                # Check if y-coordinates are also within one unit distance.
                if abs(points[j][1] - points[i][1]) <= 1:
                    # Add the pair to the output list.
                    unit_distance_pairs.append((points[i], points[j]))

    return unit_distance_pairs

# Inputs:
points = [(1, 2), (2, 3), (4, 5), (4, 6), (6, 7)]
result = find_unit_distance_pairs(points)
print(result) #[((1, 2), (2, 3)), ((4, 5), (4, 6))]

points = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 2), (3, 3)]
result = find_unit_distance_pairs(points)
print(result) #[((0, 0), (0, 1)), ((0, 0), (1, 0)), ((0, 0), (1, 1)), ((0, 1), (1, 0)), ((0, 1), (1, 1)), ((1, 0), (1, 1)), ((1, 1), (2, 2)), ((2, 2), (3, 3))]

points = [(10, 10), (12, 10), (10, 12), (12, 12), (11, 11)]
result = find_unit_distance_pairs(points) # [((10, 10), (11, 11)), ((10, 12), (11, 11)), ((11, 11), (12, 10)), ((11, 11), (12, 12))]
print(result)



"""The find_unit_distance_pairs method takes a list of 2D points as input and returns 
    a list of pairs of points that are within one unit distance from each other in both the x and y coordinates.

    The method first sorts the input points based on their x-coordinates to ensure efficient 
    processing. Then, it iterates through each point and checks for other points that have 
    x-coordinates within one unit distance. For each such pair of points with close x-coordinates, 
    it further checks if their y-coordinates are also within one unit distance. If both conditions 
    are met, the pair is added to the output list.

    The result is a list of tuples, where each tuple contains two points that are within one 
    unit distance from each other in both the x and y coordinates."""


"""Recall the definition of a convex point set [1] in two dimensions. A half convex point
    set is a special case where the point set is convex consisting of at most two
    monotonic sequences. A monotonic sequence is a set of points such that
    coordinates of the points are increasing/decreasing along both the axes. Note that
    coordinate values might increase along one axis and decrease along another one.
    A unit distance pair is a pair of two points iff the distance between both the points is
    exactly one. Implement the code to compute all the unit distance pairs in a given
    half convex point set. Argue an upper bound on the number of such pairs.
    a. Input: A list of tuples where each tuple indicates a point with both coordinate
    values.
    b. Output: A list of pairs of tuples with unit distance"""