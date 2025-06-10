package DAY07.P11266;

import java.util.ArrayList;

public class CutPoint {
    static int[] visited;
    static int visitOrder;
    static ArrayList<ArrayList<Integer>> adjList;
    static int[] isCutPoint;
    static int cutPointCnt;
    public static int cutPointSearch(int curNode, int root) {
        //루트노드일때 자식노드가 몇개인지 파악하기 위함
        int childNodeCnt = 0;

        //방문순서
        visited[curNode] = visitOrder++;

        //방문을 한 점의 인접한 Min order
        //초기화는 자기자신의 순서
        int minOrder = visited[curNode];

        //current Node랑 인접한 인접리스트 탐색진행
        for(int i=0;i<adjList.get(curNode).size();i++) {

            //Destination Node(B)
            int destNode = adjList.get(curNode).get(i);

            //만일 방문을 한곳이다
            if(visited[destNode] != 0) {
                minOrder = Math.min(minOrder, visited[destNode]);
                continue;
            }

            //자식Order는 DFS를 한번 더 돌린다.
            int childOrder = cutPointSearch(destNode, 1);

            //루트노드가 아닌 경우에서
            //자기 자신의 order와
            //자기 자신과 인접한 정점들의 order중 가장 작은 order
            if(root == 1 && childOrder >= visited[curNode]) {
                if(isCutPoint[curNode] == 0) cutPointCnt++;
                isCutPoint[curNode] = 1;
            }

            minOrder = Math.min(minOrder, childOrder);
            childNodeCnt++;
        }

        if(root == 0 && childNodeCnt > 1) {
            if(isCutPoint[curNode] == 0) cutPointCnt++;
            isCutPoint[curNode] = 1;
        }

        return minOrder;
    }
}
