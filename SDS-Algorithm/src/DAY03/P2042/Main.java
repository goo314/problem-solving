package P2042;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N ,M, K;
    static long[] nums;
    static long[] tree;
    static int s;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        nums = new long[N];
        for (int i = 0; i < N; i++) {
            nums[i] = Long.parseLong(br.readLine());
        }

        s = 1;
        while (s < N) {
            s *= 2;
        }

        tree = new long[2*s];
        init();

        for (int i = 0; i < M+K; i++) {
            st = new StringTokenizer(br.readLine());
            int type = Integer.parseInt(st.nextToken());
            // 1. update
            if (type == 1) {
                int target = Integer.parseInt(st.nextToken());
                long value = Long.parseLong(st.nextToken());
//                update(1, s, 1, target, value - nums[target]);
                updateBU(target, value);
            }
            // 2. query
            else {
                int queryLeft = Integer.parseInt(st.nextToken());
                int queryRight = Integer.parseInt(st.nextToken());
//                long result = query(1, s, 1, queryLeft, queryRight);
                long result = queryBU(queryLeft, queryRight);
                System.out.println(result);
            }
        }


    }

    static void init() {
        // leaf는 데이터로
        for (int i = 0; i < N; i++) {
            tree[s+i] = nums[i];
        }
        // 내부노드는 자식의 합
        for (int i = s-1; i > 0; i--) {
            tree[i] = tree[2*i] + tree[2*i+1];
        }
    }

    static long query(int left, int right, int node, int queryLeft, int queryRight) {
        // 1. 연관 없음
        if (queryRight < left || right < queryLeft) {
            return 0;
        }
        // 2. 연관 가능 ( 쏙 들어감 )
        else if (queryLeft <= left && right <= queryRight) {
            return tree[node];
        }
        // 3. 판단 불가 ( 걸쳐 있음 )
        else {
            int mid = (left + right) / 2;
            long leftResult = query(left, mid, node*2, queryLeft, queryRight);
            long rightResult = query(mid+1, right, node*2+1, queryLeft, queryRight);
            return leftResult + rightResult;
        }
    }

    static void update(int left, int right, int node, int target, long diff) {
        // 1. 연관 없음
        if (target < left || right < target) {
            return;
        }
        // 2. 연관 있음
        else {
            tree[node] += diff;
            if (left != right) {
                int mid = (left+right)/2;
                update(left, mid, node*2, target, diff);
                update(mid+1, right, node*2+1, target, diff);
            }
        }
    }

    static long queryBU(int queryLeft, int queryRight) {
        long sum = 0;
        int left = s + queryLeft - 1;
        int right = s + queryRight - 1;

        while (left <= right) {
            if (left % 2 == 1) {
                sum += tree[left++];
            }
            if (right % 2 == 0) {
                sum += tree[right--];
            }
            left /= 2;
            right /= 2;
        }

        return sum;
    }

    static void updateBU(int target, long value) {
        int node = s + target - 1;
        tree[node] = value;
        node /= 2;
        while (node > 0) {
            tree[node] = tree[node*2]+tree[node*2+1];
            node /= 2;
        }

    }
}
