package DAY08.P3830;

import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static int[] parent;
    static long[] dist;
    static long answer;
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

            parent = new int[N+1];
            dist = new long[N+1];
            for (int i = 0; i <= N; i++) {
                parent[i] = i;
            }

            char type; int a, b, w;
            for (int i = 0; i < M; i++) {
                st = new StringTokenizer(br.readLine());
                type = st.nextToken().charAt(0);
                if (type == '!') {
                    a = Integer.parseInt(st.nextToken());
                    b = Integer.parseInt(st.nextToken());
                    w = Integer.parseInt(st.nextToken());
                    union(a, b, w);
                } else if (type == '?') {
                    a = Integer.parseInt(st.nextToken());
                    b = Integer.parseInt(st.nextToken());

                    int parentA = findParent(a);
                    int parentB = findParent(b);

                    if (parentA != parentB) {
                        bw.write("UNKNOWN\n");
                    } else {
                        answer = dist[b]-dist[a];
                        bw.write(answer+"\n");
                    }
                }
            }

            bw.flush();


        }
    }

    static void union(int a, int b, int w) {
        int parentA = findParent(a);
        int parentB = findParent(b);
        if (parentA == parentB) {
            return;
        }
        parent[parentB] = parentA;
        dist[parentB] = dist[a] - dist[b] + w;
    }

    static int findParent(int x) {
        if(parent[x] == x){
            return x;
        }
        int parentX = findParent(parent[x]);
        dist[x] += dist[parent[x]];
        return parent[x] = parentX;
    }
}