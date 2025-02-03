"""
Description:
    1 <- n <= 9, 1<=m<=100000
    공격량 : atk
    몬스터의 체력 : monster_hp[n]
    몬스터의 공격량 : monster_atk[n][m]
    최소 데미지를 구하라.
Algorithm:
    DP
Status:
    시간 부족 Fail
My Solution:
    접근 다 했는데 하 아쉽군
    미리 damage 합을 dp로 몬스터별로 구함, 즉 subsum[i][j] : 몬스터 i가 j라운드까지 주는 데미지의 합
    permutation으로 몬스터 죽이는 순서 다 구하고
        몬스터 순서를 돌면서 subsum을 더하면 되는데
        흠, 더 디테일하게 예시로 밑에 들면
    
    atk=10, 
    monster_hp = (30, 10, 15)이고 (편하게 a, b, c)
    monster_atk = [
        [1, 2, 1, 2, 1],
        [2, 1, 3, 6, 2],
        [3, 5, 4, 2, 1]
    ]

    이때,
    subsum = [
        [1, 3, 4, 6, 7],
        [2, 3, 6, 12, 14],
        [3, 8, 12, 14, 15]
    ]

    만약 몬스터를 (15, 10, 30)로 죽였다면
    15는 1번째 round에서 죽음 damage += subsum[c][0] => damage = 3
    10은 2번째 round에서 죽음 damage += subsum[b][1] => damage = 3 + 3 = 6
    30은 4번째 round에서 죽음 damage += subsum[c][4] => damage = 6 + 7 = 13
    이걸 구현해야 하는데 못 했어...

"""

def solution(atk, monster_hp, monster_atk):
    answer = 0
    # 딕셔너리로 monster_hp -> index에 대응하도록 만듬
    # dp를 통해 monster_atk의 subsum을 구함
    # itertools.permutation으로 몬스터를 죽이는 모든 경우의 수를 구함
    # 경우를 다 돌면서 subsum 합이 작은걸 answer로 업데이트 <= 이 부분을 구현 못함...
    return answer