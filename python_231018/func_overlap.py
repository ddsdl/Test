# def average(*scores):
#     length = len(scores)
#     sum = 0
#     for i in scores:
#         sum += i
#     return sum / length


# print(average(10, 20, 30, 40, 50))

def average(*scores):
    def length():
        return len(scores)

    def sum():
        total = 0
        for i in scores:
            total += i
        return total
    return sum() / length()


print(average(10, 20, 30, 40, 50))
