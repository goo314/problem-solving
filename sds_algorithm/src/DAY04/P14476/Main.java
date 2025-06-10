package DAY04.P14476;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[] nums;
    static int[] gcdLtoR;
    static int[] gcdRtoL;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        nums = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

//        int[] gcdFromStart = new int[N];
//
//        int gcdSoFar = nums[0];
//        gcdFromStart[0] = nums[0];
//        for (int i = 1; i < N; i++) {
//            gcdSoFar = gcd(gcdSoFar, nums[i]);
//            gcdFromStart[i] = gcdSoFar;
//        }
//
//        int[] gcdFromEnd = new int[N];
//        gcdSoFar = nums[N-1];
//        gcdFromEnd[0] = nums[N-1];
//        for (int i = N-1; i >= 0; i--) {
//            gcdSoFar = gcd(gcdSoFar, nums[i]);
//            gcdFromEnd[i] = gcdSoFar;
//        }
//
//        int maxGcd = 0, temp, answer = 0;
//        for (int i = 0; i < N; i++) {
//            if (i == 0) {
//                temp = gcdFromEnd[i+1];
//            } else if (i == N - 1) {
//                temp = gcdFromStart[i-1];
//            } else {
//                temp = gcd(gcdFromStart[i-1] , gcdFromEnd[i+1]);
//            }
//
//            if (maxGcd < temp) {
//                maxGcd = temp;
//                answer = nums[i];
//            }
//        }
//
//        if (answer % maxGcd == 0) {
//            System.out.println(-1);
//        } else {
//            System.out.print(maxGcd);
//            System.out.print(" ");
//            System.out.println(answer);
//        }

        gcdLtoR = new int[N];
        gcdRtoL = new int[N];

        gcdLtoR[0] = nums[0];
        for (int i = 0; i < N; i++) {
            gcdLtoR[i] = gcd(gcdLtoR[i-1], nums[i]);
        }

        gcdRtoL[N-1] = nums[N-1];
        for (int i = N-2; i >= 0; i--) {
            gcdRtoL[i] = gcd(gcdRtoL[i+1], nums[i]);
        }

        int max = 0;
        int maxIndex = 0;
        for (int i = 0; i < N; i++) {
            int temp = 0;
            // 왼쪽끝
            if (i == 0) {
                temp = gcdRtoL[1];
            }
            // 오른쪽끝
            else if (i == N-1) {
                temp = gcdLtoR[N-2];
            }
            // 중간
            else {
                temp = gcd(gcdLtoR[i-1], gcdRtoL[i-2]);
            }

            if (nums[i] % temp != 0 && max < temp) {
                max = temp;
                maxIndex = i;
            }
        }


    }

    static int gcd(int a, int b) {
        // gcd(a, b) == gcd(b, a % b), a % b가 0일 때 b에
        while (b != 0) {
            int r = a % b;
            a = b;
            b = r;
        }
        return a;
    }
}
