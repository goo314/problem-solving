package DAY03.P2748;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static long[] fibo;
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        fibo = new long[N+1];
        for (int i = 0; i <= N; i++) {
            if(i == 0){
                fibo[i] = 0;
            }
            else if(i == 1){
                fibo[i] = 1;
            } else {
                fibo[i] = fibo[i-1] + fibo[i-2];
            }
        }

        System.out.println(fibo[N]);
    }
}
