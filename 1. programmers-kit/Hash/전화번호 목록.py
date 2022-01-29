def solution(phone_book):
    # 12 123 => 120 123으로 보고 정렬, 비교할떄는 바로 다음 거랑 1번만 비교해보면 OK
    phone_book.sort()
    
    # 한 배열에서 앞뒤로 비교할 때는 범위를 (전체 배열길이-1)
    for i in range(len(phone_book)-1):
        pre_len = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][0:pre_len]:
            print(phone_book[i])
            return False
        else:
            continue
    
    return True
