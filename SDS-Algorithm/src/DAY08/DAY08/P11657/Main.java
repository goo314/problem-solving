package DAY08.P11657;

import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static Edge[] edges; // (v1, v2, w)
    static long[] dist;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        edges = new Edge[M];
        dist = new long[N+1];
        for (int i = 0; i <= N; i++) {
            dist[i] = 5000001;
        }

        int a, b, c;
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());
            edges[i] = new Edge(a, b, c);
        }

        dist[1] = 0;
        for (int i = 0; i < N-1; i++) {
            for (int j = 0; j < M; j++) {
                Edge edge = edges[j];
                if(dist[edge.from] != 5000001) {
                    dist[edge.to] = Math.min(dist[edge.to], dist[edge.from]+ edge.cost);
                }
            }
        }

        boolean isPossible = true;
        for (int j = 0; j < M; j++) {
            Edge edge = edges[j];
            if(dist[edge.from] != 5000001 && dist[edge.from]+ edge.cost < dist[edge.to]){
                isPossible = false;
                break;
            }
        }

        if (isPossible == false) {
//            bw.write(-1+"\n");
            sb.append(-1+"\n");
        } else {
            for (int i = 2; i <= N; i++) {
                if (dist[i] == 5000001) {
//                    bw.write(-1+"\n");
                    sb.append(-1+"\n");
                } else {
//                    bw.write(dist[i]+"\n");
                    sb.append(dist[i]+"\n");
                }
            }

        }
//        bw.flush();

        bw.write(sb.toString());
        bw.flush();
    }
}

class Edge {
    int from;
    int to;
    int cost;

    public Edge(int v1, int v2, int c) {
        this.from = v1;
        this.to = v2;
        this.cost = c;
    }
}