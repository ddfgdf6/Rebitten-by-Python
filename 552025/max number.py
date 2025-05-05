def gela(lst):
    return max(lst)


print(gela([-1,-4,-8]))

# def find_max(lst):
#     if not lst:
#         return None  # or raise an error if preferred
#     max_num = lst[0]
#     for num in lst:
#         if num > max_num:
#             max_num = num
#     return max_num