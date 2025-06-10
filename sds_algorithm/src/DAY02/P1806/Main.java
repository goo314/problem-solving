package DAY02.P1806;

import java.util.Scanner;

public class Main {
    static int N;
    static long S;
    static int[] numbers;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        S = sc.nextLong();

        numbers = new int[N];
        for (int i = 0; i < N; i++) {
            numbers[i] = sc.nextInt();
        }

        int left = 0, right = 0;
        long sum = numbers[0];
        int answer = 100001, length = 1;
        while(left < N && right < N){
            if(sum < S){
                right++;
                if(right < N){
                    sum += numbers[right];
                }
                length++;
            } else {
                answer = Math.min(answer, length);
                sum -= numbers[left];
                length--;
                left++;
            }
        }

        if(answer == 100001){
            System.out.println(0);
        } else {
            System.out.println(answer);
        }

    }
}
