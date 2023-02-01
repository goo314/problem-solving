package P2143;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static long T;
    static int N, M;
//    static int[] arr1, arr2;
    static  long[] inputA, inputB;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        T = Long.parseLong(st.nextToken());

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());

        inputA = new long[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            inputA[i] = Long.parseLong(st.nextToken());
        }

        M = Integer.parseInt(br.readLine());

        inputB = new long[M];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            inputB[i] = Long.parseLong(st.nextToken());
        }

        List<Long> subA = new ArrayList<>();
        List<Long> subB = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            long sum = inputA[i];
            subA.add(sum);
            for (int j = i+1; j < N; j++) {
                sum += inputA[j];
                subA.add(sum);
            }
        }

        for (int i = 0; i < M; i++) {
            long sum = inputB[i];
            subB.add(sum);
            for (int j = i+1; j < M; j++) {
                sum += inputB[j];
                subB.add(sum);
            }
        }

        Collections.sort(subA);
        Collections.sort(subB, Comparator.reverseOrder());

        long result = 0;
        int ptA = 0, ptB = 0;
        while(true) {
            long currentA = subA.get(ptA);
            long target = T - currentA;
            if (subB.get(ptB) > target) {
                ptB++;
            } else if (subB.get(ptB) < target) {
                ptA++;
            } else { // target == currentB
                long countA = 0;
                long countB = 0;
                while(ptA < subA.size() && subA.get(ptA) == currentA){
                    ptA++;
                    countA++;
                }
                while(ptB < subB.size() && subB.get(ptB) == target){
                    ptB++;
                    countB++;
                }
                result += countA * countB;
            }

            if(ptA == subA.size() || ptB == subB.size()){
                break;
            }
        }

        System.out.println(result);



//        arr1 = new int[N];
//        st = new StringTokenizer(br.readLine());
//        for (int i = 0; i < N; i++) {
//            arr1[i] = Integer.parseInt(st.nextToken());
//        }
//
//        st = new StringTokenizer(br.readLine());
//        M = Integer.parseInt(st.nextToken());
//
//        arr2 = new int[M];
//        st = new StringTokenizer(br.readLine());
//        for (int i = 0; i < M; i++) {
//            arr2[i] = Integer.parseInt(st.nextToken());
//        }
//
//        int cntSubArr1 = 0, cntSubArr2 = 0, num;
//        long[] sortedSubArr1 = new long[(N*(N+1))/2];
//        long[] sortedSubArr2 = new long[(M*(M+1))/2];
//
//        for (int i = 0; i < N; i++) {
//            num = 0;
//            for (int j = i; j < N; j++) {
//                num += arr1[j];
//                sortedSubArr1[cntSubArr1++] = num;
//            }
//        }
//        Arrays.sort(sortedSubArr1);
//
//        for (int i = 0; i < M; i++) {
//            num = 0;
//            for (int j = i; j < M; j++) {
//                num += arr2[j];
//                sortedSubArr2[cntSubArr2++] = num;
//            }
//        }
//        Arrays.sort(sortedSubArr2);
//
//        System.out.println(Arrays.toString(sortedSubArr1));
//        System.out.println(Arrays.toString(sortedSubArr2));
//
//        int p1 = 0, p2 = cntSubArr2-1, sub1, sub2, answer = 0;
//        long sum;
//        while (p1 < cntSubArr1 && p2 >= 0) {
//            sum = sortedSubArr1[p1] + sortedSubArr2[p2];
//            System.out.printf("%d %d %d\n", p1, p2, sum);
//            if (sum < T) {
//                p1++;
//            } else if(sum == T){
//                sub1 = 1;
//                while(p1<cntSubArr1-1 && sortedSubArr1[p1] == sortedSubArr1[p1+1]) {
//                    sub1++;
//                    p1++;
//                }
//
//                sub2 = 1;
//                while(p2>0 && sortedSubArr2[p2] == sortedSubArr2[p2-1]) {
//                    sub2++;
//                    p2--;
//                }
//                answer += sub1 * sub2;
//                p1++;
//                p2--;
//            } else {
//                p2--;
//            }
//        }
//
//        System.out.println(answer);

    }
}
