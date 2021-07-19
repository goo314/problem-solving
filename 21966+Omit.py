N = int(input())
S = input()

if N <= 25:
    print(S)

else:
    partOfS = S[11:-11]
    possible = [-1, len(partOfS)-1]

    if partOfS.find('.') in possible:
        print(S[:11] + '...' + S[-11:])

    else:
        print(S[:9] + '......' + S[-10:])
