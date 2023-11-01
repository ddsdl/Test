import time

number = int(input())


def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)


start = time.time()
factorial(number)
end = time.time()

print("{0:0.20} sec.".format(end - start))
