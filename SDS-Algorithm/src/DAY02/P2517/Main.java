// TODO: sort people by rank and use Indexed tree
package DAY02.P2517;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Main {
    static int N;
    static int s;
    static int[] tree;
    static Runner[] runners;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        s = 1;
        while (s < N) {
            s *= 2;
        }

        tree = new int[2*s];
        runners = new Runner[N];

        for (int i = 0; i < N; i++) {
            long skill = Long.parseLong(br.readLine());
            runners[i] = new Runner(i+1, skill, 0);
        }

        // skill 오름차순으로 정렬
        Arrays.sort(runners, Comparator.comparingLong(Runner::getSkill));

        // 앞에 있는 사람 수 계산
        for (int i = 0; i < N; i++) {
            Runner runner = runners[i];
            update(1, s, 1, runner.rank, 1);
            runner.countPrev = query(1, s, 1, 0, runner.rank-1);
        }

        // rank 오름차순으로 정렬
        Arrays.sort(runners, Comparator.comparingInt(Runner::getRank));

        for (int i = 0; i < N; i++) {
            Runner runner = runners[i];
            System.out.println(runner.rank - runner.countPrev);
        }

    }

    static void update(int left, int right, int node, int target, int diff) {
        if (target < left || right < target) {
            return;
        }
        else {
            tree[node] += diff;
            if (left != right) {
                int mid = (left+right)/2;
                update(left, mid, node*2, target, diff);
                update(mid+1, right, node*2+1, target, diff);
            }
        }
    }

    static int query(int left, int right, int node, int queryLeft, int queryRight) {
        if (queryRight < left || right < queryLeft) {
            return 0;
        }
        else if (queryLeft <= left && right <= queryRight) {
            return tree[node];
        }
        else {
            int mid = (left + right) / 2;
            int leftResult = query(left, mid, node*2, queryLeft, queryRight);
            int rightResult = query(mid+1, right, node*2+1, queryLeft, queryRight);
            return leftResult + rightResult;
        }
    }

}

class Runner {
    int rank;
    long skill;
    int countPrev;

    public Runner(int rank, long skill, int countPrev) {
        this.rank = rank;
        this.skill = skill;
        this.countPrev = countPrev;
    }

    public int getRank() {
        return rank;
    }

    public long getSkill() {
        return skill;
    }

    @Override
    public String toString() {
        return "{" +
                "rank=" + rank +
                ", skill=" + skill +
                ", countPrev=" + countPrev +
                '}';
    }
}