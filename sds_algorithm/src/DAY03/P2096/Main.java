package DAY03.P2096;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[] DY = { -1, 0, 1};
    static int[][] dpMax;
    static int[][] dpMin;
    static int N;
    static int[][] numbers;
    static int max, min;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());

        numbers = new int[N][3];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 3; j++) {
                numbers[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dpMax = new int[N][3];
        dpMin = new int[N][3];

        for (int i = 0; i < 3; i++) {

        }

    }

    static void dfs(int x, int y, int depth){

    }
}
