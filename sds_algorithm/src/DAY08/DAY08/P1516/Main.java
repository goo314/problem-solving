package DAY08.P1516;

import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[] initCost;
    static int[] cost;
    static int[] in;
    static ArrayList<ArrayList<Integer>> adjList = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());

        in = new int[N+1];
        initCost = new int[N+1];
        cost = new int[N+1];
        for (int i = 0; i <= N; i++) {
            adjList.add(new ArrayList<>());
        }

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            initCost[i] = Integer.parseInt(st.nextToken());

            while (true) {
                int prev = Integer.parseInt(st.nextToken());
                if (prev == -1) break;

                adjList.get(prev).add(i);
                in[i]++;
            }
        }

        // topological sort
        Queue<Integer> q = new LinkedList<>();
        for (int i = 1; i <= N; i++) {
            if (in[i] == 0) q.add(i);
        }

        while (!q.isEmpty()) {
            int current = q.poll();
            cost[current] += initCost[current];
            for(int next: adjList.get(current)) {
                cost[next] = Math.max(cost[next], cost[current]);
                if (--in[next] == 0) {
                    q.add(next);
                }
            }
        }

        for (int i=1; i<=N; i++) {
            bw.write(cost[i]+"\n");
        }
        bw.flush();

    }

}
