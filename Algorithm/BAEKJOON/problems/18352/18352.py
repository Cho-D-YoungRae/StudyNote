if __name__ == '__main__':
    N = list(map(int, list(input())))

    my_status = "LUCKY" if sum(N[:len(N)//2]) == sum(N[len(N)//2:]) \
                                                        else "READY"

    print(my_status)

