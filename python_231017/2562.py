a = []   					
for i in range(9):
    a.append(int(input()))	

result = a

for i in range(8):	
    if a[i] > a[i+1]:
        a[i+1] = a[i]

print(a[-1])				
print(result.index(a[-1])+1)