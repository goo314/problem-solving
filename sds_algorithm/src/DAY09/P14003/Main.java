package DAY09.P14003;

import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[] input;
    static ArrayList<Integer> dp = new ArrayList<>();
    static int[] parent;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());

        input = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            input[i] = Integer.parseInt(st.nextToken());
        }

        parent = new int[N];
        for (int i = 0; i < N; i++) {
            int low=0, high=dp.size()-1, mid = 0;

            while (low <= high) {
                mid = (low+high)/2;
                if(dp.get(mid) == input[i]) {
                    low = mid;
                    break;
                } else if (dp.get(mid) < input[i]) {
                   low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }

            if (low == dp.size()) {
                dp.add(input[i]);
            } else {
                dp.set(low, input[i]);
            }
            parent[i] = low;
        }

        bw.write(dp.size()+"\n");

        Stack<Integer> stack = new Stack<>();

        int target = dp.size() - 1;
        for (int i = N-1; i >= 0; i--) {
            if (parent[i] == target) {
                stack.add(input[i]);
                target--;
            }
        }

        while(!stack.isEmpty()) {
            bw.write(stack.pop()+" ");
        }

        bw.flush();

    }
}
