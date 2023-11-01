test_num = int(input())

words1 = []
words2 = []

for i in range(0, test_num):
    case1, case2 = input().split()
    words1.append(case1)
    words2.append(case2)
    
    
for i in range(0, test_num):
    if sorted(words1[i]) == sorted(words2[i]):
        print('{} & {} are anagrams.'.format(words1[i],words2[i]))
    else:
        print('{} & {} are NOT anagrams.'.format(words1[i],words2[i]))
        