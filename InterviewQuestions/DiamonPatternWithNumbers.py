def pattern(n):
    n = 1
    while n <= 8:
        if n <= 4:
            print(f"{n}*" * n)
        else:
            print(f"{9-n}*" * (9-n))
        n += 1

pattern("*")