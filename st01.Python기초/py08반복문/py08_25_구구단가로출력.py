for 단 in range(2, 20, 1):
    for 곱 in range(1, 10, 1):
        str = "%2s * %s = %3s" % (단, 곱, 단*곱)
        if 곱 == 9:
            print(str, end=".")
        else:
            print(str, end=",")
