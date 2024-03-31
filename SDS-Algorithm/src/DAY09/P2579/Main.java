package DAY09.P2579;

import java.io.*;

public class Main {
    static int N;
    static int[] input;
    static int[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        N = Integer.parseInt(br.readLine());
        input = new int[N+1];
        for (int i = 1; i <= N; i++) {
            input[i] = Integer.parseInt(br.readLine());
        }

        int max = 0;
        dp = new int[N+1];
        for (int i = 1; i <= N; i++) {

        }

    }
}
