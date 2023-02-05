package DAY05.P1722;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static long[] factorial;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());

        factorial = new long[N+1];
        factorial[0] = 1;
        for (int i = 1; i <= N; i++) {
            factorial[i] = factorial[i-1]*i;
        }

        int type;
        st = new StringTokenizer(br.readLine());
        type = Integer.parseInt(st.nextToken());

        if (type == 1) {
            StringBuilder sb = new StringBuilder();

            ArrayList<Integer> nums = new ArrayList<>();
            for (int i = 1; i <= N; i++) {
                nums.add(i);
            }

            long k = Long.parseLong(st.nextToken());
            int n = N-1;
            for (int i = 0; i < N; i++) {
                int current = 0;
                while (factorial[n] < k) {
                    k -= factorial[n];
                    current++;
                }
                sb.append(nums.get(current));
                nums.remove(current);
                sb.append(" ");
                n--;
            }
            sb.deleteCharAt(sb.length()-1);
            System.out.println(sb.toString());

        } else {
            boolean[] checked = new boolean[N+1];

            int[] input = new int[N];
            for (int i = 0; i < N; i++) {
                input[i] = Integer.parseInt(st.nextToken());
            }

            long answer = 1;
            int n = N-1;

            for (int i = 0; i < N; i++) {
                int current = 1;
                while (current != input[i]) {
                    if (checked[current] == false) {
                        answer += factorial[n];
                    }
                    current++;
                }
                n--;
                checked[current] = true;
            }
            System.out.println(answer);
        }
    }
}
