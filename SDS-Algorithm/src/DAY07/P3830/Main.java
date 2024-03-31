package DAY07.P3830;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static int[] parent;
    static ArrayList<ArrayList<Pair>> adjList;
    static int answer;
    static boolean[] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        while (true) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            if (N == 0 && M == 0) {
                break;
            }

            parent = new int[N+1];
            for (int i = 0; i <= N; i++) {
                parent[i] = i;
            }

            adjList = new ArrayList<>();
            for (int i = 0; i <= N; i++) {
                adjList.add(new ArrayList<>());
            }


            char type; int a, b, w;
            for (int i = 0; i < M; i++) {
                st = new StringTokenizer(br.readLine());
                type = st.nextToken().charAt(0);
                if (type == '!') {
                    a = Integer.parseInt(st.nextToken());
                    b = Integer.parseInt(st.nextToken());
                    w = Integer.parseInt(st.nextToken());
                    union(a, b);
                    adjList.get(a).add(new Pair(b, w));
                    adjList.get(b).add(new Pair(a, -w));
                } else if (type == '?') {
                    a = Integer.parseInt(st.nextToken());
                    b = Integer.parseInt(st.nextToken());

                    int parentA = findParent(a);
                    int parentB = findParent(b);

                    if (parentA != parentB) {
                        System.out.println("UNKNOWN");
                    } else {
                        visited = new boolean[N+1];
                        dfs(a, b, 0);
                        System.out.println(answer);
                    }
                }
            }


        }
    }

    static void union(int a, int b) {
        int parentA = findParent(a);
        int parentB = findParent(b);
        parent[parentA] = parentB;
    }

    static int findParent(int x) {
        if(parent[x] == x){
            return x;
        }
        return parent[x] = findParent(parent[x]);
    }

    static void dfs(int current, int target, int w){
        visited[current] = true;

        if(current == target){
            answer = w;
            return;
        }

        for (Pair next: adjList.get(current)) {
            if(visited[next.vertex] == false){
                dfs(next.vertex, target, w+next.weight);
            }
        }

        visited[current] = false;

    }

    static void printAdjList() {
        for (int i = 0; i <= N; i++) {
            System.out.print(i+" ");
            for (Pair p: adjList.get(i)) {
                System.out.print(p+" ");
            }
            System.out.println();
        }
    }
}

class Pair {
    int vertex;
    int weight;

    public Pair(int vertex, int weight) {
        this.vertex = vertex;
        this.weight = weight;
    }

    @Override
    public String toString() {
        return "Pair{" +
                "vertex=" + vertex +
                ", weight=" + weight +
                '}';
    }
}