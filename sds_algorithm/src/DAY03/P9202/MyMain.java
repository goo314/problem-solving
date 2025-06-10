package DAY03.P9202;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class MyMain {
    static int[] MX = { -1, -1, -1, 0, 0, 1, 1, 1};
    static int[] MY = {-1, 0, 1, -1, 1, -1, 0, 1};
    static int W, B;
    static int score;
    static String maxWord;
    static int countWord;

    static char[][] map;
    static boolean[][] visited;
    static Node root;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        W = Integer.parseInt(br.readLine());

        // make trie
        root = new Node(false, false, new Node[26]);
        Node currentNode;
        for (int i = 0; i < W; i++) {
            currentNode = root;
            char[] word = br.readLine().toCharArray();
            for (int j = 0; j < word.length; j++) {
                char c = word[j];
                if (currentNode.child[c - 'A'] == null) {
                    currentNode.child[c-'A'] = new Node(j == word.length - 1, false, new Node[26]);
                }
                currentNode = currentNode.child[c-'A'];
            }
        }

        br.readLine();

        B = Integer.parseInt(br.readLine());

        for (int i = 0; i < B; i++) {
            map = new char[4][4];
            for (int j = 0; j < 4; j++) {
                map[j] = br.readLine().toCharArray();
            }
            if(i < B-1) br.readLine();

            visited = new boolean[4][4];
            score = 0;
            countWord = 0;
            maxWord = "";
            initNode(root);

            for (int j = 0; j < 4; j++) {
                for (int k = 0; k < 4; k++) {
                    char c = map[j][k];
                    if (root.child[c-'A'] != null) {
                        dfs(j, k, root.child[c-'A'], ""+c);
                    }
                }
            }

            System.out.printf("%d %s %d\n", score, maxWord, countWord);

        }


    }

    static void initNode(Node node) {
        node.isHit = false;
        for (int i = 0; i < 26; i++) {
            if (node.child[i] != null) {
                initNode(node.child[i]);
            }
        }
    }

    static void dfs(int x, int y, Node node, String word) {
        // 1. 체크인
        visited[x][y] = true;

        // 2. 목적지인가
        if (node.isHit == false && node.isEnd == true) {
            int wordLength = word.length();
            countWord++;
            score += getScore(wordLength);
            if (maxWord.length() == wordLength) {
                if(maxWord.compareTo(word) > 0) {
                    maxWord = word;
                }
            }

            if (maxWord.length() < wordLength) {
                maxWord = word;
            }

            node.isHit = true;
        }

        // 3. 연결된 곳 순회
        for (int i = 0; i < 8; i++) {
            int nx = x + MX[i];
            int ny = y + MY[i];

            // 4. 갈 수 있는 가
            if (0 <= nx && nx < 4 && 0 <= ny && ny < 4) {
                char next = map[nx][ny];
                if (visited[nx][ny] == false && node.child[next - 'A'] != null) {
                    // 5. 간다.
                    dfs(nx, ny, node.child[next-'A'], word+next);
                }
            }
        }


        // 6. 체크아웃
        visited[x][y] = false;
    }

    static int getScore(int wordLength) {
        if (wordLength == 1 || wordLength== 2) {
            return 0;
        } else if (wordLength == 3 || wordLength == 4) {
            return  1;
        } else if (wordLength == 5) {
            return  2;
        } else if (wordLength == 6) {
            return 3;
        } else if (wordLength == 7) {
            return 5;
        } else if (wordLength == 8) {
            return  11;
        }
        return 0;
    }



}

class Node {
    boolean isEnd;
    boolean isHit;
    Node child[];

    public Node( boolean isEnd, boolean isHit, Node[] child) {
        this.isEnd = isEnd;
        this.isHit = isHit;
        this.child = child;
    }

    @Override
    public String toString() {
        return "{" + isEnd +
                ", " + isHit +
                ", " + Arrays.toString(child) +
                '}';
    }
}