/*
Description:
    grid에서 상하좌우로 grid[i][j]만큼 이동할 수 있음.
    근데, 이동할 때 1만큼 적게(=grid[i][j]-1) 이동할 수 있는 기회가 k번 있음.
    테두리에서 시작한다고 했을 때, (r, c)에 도착하는 최소 거리를 구하여라.
Status:
    dfs와 dp 구현하다가 Fail
My Solution:
    dp[n][m]에 (r, c)까지 가는 최소 거리를 저장하고
        여기서 자바 Pair를 못 사용해서 한참 헤멨음.
        dfs recursive로 dp에 저장하면서 순회하는 부분을 구현하다가 계속 stack overflow.
    후에 트리 순회처럼 사용횟수가 k가 되면 멈추는 로직을 생각했는데 구현 못했어...
*/
