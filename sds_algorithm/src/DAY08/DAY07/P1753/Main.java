package DAY07.P1753;

import java.io.*;
import java.util.*;

public class Main {
    static int V, E, K;
    static int[] dist;
    static ArrayList<ArrayList<Pair>> adjList; // adjList[v1] = (v2, w)
    static PriorityQueue<Pair> pq; // (v, w)

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(br.readLine());

        adjList = new ArrayList<>();
        for (int i = 0; i <= V; i++) {
            adjList.add(new ArrayList<>());
        }

        int u, v, w;
        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            u = Integer.parseInt(st.nextToken());
            v = Integer.parseInt(st.nextToken());
            w = Integer.parseInt(st.nextToken());
            adjList.get(u).add(new Pair(v, w));
        }

        dist = new int[V+1];
        for (int i = 0; i <= V; i++) {
            dist[i] = Integer.MAX_VALUE;
        }

        pq = new PriorityQueue<>(new Comparator<Pair>() {
            @Override
            public int compare(Pair p1, Pair p2) {
                return p1.second - p2.second;
            }
        });


        pq.add(new Pair(K, 0));
        dist[K] = 0;

        int v1, w1, v2, w2;
        while(pq.isEmpty() == false) {
            Pair current = pq.poll();
            v1 = current.first;
            w1 = current.second;

            for (Pair next: adjList.get(current.first)) {
                v2 = next.first;
                w2 = next.second;

                if(dist[v1]+w2 < dist[v2]){
                    dist[v2] = dist[v1]+w2;
                    pq.add(new Pair(v2, dist[v2]));
                }
            }
        }

        for (int i = 1; i <= V; i++) {
            if (dist[i] == Integer.MAX_VALUE) {
                bw.write("INF\n");
            } else {
                bw.write(dist[i]+"\n");
            }
        }

        bw.flush();
        bw.close();

    }
}

class Pair {
    int first;
    int second;

    public Pair(int first, int second) {
        this.first = first;
        this.second = second;
    }

}