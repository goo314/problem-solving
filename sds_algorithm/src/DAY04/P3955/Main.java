package DAY04.P3955;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int T;
    static int K, C;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());
            K = Integer.parseInt(st.nextToken());
            C = Integer.parseInt(st.nextToken());

//            if (hasAnswer() == false) {
//                System.out.println("IMPOSSIBLE");
//                continue;
//            }
//
//            long answer = findInitialAnswer();
//
//            while (answer < K) {
//                answer += K;
//            }
//
//            while (answer >= 1e9) {
//                answer -= K;
//            }
//
//            if (answer <= 0 || answer > 1e9) {
//                System.out.println("IMPOSSIBLE");
//            } else {
//                System.out.println(answer);
//            }

            // X: 인당 나너줄 사탕의 수
            // Y: 사탕 문자의 수
            // A*X + ! = B*Y
            // Ax + By = C 의 형태로 변환
            // Ax + By = 1
            // A(-x) + By = 1의 형태로 변환 -> 추후 k를 구할 때 x의 범위가 반전된다.

            EGResult result = egcd(K, C);
            // Ax + By = C 일떄 C % gcd(A, B) == 0 이여야 해를 가질 수 있음 : 베주 항등식
            if (result.r != 1) {
                System.out.println("IMPOSSIBLE");
            } else {
                // As + Bt = r, Ax + By = C 두 식에서 C와 r을 일치시켜서 x0, y0를 구할 수 있음 -> 초기해
                // x0 = s * c/r
                // y0 = t * c/r
                long x0 = result.s;
                long y0 = result.t;

                // 일반해 공식
                // x = x0 + B/gcd * k
                // y = y0 - A/gcd * k

                // x < 0
                // x0 + B * k < 0
                // k < -x0 / B

                // 0 < y <= 1e9
                // 0 < y0 - A * k <= 1e9
                // -(y0-1e9)/A <= k < y0/A

                // -(y0-1e9)/A <= k < y0/A
                //                k < -x0 / B

                long kFromY = (long) (Math.ceil((double) y0 / (double) K) - 1);
                long kFromX = (long) (Math.ceil((double) -x0/ (double) C) - 1);

                long k = Math.min(kFromX, kFromY);
                long kLimitFromY = (long) Math.ceil((double) (y0-1e9) / (double) K);

                if (kLimitFromY <= k) {
                    System.out.println(y0 - K*k);
                } else {
                    System.out.println("IMPOSSIBLE");
                }

            }



        }
    }

    static int gcd(int a, int b) {
        while(b != 0) {
            int r = a % b;
            a = b;
            b = r;
        }
        return a;
    }

    static boolean hasAnswer() {
        int gcd = gcd(K, C);
        if (1 % gcd == 0) {
            return true;
        }
        return false;
    }

    static long findInitialAnswer() {

        // x = 사탕 개수, y = 봉지 개수
        // K*x + 1 = C*y -> K*(-x) + C*y = 1

        long s0 = 1, t0 = 0, r0 = K;
        long s1 = 0, t1 = 1, r1 = C;

        long temp;
        while (r1 != 0) {
            long q = r0 / r1;

            temp = r0 - q*r1; // r0 % r1
            r0 = r1;
            r1 = temp;

            temp = s0 - q*s1;
            s0 = s1;
            s1 = temp;

            temp = t0 - q*t1;
            t0 = t1;
            t1 = temp;
        }

        return t0;
    }

    static EGResult egcd(long a, long b) {
        long s0 = 1, t0 = 0, r0 = a;
        long s1 = 0, t1 = 1, r1 = b;

        long temp;
        while (r1 != 0) {
            long q = r0 / r1;

            temp = r0 - q*r1; // r0 % r1
            r0 = r1;
            r1 = temp;

            temp = s0 - q*s1;
            s0 = s1;
            s1 = temp;

            temp = t0 - q*t1;
            t0 = t1;
            t1 = temp;
        }
        return new EGResult(s0, t0, r0);
    }


}

class EGResult {
    long s;
    long t;
    long r;

    public EGResult(long s, long t, long r) {
        this.s = s;
        this.t = t;
        this.r = r;
    }

    @Override
    public String toString() {
        return "EGResult{" +
                "s=" + s +
                ", t=" + t +
                ", r=" + r +
                '}';
    }
}