package DAY06.P1922;

import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static boolean[] visited;
    static ArrayList<ArrayList<Pair>> adjList;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());
        
        adjList = new ArrayList<>(N+1); // adjList[v1] = (v2, cost)
        for (int i = 0; i <= N; i++) {
            adjList.add(new ArrayList<>());
        }

        int a, b, c;
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());

            adjList.get(a).add(new Pair(b, c));
            adjList.get(b).add(new Pair(a, c));
        }

        PriorityQueue<Pair> pq = new PriorityQueue<>(Comparator.comparingInt(Pair::getSecond));
        visited = new boolean[N+1];

        pq.add(new Pair(1, 0));

        int answer = 0;
        int v, cost;
        while (pq.isEmpty() == false) {
            Pair current = pq.poll();
            v = current.first;
            cost = current.second;

            if (visited[v] == true) {
                continue;
            }

            answer += cost;
            visited[v] = true;

            for(Pair next: adjList.get(v)){
                pq.add(new Pair(next.first, next.second));
            }

        }
        System.out.println(answer);
    }
}

class Pair {
    int first;
    int second;

    public Pair(int first, int second) {
        this.first = first;
        this.second = second;
    }

    public int getSecond() {
        return second;
    }

    @Override
    public String toString() {
        return "Pair{" +
                "first=" + first +
                ", second=" + second +
                '}';
    }
}