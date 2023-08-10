# Original graph with sublists
graph = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Using nested map functions
dist_map = list(map(lambda i: list(map(lambda j: j, i)), graph))

# Using list comprehension
dist_list_comp = [list(i) for i in graph]

# Testing if the two resulting lists are the same
print(dist_map == dist_list_comp)  # Should print True
print(dist_map)
print(dist_list_comp)

