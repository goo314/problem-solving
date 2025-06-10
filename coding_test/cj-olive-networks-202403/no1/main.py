"""
Description:
    좌표: A(ax, ay), B(bx, by)
    지하철: square[4] = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
    지하철을 타면 거리는 0
    A에서 B로 가는 최단 거리를 구하라.
Status:
    주어진 테스트케이스는 다 맞음
My Solution:
    A에서 B까지의 거리와 지하철까지의 A 거리 + 지하철까지의 B 거리 중 최소값
"""

def solution(ax, ay, bx, by, square):
    def take_train(x, y, x0, x1, y0, y1):
        ret = 0
        dx = min(abs(x-x0), abs(x-x1))
        dy = min(abs(y-y0), abs(y-y1))
        # square 밖인지 안인지 구분해서 거리 구함
        return ret

    answer = 1e9
    x0, x1, y0, y1 = square[0][0], square[1][0], square[1][1], square[2], [1]
    answer = abs(ax-bx) + abs(ay-by)
    answer = min(answer, take_train(ax, ay, x0, x1, y0, y1)+take_train(bx, by, x0, x1, y0, y1))

    return answer