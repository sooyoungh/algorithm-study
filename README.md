# algorithm-study


### 배열 복사하기
- 깊은 복사
```py
 import copy
 result = copy.deepcopy(data)
```

- 얕은 복사 -> 원래 배열도 값이 변경
```py
result = data
# 혹은
result = data.copy()
# 혹은
result = list(data)
```

- 리스트 슬라이싱 [:]

```py
# 1차원에서는 깊은 복사, 2차원에서는 얕은 복사
result = data[:]

# 2차원에서 깊은 복사 원하면
result = [item[:] for item in data]

```



[배열 복사하기 - 깊은 복사, 얕은 복사](https://blockdmask.tistory.com/576)
