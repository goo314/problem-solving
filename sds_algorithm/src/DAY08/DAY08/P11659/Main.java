package DAY08.P11659;

import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static int[] input;
    static int[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        input = new int[N+1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            input[i] = Integer.parseInt(st.nextToken());
        }

        dp = new int[N+1];
        dp[1] = input[1];
        for (int i = 2; i <= N; i++) {
            dp[i] = dp[i-1] + input[i];
        }

        int from, to;
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            from = Integer.parseInt(st.nextToken());
            to = Integer.parseInt(st.nextToken());
            bw.write(dp[to] - dp[from-1]+"\n");
        }

        bw.flush();
    }
}
