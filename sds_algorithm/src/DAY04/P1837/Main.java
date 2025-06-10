package DAY04.P1837;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static String P;
    static int K;
    static boolean[] isPrime;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        P = st.nextToken();
        K = Integer.parseInt(st.nextToken());

        // make prime list
        isPrime = new boolean[K];
        for (int i = 2; i < K; i++) {
            isPrime[i] = true;
        }

        for (int i = 2; i < K; i++) {
            if (isPrime[i] == true) {
                for (int j = i + i; j < K; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        // divide by prime
        int prime = 0;
        for (int i = 2; i < K; i++) {
            if (isPrime[i] == true) {
                if (divideBy(i) == true) {
                    prime = i;
                    break;
                }
            }
        }

        if (prime == 0) {
            System.out.println("GOOD");
        } else {
            System.out.print("BAD ");
            System.out.println(prime);
        }

    }

    static boolean divideBy(int x){
        int temp = 0;
        for (int i = 0; i < P.length(); i++) {
            temp = temp * 10 + (P.charAt(i) - '0');
            temp = temp % x;
        }

        if (temp == 0) {
            return true;
        } else {
            return false;
        }
    }


}
