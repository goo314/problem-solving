// TODO: sort people by rank and use Indexed tree
package DAY03.P2517;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int N;
    static int s;
    static int[] tree;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        s = 1;
        while (s < N) {
            s *= 2;
        }

        tree = new int[2*s];
        for (int i = 0; i < N; i++) {

        }

    }
}
