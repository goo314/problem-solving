package DAY08.P1932;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[][] input;

    static long[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());

        input = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j <= i; j++) {
                input[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dp = new long[N][N];
        dp[0][0] = input[0][0];
        long answer = dp[0][0];
        for (int i = 1; i < N; i++) {
            for (int j = 0; j <= i; j++) {
                if (j == 0 || (i==1 && i==j)) {
                    dp[i][j] = dp[i-1][j] + input[i][j];
                } else if (j == i) {
                    dp[i][j] = dp[i-1][j-1] + input[i][j];
                } else {
                    dp[i][j] = Math.max(dp[i][j], Math.max(dp[i-1][j-1], dp[i-1][j])+input[i][j]);
                }

                if (answer < dp[i][j]) {
                    answer = dp[i][j];
                }

            }
        }
        System.out.println(answer);

    }
}
