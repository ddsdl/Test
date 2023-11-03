
# def minimumRecolors(blocks: str, k: int) -> int:
#     count = 0
#     lst = []
#     for i in range(k):
#         if (blocks[i] == "W"):
#             count += 1
#             lst.append(i)
#     min = count
#     for i in range(k, len(blocks)):
#         if (blocks[i] == "W"):
#             if (blocks[i-k] == "B"):
#                 count += 1
#         if (blocks[i] == "B" and blocks[i-k] == "W"):
#             count -= 1
#         min = min(count, min)

#     return min

def minimumRecolors(blocks: str, k: int) -> int:
    count = 0
    min_count = float('inf')
    for i in range(len(blocks)):
        if blocks[i] == "W":
            count += 1
        if i >= k:
            if blocks[i - k] == "W":
                count -= 1
        if i >= k - 1:
            min_count = min(min_count, count)

    return min_count
