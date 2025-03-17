def solution(phone_book):
    answer = True
    
    d = dict()
    
    phone_book.sort(key=lambda x: len(x))
    for phone in phone_book:
        n_p = len(phone)
        for i in range(1, n_p+1):
            if phone[:i] in d:
                answer = False
                break
        d[phone] = 1
    
    
    return answer