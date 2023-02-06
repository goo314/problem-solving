package DAY05.P15663;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static int[] count = new int[10001];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            count[Integer.parseInt(st.nextToken())]++;
        }

        dfs(0, 0, "");

    }

    static void dfs(int num, int length, String seq) {
        // 1. 체크인
        count[num]--;
        // 2. 목적지인가
        if (length == M) {
            System.out.println(seq);
        }
        // 3. 연결된 곳 순회
        for (int i = 1; i <= 10000; i++) {
            // 4. 갈 수 있는가
            if (count[i] > 0) {
                // 5. 간다.
                dfs(i, length+1, seq+i+" ");
            }
        }

        // 6. 체크아웃
        count[num]++;
    }
}
