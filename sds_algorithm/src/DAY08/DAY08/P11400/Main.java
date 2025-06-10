// TODO: 그래프2 > 단절선, order < low
package DAY08.P11400;

import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int V, E;
    static int[] order;
    static boolean[] visited;
    static ArrayList<ArrayList<Integer>> adjList = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());

        order = new int[V+1];
        visited = new boolean[V+1];
        for (int i = 0; i <= V; i++) {
            adjList.add(new ArrayList<>());
        }

        int v1, v2;
        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            v1 = Integer.parseInt(st.nextToken());
            v2 = Integer.parseInt(st.nextToken());
            adjList.get(v1).add(v2);
            adjList.get(v2).add(v1);
        }

    }
    static int findCutPoint() {

        return 0;
    }
}
