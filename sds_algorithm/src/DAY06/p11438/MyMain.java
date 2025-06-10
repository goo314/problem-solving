package DAY06.p11438;

import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class MyMain {
    static int N, M;
    static int[][] parent;
    static int[] depth;
    static ArrayList<ArrayList<Integer>> adjList = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());

        for (int i = 0; i <= N; i++) {
            adjList.add(new ArrayList<>());
        }

        int a, b;
        parent = new int[18][N+1];
        for (int i = 0; i < N-1; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            adjList.get(a).add(b);
            adjList.get(b).add(a);
        }

        depth = new int[N+1];
        getDepth(1, 1);

        for (int i = 1; i <= 17; i++) {
            for (int j = 1; j <= N; j++) {
                parent[i][j] = parent[i-1][parent[i-1][j]];
            }
        }

        int node1, node2, answer;
        M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());

            // node1 is deeper than node2
            if(depth[a] > depth[b]) {
                node1 = a; node2 = b;
            } else {
                node1 = b; node2 = a;
            }

            // make depth[node1] == depth[node2]
            for (int j = 17; j>=0 && depth[node1]>depth[node2]; j--) {
                if (depth[node1] - depth[node2] >= (int) Math.pow(2, j)) {
                    node1 = parent[j][node1];
                }
            }

            answer = node1;
            for (int j = 17; j>=0 && node1!=node2; j--) {
                if(parent[j][node1] != parent[j][node2]) {
                    node1 = parent[j][node1];
                    node2 = parent[j][node2];
                }
                answer = parent[j][node1];
            }

            bw.write(answer + "\n");
        }
        bw.flush();
    }

    static void getDepth(int current, int d) {
        depth[current] = d;
        for(int next: adjList.get(current)) {
            if (depth[next] == 0) {
                parent[0][next] = current;
                getDepth(next, d+1);
            }
        }
    }
}
