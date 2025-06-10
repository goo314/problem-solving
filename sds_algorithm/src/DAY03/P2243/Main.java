package DAY03.P2243;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int MAX = 1000000;
    static int[] tree;
    static int s;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        s = 1;
        while (s < MAX) {
            s *= 2;
        }

        tree = new int[2*s];

        N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int input = Integer.parseInt(st.nextToken());
            // 1. 사탕 꺼내기 -> (input=1, rank)
            if (input == 1) {
                int rank = Integer.parseInt(st.nextToken());
                int favor = query(1, s, 1, rank);
                System.out.println(favor);
                update(1, s, 1, favor, -1);

            }
            // 2. 사탕 넣기 -> (input=2, favor, num)
            else if (input == 2) {
                int favor = Integer.parseInt(st.nextToken());
                int num = Integer.parseInt(st.nextToken());
                update(1, s, 1, favor, num);

            }
        }

    }

    static int query(int left, int right, int node, int target) {
        // leaf -> 사탕 찾음
        if (left == right) {
            return left;
        }

        // 내부노드인 경우
        else {
            int mid = (left+right) / 2;
            if (tree[node * 2] >= target) {
                return query(left, right, node *2, target);
            } else {
                return query(mid+1, right, node*2+1, target-tree[node*2]);
            }
        }
    }

    static void update(int left, int right, int node, int target, int diff) {
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
}

