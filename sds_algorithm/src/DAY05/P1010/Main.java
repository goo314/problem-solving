package DAY05.P1010;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int T;
    static int[][] dp = new int[31][31];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        T = Integer.parseInt(br.readLine());

        int N, M;
        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            sb.append(combination(M, N)+"\n");
        }
        System.out.println(sb.toString());

    }

    static int combination(int n, int k){
        if (n == k || k == 0) {
            return 1;
        } else if(dp[n][k] != 0) {
            return dp[n][k];
        } else {
            return dp[n][k] = combination(n-1, k) + combination(n-1, k-1);
        }
    }
}
