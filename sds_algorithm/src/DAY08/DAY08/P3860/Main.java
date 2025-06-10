// TODO: bellman-ford
package DAY08.P3860;

import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {-1, -1, 0, 0};
    static int W, H, G;
    static int[][] edges;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        W = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());

        edges = new int[W][H];
        for (int i = 0; i < W; i++) {
            for (int j = 0; j < H; j++) {
                edges[W][H] = 1;
            }
        }

        G = Integer.parseInt(br.readLine());
        for (int i = 0; i < G; i++) {
            // 어머
            for (int j = 0; j < 4; j++) {
            }
        }

    }
}
