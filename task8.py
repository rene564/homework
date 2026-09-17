print("Введите плей-лист папы:")
songs = [input() for i in range(5)]
print("Плей-лист мамы:")
for song in reversed(songs):
    print(song)