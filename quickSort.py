# def sum(arr):
#     total = 0
#     for x in arr:
#         total += x
#     return total

# print(sum([1, 2, 3, 4]))

# def sum(list):
#     if list == []:
#         return 0
#     return list[0] + sum(list[1:])

# print(sum([2, 4, 6]))

def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])

print(count([1, 8, 4, 56, 5, 12]))