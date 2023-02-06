// TODO: sort people by rank and use Indexed tree
package DAY01.P2517;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.PriorityQueue;

public class Main {
    static int N;
    static int s;
    static int[] tree;
    static PriorityQueue<Person> pq = new PriorityQueue<>(Comparator.comparingLong(Person::getSkill));
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        s = 1;
        while (s < N) {
            s *= 2;
        }

        tree = new int[2*s];
        for (int rank = 1; rank <= N; rank++) {
            long skill = Long.parseLong(br.readLine());
            pq.add(new Person(rank, skill));

            while (pq.isEmpty() == false && pq.peek().skill <= skill) {
                Person p = pq.poll();
                System.out.print(p.skill+" ");
                update(1, s, 1, p.rank, 1);
            }
            System.out.println();

//            System.out.println(rank +" " + skill + " " + query(1, s, 1, 1, rank-1));
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

class Person {
    int rank;
    long skill;

    public Person(int rank, long skill) {
        this.rank = rank;
        this.skill = skill;
    }

    public int getRank() {
        return rank;
    }

    public long getSkill() {
        return skill;
    }

    @Override
    public String toString() {
        return "{" + rank + ", " + skill + '}';
    }
}