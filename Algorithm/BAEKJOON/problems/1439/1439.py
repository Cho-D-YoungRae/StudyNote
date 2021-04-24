

if __name__ == '__main__':
    S = input()

    change_point = 0

    for i in range(1, len(S)):
        if S[i] != S[i-1]:
            change_point += 1

    print((change_point + 1) // 2)

