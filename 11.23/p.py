while True:
    n=int(input())
    m=int(input())
    result = m//n + 1
    print('ехали ли весь последний день:', result-(n - m%n)//n)
