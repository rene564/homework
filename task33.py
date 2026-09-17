N=int(input())
C=int(input())
K=int(input())
a = N * C
page = (K - 1) // a + 1
pos_in_page = (K - 1) % a
column = pos_in_page // N + 1
row = pos_in_page % N + 1

print(f"страница {page} столбец {column} строка {row}")

