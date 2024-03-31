package DAY08.P3176;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N, K;
    static int[] depth;
    static int[][] parent;
    static Pair[] dp;
    static ArrayList<ArrayList<Pair>> adjList = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        for (int i = 0; i <= N; i++) {
            adjList.add(new ArrayList<>());
        }

        dp = new Pair[N+1];
        depth = new int[N+1];
        parent = new int[18][N+1];

        int a, b, c;
        for (int i = 0; i < N-1; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());
            adjList.get(a).add(new Pair(b, c));
            adjList.get(b).add(new Pair(a, c));
        }

        depth[1] = 1;
        findBridge(1);

        // TODO: fill parent

        K = Integer.parseInt(br.readLine());

        int d, e, lca;
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            d = Integer.parseInt(st.nextToken());
            e = Integer.parseInt(st.nextToken());
            lca = findLCA(d, e);
            bw.write(dp[lca].first+" "+dp[lca].second);
        }

    }

    static void findBridge(int current) {
        int min = 1000001, max = 0;

        for(Pair next: adjList.get(current)) {
            int nv = next.first;
            int nw = next.second;

            if (depth[nv] == 0) {
                depth[nv] = depth[current]+1;
                parent[0][nv] = current;
                findBridge(nv);
                min = Math.min(min, Math.min(dp[nv].first, nw));
                max = Math.max(max, Math.max(dp[nv].second, nw));
            }

        }

        dp[current] = new Pair(min, max);
    }

    static int findLCA(int a, int b) {
        return 1;
    }

}

class Pair {
    int first;
    int second;

    public Pair(int first, int second) {
        this.first = first;
        this.second = second;
    }

    @Override
    public String toString() {
        return "Pair{" +
                "first=" + first +
                ", second=" + second +
                '}';
    }
}