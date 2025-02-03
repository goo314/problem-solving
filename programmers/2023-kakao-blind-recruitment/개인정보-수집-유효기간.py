"""개인정보 수집 유효기간

Algorithm: 
    Implementation
Level :
    Level 1
Status:
    Pass
Tag:
    CJ올리브네트웍스
"""

def solution(today, terms, privacies):
    answer = []
    
    this_year, this_month, this_date = map(int, today.split('.'))
    
    periods = [0] * 26
    for term in terms:
        type, period = term.split()
        period = int(period)
        periods[ord(type)-ord('A')] = period
    
    for i in range(len(privacies)):
        privacy = privacies[i]
        full_date, type = privacy.split()
        year, month, date = map(int, full_date.split('.'))
        
        period = periods[ord(type)-ord('A')]
        # 오답노트 : 12월은 0월이 아니에요
        year += (month+period-1) // 12
        month = (month+period-1) % 12 + 1
        
        if year == this_year and month == this_month and date <= this_date:
            answer.append(i+1)
        elif year == this_year and month < this_month:
            answer.append(i+1)
        elif year < this_year:
            answer.append(i+1)
    
    return answer