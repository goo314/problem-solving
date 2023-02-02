// TODO: input and print result

package DAY04.P9202;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int[] mx = { -1, 1, 0, 0, -1, 1, -1, 1};
    static int[] my = {0, 0, -1, 1, -1, -1, 1, 1};
    static int[] score = {0, 0, 0, 1, 1, 2, 3, 5, 11};
    static int W, N;
    static char[][] map;
    static boolean[][] visited;
    static String answer;
    static int sum;
    static int count;
    static StringBuilder sb = new StringBuilder();
    static TrieNode root = new TrieNode();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        W = Integer.parseInt(br.readLine());

        for (int i = 0; i < W; i++) {
            insert(br.readLine());
        }

        N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            root.clearHit();
            sum = 0;
            count = 0;
            answer = null;

            visited = new boolean[4][4];
            map = new char[4][4];

            for (int j = 0; j < 4; j++) {
                String x = br.readLine();
                for (int k = 0; k < 4; k++) {
                    map[j][k] = x.charAt(k);
                }
            }

            for (int j = 0; j < 4; j++) {
                for (int k = 0; k < 4; k++) {
                    search(j, k, root);
                    System.out.print(sum);
                    System.out.print(" ");
                    System.out.print(answer);
                    System.out.print(" ");
                    System.out.println(count);
                }
            }
        }



    }

    static void search(int y, int x, TrieNode node) {
        // 1. 체크인
        visited[y][x] = true;
        sb.append(map[y][x]);
        // 2. 목적지에 도달했는가?
        if (node.isEnd && node.isHit == false) {
            node.isHit = true;
            sum += score[sb.length()];
            count++;
            String foundAnswer = sb.toString();
            if (compare(answer, foundAnswer) > 0) {
                answer = foundAnswer;
            }
        }
        // 3. 연결된 곳을 순회
        for (int i = 0; i < 8; i++) {
            int ty = y + my[i];
            int tx = x + mx[i];
            // 4. 가능한가? : 맵을 벗어나지 않고, Trie에 단어가 있고, 방문한 적이 없고
            if (0 <= ty && ty < 4 && 0 <= tx && tx < 4) {
                if (node.hasChild(map[ty][tx]) && visited[ty][tx] == false) {
                    // 5. 간다
                    search(ty, tx, node.getChild(map[ty][tx]));
                }
            }
        }

        // 6. 체크아웃
        visited[y][x] = false;
        sb.deleteCharAt(sb.length()-1);
    }

    static int compare(String s1, String s2) {
        int result = s2.length() - s1.length();
        if (result == 0) {
            return s1.compareTo(s2);
        }
        return result;
    }

    static void insert(String word) {
        TrieNode current = root;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (current.hasChild(c) == false) {
                current.children[c-'A'] = new TrieNode();
            }
            current = current.getChild(c);
        }
        current.isEnd = true;
    }

}

class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isEnd;
    boolean isHit;

    boolean hasChild(char c) {
        return children[c-'A'] != null;
    }

    TrieNode getChild(char c) {
        return children[c-'A'];
    }

     void clearHit() {
        this.isHit = false;
         for (int i = 0; i < children.length; i++) {
             if (children[i] != null) {
                 children[i].clearHit();
             }
         }
     }
}