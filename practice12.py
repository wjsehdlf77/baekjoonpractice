# 2914번


song_num, avg_value = map(int, input().split())

avg_value -= 1

melody = (song_num * avg_value) + 1

print(melody)
