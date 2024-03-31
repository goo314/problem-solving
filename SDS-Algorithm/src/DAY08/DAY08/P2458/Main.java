package DAY08.P2458;

import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static boolean[][] floyd;
    static ArrayList<ArrayList<Integer>> adjList = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        floyd = new boolean[N+1][N+1];

        int a, b;
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            floyd[a][b] = true;
        }

        // floyd-warchall
        for (int k = 1; k <= N; k++) {
            for (int i = 1; i <= N; i++) {
                for (int j = 1; j <= N; j++) {
                    if (floyd[i][j] || (floyd[i][k] && floyd[k][j])) {
                        floyd[i][j] = true;
                    }
                }
            }
        }

        int answer = 0;
        for (int i = 1; i <= N; i++) {
            int temp = 0;
            for (int j = 1; j <= N; j++) {
                if (i == j) continue;

                if (floyd[i][j]) temp++;
                if(floyd[j][i]) temp++;
            }

            if (temp == N - 1) {
                answer++;
            }
        }

        bw.write(answer+"\n");
        bw.flush();

    }
}
