// TODO: find shortest multiple paths and second dijkstra
package DAY08.P5719;

import java.io.*;
import java.util.*;

public class Main {
    static int INF = Integer.MAX_VALUE;
    static int N, M;
    static int S, D;
    static boolean[] visited;
    static int[] dist;
    static ArrayList<ArrayList<Integer>> shortestPath;
    static ArrayList<ArrayList<Pair>> adjList;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        while (true) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            if (N == 0 && M == 0) {
                break;
            }

            st = new StringTokenizer(br.readLine());
            S = Integer.parseInt(st.nextToken());
            D = Integer.parseInt(st.nextToken());

            // initialize
            adjList = new ArrayList<>();
            shortestPath = new ArrayList<>();
            visited = new boolean[N];
            dist = new int[N];
            for (int i = 0; i < N; i++) {
                adjList.add(new ArrayList<>());
                shortestPath.add(new ArrayList<>());
                dist[i] = INF;
            }

            int u, v, p;
            for (int i = 0; i < M; i++) {
                st = new StringTokenizer(br.readLine());
                u = Integer.parseInt(st.nextToken());
                v = Integer.parseInt(st.nextToken());
                p = Integer.parseInt(st.nextToken());

                adjList.get(u).add(new Pair(v, p));
            }

            computeDijkstra();
//            System.out.println(Arrays.toString(dist));
            for (int i = 0; i < N; i++) {
                System.out.print(i+": ");
                for (int j: shortestPath.get(i)) {
                    System.out.print(j+" ");
                }
                System.out.println();
            }
        }


    }

    static void computeDijkstra() {
        PriorityQueue<Pair> pq = new PriorityQueue<>(Comparator.comparingInt(Pair::getSecond));

        visited[S] = true;
        dist[S] = 0;
        pq.add(new Pair(S, 0));

        while (!pq.isEmpty()) {
            Pair current = pq.poll();
            int v = current.first;
            for(Pair next: adjList.get(current.first)) {
                int nv = next.first;
                int nw = next.second;
                if(!visited[nv] && dist[v]+nw<=dist[nv]) {
                    if(dist[v]+nw == dist[nv]) {
                        shortestPath.set(nv, new ArrayList<>());
                    }
                    shortestPath.get(nv).add(v);
                    visited[nv] = true;
                    dist[nv] = dist[v] + nw;
                    pq.add(new Pair(nv, dist[nv]));
                }
            }
        }

    }
}

class Pair {
    int first;
    int second;

    public int getSecond() {
        return second;
    }

    public Pair(int first, int second) {
        this.first = first;
        this.second = second;
    }
}