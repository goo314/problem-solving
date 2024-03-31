package DAY09.P11049;

import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static Matrix[] input;
    static int[][] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        
        N = Integer.parseInt(br.readLine());

        input = new Matrix[N];
        int r, c;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            r = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());
            input[i] = new Matrix(r, c);
        }

        dp = new int[N][N];
        for (int a = 1; a < N; a++) {
            for (int i = 0; i+a < N; i++) {
                dp[i][i+a] = dp[i][i+a-1] + dp[i+1][i+a] + input[i].row * input[i].col * input[i+a].col;
            }
        }

        for (int i = 0; i < N; i++) {
            System.out.println(Arrays.toString(dp[i]));
        }
        
    }
}

class Matrix {
    int row;
    int col;
    public Matrix(int row, int col) {
        this.row = row;
        this.col = col;
    }
}