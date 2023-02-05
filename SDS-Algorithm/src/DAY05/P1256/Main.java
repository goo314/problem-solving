package DAY05.P1256;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N, M, K;
    static int[][] C;
    static int[][] dp = new int[201][201];
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

//        C = new int[N+M+1][N+M+1];
//        C[0][0] = 1;
//        C[1][0] = 1;
//        C[1][1] = 1;
//        for (int i = 1; i <= N+M; i++) {
//            C[i][0] = 1;
//            for (int j = 1; j <= N+M; j++) {
//                C[i][j] = Math.min(C[i-1][j-1] + C[i-1][j], (int) 1e9);
//            }
//        }
//
//        if (C[N + M][N] < K) {
//            System.out.println(-1);
//        } else {
//            StringBuilder sb = new StringBuilder();
//
//            int n=N-1, m=M, k=K;
//            for (int i = 0; i < N+M; i++) {
//                if (C[n + m][m] < k) {
//                    sb.append('z');
//                    k -= C[n+m][m];
//                    m--;
//                } else {
//                    sb.append('a');
//                    n--;
//                }
//            }
//
//            System.out.println(sb.toString());

//            int answer = 1;
//            n = N-1;
//            m = M;
//            String target = sb.toString();
//            for (int i = 0; i < target.length(); i++) {
//                if (target.charAt(i) == 'a') {
//                    n--;
//                } else {
//                    answer += C[n+m][m];
//                    m--;
//                }
//            }
//
//            System.out.println(answer);

        if (N > combination(N + M, M)) {
            System.out.println(-1);
        } else {
            StringBuilder sb = new StringBuilder();
            query(N, M, K);
            System.out.println(sb.toString());
        }

    }

    public static void query(int n, int m, int k) {
        if (n + m == 0) {
            return;
        } else if (n == 0) {
            sb.append('z');
            query(n-1, m, k);
        } else {
            int limit = combination(n+m-1, m);
            if (limit >= k) {
                sb.append('a');
                query(n-1, m, k);
            } else {
                sb.append('z');
                query(n, m-1, k-limit);
            }
        }
    }

    public static int combination(int n, int r) {
        if (n == r || r == 0) {
            return 1;
        } else if (dp[n][r] != 0) {
            return dp[n][r];
        } else {
            return dp[n][r] = (int) Math.min(1e9, combination(n-1, r-1) + combination(n-1, r));
        }
    }

}
