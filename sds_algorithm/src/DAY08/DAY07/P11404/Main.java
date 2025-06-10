package DAY07.P11404;

import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static int[][] dist;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());

        dist = new int[N+1][N+1];
        for (int i = 0; i <= N; i++) {
            for (int j = 0; j <= N; j++) {
                dist[i][j] = 10000001;
                if (i == j) {
                    dist[i][j] = 0;
                }
            }
        }

        for (int i = 0; i < M; i++) {
            int a, b, c;
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());
            if(c < dist[a][b]) {
                dist[a][b] = c;
            }
        }

        for (int k = 1; k <= N; k++) {
            for (int i = 1; i <= N; i++) {
                for (int j = 1; j <= N; j++) {
                    if(dist[i][j] > dist[i][k] + dist[k][j]){
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }

        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                if (dist[i][j] == 10000001) {
                    bw.write(0+" ");
                } else {
                    bw.write(dist[i][j]+" ");
                }
            }
            bw.write("\n");
        }
        bw.flush();
        bw.close();
    }

    static void printDist() {
        for (int i = 1; i <= N ; i++) {
            System.out.println(Arrays.toString(dist[i]));
        }
    }
}
