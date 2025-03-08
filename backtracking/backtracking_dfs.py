# ans = []
# def dfs(start_index, path, [...additional states]):
#     if is_leaf(start_index):
#         ans.append(path[:]) # add a copy of the path to the result
#         return
#     for edge in get_edges(start_index, [...additional states]):
#         # prune if needed
#         if not is_valid(edge):
#             continue
#         path.add(edge)
#         if additional states:
#             update(...additional states)
#         dfs(start_index + len(edge), path, [...additional states])
#         # revert(...additional states) if necessary e.g. permutations
#         path.pop()




# def dfs(start_index, [...additional states]):
#     if is_leaf(start_index):
#         return 1
#     ans = initial_value
#     for edge in get_edges(start_index, [...additional states]):
#         if additional states: 
#             update([...additional states])
#         ans = aggregate(ans, dfs(start_index + len(edge), [...additional states]))
#         if additional states: 
#             revert([...additional states])
#     return ans
