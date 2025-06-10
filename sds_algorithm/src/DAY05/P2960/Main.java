// TODO: 정수론 > 에라토스테네스의 체

package DAY05.P2960;

import java.util.Scanner;

public class Main {
    static int N, K;
    static int[] numbers;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        K = sc.nextInt();

        numbers = new int[N];
        for (int i = 2; i < N; i++) {
            numbers[i] = i;
        }

    }
}
