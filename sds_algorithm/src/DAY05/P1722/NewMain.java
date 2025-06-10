package DAY05.P1722;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class NewMain {
    static int N;
    static long[] fact;
    static int[] nums;
    static boolean[] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());

        fact = new long[N+1];
        fact[0] = 1;
        for (int i = 1; i <= N; i++) {
            fact[i] = fact[i-1]*i;
        }

        int command;
        st = new StringTokenizer(br.readLine());
        command = Integer.parseInt(st.nextToken());

        if (command == 1) {
            long target = Long.parseLong(st.nextToken());
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < N; i++) {
                for (int j = 1; j <= N; j++) {
                    if (visited[j] == true) {
                        continue;
                    }
                    // Target이 경계보다 클 경우
                    if(target > fact[N-i-1]) {
                        target -= fact[N-i-1];
                    }
                    // Target의 경계 이하일 경우
                    else {
                        sb.append(j);
                        sb.append(" ");
                        visited[j] = true;
                        break;
                    }
                }
            }

        } else if (command == 2) {
            nums = new int[N];
            for (int i = 0; i < N; i++) {
                nums[i] = Integer.parseInt(st.nextToken());
            }

            long result = 0;
            for (int i = 0; i < N; i++) {
                for (int j = 1; j < nums[i]; j++) {
                    if (visited[j] == false) {
                        result += fact[N-i-1];
                    }
                }
                visited[nums[i]] = true;
            }

            System.out.println(result + 1);

        }
    }
}

