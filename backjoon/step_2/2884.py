H, M = map(int, input().split(" "))
if M < 45:
    M = M + 15
    H = H - 1
    if H < 0:
        H = 23

    print(H, M)

else:
    M = M - 45

    print(H, M)
