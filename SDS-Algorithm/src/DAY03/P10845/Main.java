package DAY03.P10845;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Objects;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int back = 0;
    static Queue<Integer> q;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        q = new LinkedList<>();
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String cmd = st.nextToken();

            if (Objects.equals(cmd, "push")) {
                int x = Integer.parseInt(st.nextToken());
                back = x;
                q.add(x);
            }

            else if (Objects.equals(cmd, "pop")) {
                if (q.isEmpty() == true) {
                    System.out.println(-1);
                } else {
                    System.out.println(q.poll());
                }
            }

            else if (Objects.equals(cmd, "size")) {
                System.out.println(q.size());
            }

            else if (Objects.equals(cmd, "empty")) {
                if (q.isEmpty() == true) {
                    System.out.println(1);
                } else {
                    System.out.println(0);
                }
            }

            else if (Objects.equals(cmd, "front")) {
                if (q.isEmpty() == true) {
                    System.out.println(-1);
                } else {
                    System.out.println(q.peek());
                }

            }

            else if (Objects.equals(cmd, "back")) {
                if (q.isEmpty() == true) {
                    System.out.println(-1);
                } else {
                    System.out.println(back);
                }

            }
        }

    }
}
