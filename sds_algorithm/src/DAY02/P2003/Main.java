package DAY02.P2003;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static int[] numbers;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        numbers = new int[N+1];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            numbers[i] = Integer.parseInt(st.nextToken());
        }

        int low = 0, high = 0, sum = 0, count = 0;
        sum = numbers[0];
        while (true) {
            if (sum == M) {
                count++;
                sum -= numbers[low++];
            } else if (sum > M) {
                sum -= numbers[low++];
            } else {
                sum += numbers[++high];
            }
            if(high == N) {
                break;
            }
        }

        System.out.println(count);


//        Scanner sc = new Scanner(System.in);
//
//        N = sc.nextInt();
//        M = sc.nextInt();
//
//        numbers = new int[N];
//        for (int i = 0; i < N; i++) {
//            numbers[i] = sc.nextInt();
//        }
//
//        int left = 0, right = 0, sum = numbers[0];
//        int count = 0;
//        while(left < N && right < N){
//            if(sum < M){
//                right++;
//                if(right < N){
//                    sum += numbers[right];
//                }
//            } else if(sum == M){
//                count++;
//                sum -= numbers[left];
//                left++;
//            } else {
//                sum -= numbers[left];
//                left++;
//            }
//        }
//
//        System.out.println(count);

    }
}
