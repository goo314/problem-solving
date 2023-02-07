package DAY06.P2252;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N, M;
    static ArrayList<ArrayList<Integer>> edges; // edges[v1] = { v2, v3 }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        edges = new ArrayList<>();
        for (int i = 0; i < N+1; i++) {
            edges.add(new ArrayList<>());
        }
        int[] indegree = new int[N+1];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            edges.get(a).add(b);
            indegree[b]++;
        }

        Queue<Integer> q = new LinkedList<>();
        for (int i = 1; i <= N; i++) {
            if (indegree[i] == 0) {
                q.add(i);
            }
        }

        while (q.isEmpty() == false) {
            int current = q.poll();
            System.out.print(current+" ");
            for (int i = 0; i < edges.get(current).size(); i++) {
                int next = edges.get(current).get(i);
                if (--indegree[next] == 0) {
                    q.add(next);
                }
            }
        }

    }


}
