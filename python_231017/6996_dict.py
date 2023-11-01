test_count = int(input())
words = []
for _ in range(test_count):
    words.append(input().split())

for i in words:
    word1, word2 = i
    
    d_word1 = {}
    for j in word1:
        if j in d_word1:
            d_word1[j] += 1
        else:
            d_word1[j] = 1
    d_word2 = {}
    for j in word2:
        if j in d_word2:
            d_word2[j] += 1
        else:
            d_word2[j] = 1
    if d_word1 == d_word2:
        print(f'{i[0]} & {i[1]} are anagrams')
    else:
        print(f'{i[0]} & {i[1]} are NOT anagrams')
        