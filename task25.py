X, Y, N = map(int, input().split())
a = (X * 100 + Y) * N
R = a // 100
K = a % 100
print(f"{R} руб. {K} коп.")
