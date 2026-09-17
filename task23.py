a = int(input())
h = a // 3600
min = (a % 3600) // 60
seconds = a % 60
print(f"{h} часов {min} минут {seconds} секунд")

