package DAY06.P1717;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static int[] parent;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        parent = new int[N+1];
        init();

        int type, a, b;
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            type = Integer.parseInt(st.nextToken());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());

            if (type == 0) {
                union(a, b);
            }

            else if (type == 1) {
                int rootA = find(a);
                int rootB = find(b);
                if (rootA == rootB) {
                    System.out.println("YES");
                } else {
                    System.out.println("NO");
                }
            }

        }
    }

    static void init() {
        for (int i = 0; i <= N; i++) {
            parent[i] = i;
        }
    }

    static void union(int a, int b) {
        int rootA = find(a);
        int rootB = find(b);
        parent[rootA] = rootB;
    }

    static int find(int x) {
        if (parent[x] == x) {
            return x;
        }
        return parent[x] = find(parent[x]);
    }

}
