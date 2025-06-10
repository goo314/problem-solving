package DAY05.P11050;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int N, K;
    static int[][] dp = new int[11][11];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        System.out.println(combination(N, K));

    }

    static int combination(int n, int k) {
        if (n == k || k == 0) {
            return 1;
        }
        else {
            return dp[n][k] = combination(n-1, k) + combination(n-1, k-1);
        }
    }
}
