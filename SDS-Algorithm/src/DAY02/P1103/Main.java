package P1103;

import java.util.Scanner;

public class Main {
    static int N, M;
    static int[][] board;
    static int[][] visited;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();

        board = new int[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                board[i][j] = sc.nextInt();
            }
        }

    }
}
