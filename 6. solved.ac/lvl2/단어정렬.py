n = int(input())

words = set()
for _ in range(n):
    words.add(input())

words = list(words)

# 방법1) 정렬 조건 2번째부터 정렬해줌
words.sort()
words.sort(key=lambda x: len(x))

# 방법2) 람다식으로 한번에
# 정렬 조건 2번째부터 정렬해줌
words.sort(key=lambda x: (len(x), x))

for i in words:
    print(i)
