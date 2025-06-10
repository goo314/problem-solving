package DAY03.P10828;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Objects;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static Stack<Integer> stack;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        String cmd;
        stack = new Stack<>();
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            cmd = st.nextToken();
            if (Objects.equals(cmd, "push")) {
                int x = Integer.parseInt(st.nextToken());
                stack.push(x);
            }

            else if(Objects.equals(cmd, "pop")) {
                if (stack.isEmpty()) {
                    System.out.println(-1);
                } else {
                    System.out.println(stack.peek());
                    stack.pop();
                }
            }

            else if (Objects.equals(cmd, "size")) {
                System.out.println(stack.size());
            }

            else if (Objects.equals(cmd, "empty")) {
                if (stack.isEmpty()) {
                    System.out.println(1);
                } else {
                    System.out.println(0);
                }
            }

            else if(Objects.equals(cmd, "top")) {
                if (stack.isEmpty()) {
                    System.out.println(-1);
                } else {
                    System.out.println(stack.peek());
                }
            }

        }
    }
}
