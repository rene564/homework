X, Y = map(int, input().split())
result = int(X % Y == 0 or Y % X == 0)
print(result)
