star = int(input())

# [n=1] 공백 4 / 별 1=(2n-1)   / 공백 4 (star-n)
# [n=2] 공백 3 / 별 3=(2n-1)   / 공백 3 (star-n)
# [n=3] 공백 2 / 별 5=(2n-1)   / 공백 2 (star-n)
# [n=4] 공백 1 / 별 7=(2n-1)   / 공백 1 (star-n)
for n in range(1, star):
    print(f'{" " * (star-n)}{"*" * (2 * n -1) }{" " * (star-n)}')

# [n=5] 공백 0 / 별 9=(2n-1)   / 공백 0 (star-n)
# [n=4] 공백 1 / 별 7=(2n-1)   / 공백 1 (star-n)
# [n=3] 공백 2 / 별 5=(2n-1)   / 공백 2 (star-n)
# [n=2] 공백 3 / 별 3=(2n-1)   / 공백 3 (star-n)
# [n=1] 공백 4 / 별 1=(2n-1)   / 공백 4 (star-n)
for n in range(star, 0, -1): # [5, 4, 3, 2, 1]
    print(f'{" " * (star-n)}{"*" * (2 * n -1) }{" " * (star-n)}')
    


