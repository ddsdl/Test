# input_val = input("공백을 기준으로 숫자를 입력하세요. (예: 1 2 3)\n")
# inputs = input_val.split()

# nums = []
# for i in inputs:
#     nums.append(int(i))
    
# inputs = input("공백을 기준으로 숫자를 입력하세요. (예: 1 2 3)\n").split()

nums = [int(i) for i in input("공백을 기준으로 숫자를 입력하세요. (예: 1 2 3)\n").split()]
# nums = list(map(int ,input().split()))
print(nums)