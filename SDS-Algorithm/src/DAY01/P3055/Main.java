package DAY01.P3055;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    static final int[] MX = {-1, 1, 0, 1};
    static final int[] MY = {0, 0, -1, 1};

    static int R, C;
    static char[][] map;
    static int[][] dp;
    static Queue<Point> queue;
    public static void main(String[] args) throws FileNotFoundException {
        System.setIn(new FileInputStream("src/DAY01/P3055/input.txt"));
        Scanner sc = new Scanner(System.in);
        R = sc.nextInt();
        C = sc.nextInt();

        map = new char[R][C];
        dp = new int[R][C];
        queue = new LinkedList<>();

        Point st = null;
        for (int i = 0; i < R; i++) {
            String line = sc.next();
            for (int j = 0; j < C; j++) {
                map[i][j] = line.charAt(j);
                if(map[i][j] == '*') {
                    queue.add(new Point(i, j, '*'));
                }
                if(map[i][j] == 'S') {
                    st = new Point(i, j, 'S');
                }
            }
        }

        queue.add(st);

        boolean foundAnswer = false;
        while(!queue.isEmpty()){
            // 1. 큐에서 가져옴
            Point p = queue.poll();
            // 2. 목적지인가? -> 고슴도치만 D에 도착
            if(p.type == 'D'){
                System.out.println(dp[p.x][p.y]);
                foundAnswer = true;
                break;
            }
            // 3. 연결된 곳을 순회 -> 상하좌우
            for (int i = 0; i < 4; i++) {
                int tx = p.x + MX[i];
                int ty = p.y + MY[i];
                // 4. 갈 수 있는가? (공통) -> 맵을 벗어나지 않고
                if(0<=tx && tx<R && 0<=ty && ty<C){
                    if(p.type == '.' || p.type == 'S'){
                        // 4. 갈 수 있는가? (고슴도치) -> ., D 방문체크
                        if((map[tx][ty] == '.' || map[tx][ty] == 'D') && dp[tx][ty] == 0){
                            // 5. 체크인(고슴도치) -> dp
                            dp[tx][ty] = dp[p.x][p.y] + 1;
                            // 6. 큐에 넣음
                            queue.add(new Point(tx, ty, map[tx][ty]));
                        }
                    } else  if(p.type == '*'){
                        // 4. 갈 수 있는가? (물) -> ., S
                        if(map[tx][ty] == '.' || map[tx][ty] == 'S'){
                            // 5. 체크인(물) -> map
                            map[tx][ty] = '*';
                            // 6. 큐에 넣음
                            queue.add(new Point(tx, ty, '*'));
                        }
                    }
                }
            }
        }

        if(foundAnswer == false){
            System.out.println("KAKTUS");
        }
    }
}

class Point {
    int x;
    int y;
    char type;

    public Point(int x, int y, char type) {
        this.x = x;
        this.y = y;
        this.type = type;
    }

    @Override
    public String toString() {
        return "Point{" +
                "x=" + x +
                ", y=" + y +
                ", type=" + type +
                '}';
    }
}
