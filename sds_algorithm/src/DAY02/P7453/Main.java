package DAY02.P7453;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static long[] inputA, inputB, inputC, inputD;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        StringTokenizer st;
        inputA = new long[N];
        inputB = new long[N];
        inputC = new long[N];
        inputD = new long[N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            inputA[i] = Integer.parseInt(st.nextToken());
            inputB[i] = Integer.parseInt(st.nextToken());
            inputC[i] = Integer.parseInt(st.nextToken());
            inputD[i] = Integer.parseInt(st.nextToken());
        }

        ArrayList<Long> sumAB = new ArrayList<>();
        ArrayList<Long> sumCD = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            for (int j = i+1; j < N; j++) {
                long sumab = inputA[i] + inputB[j];
                sumAB.add(sumab);
                long sumcd = inputC[i] + inputB[j];
                sumCD.add(sumcd);
            }
        }

        Collections.sort(sumAB);
        Collections.sort(sumCD);



    }
}
