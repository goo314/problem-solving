package DAY01.P1759;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static int L, C;
    static char[] input;
    static boolean[] visited;
    static int selectedCount;
    public static void main(String[] args) throws FileNotFoundException {
        System.setIn(new FileInputStream("src/DAY01/P1759/input.txt"));

        Scanner sc = new Scanner(System.in);

        L = sc.nextInt();
        C = sc.nextInt();

        input = new char[C];
        for (int i = 0; i < C; i++) {
            input[i] = sc.next().charAt(0);
        }

        Arrays.sort(input);

        visited = new boolean[26];

        for (int i = 0; i < C; i++) {
            dfs(i);
        }

//        sol(-1, 0, 0, 0, "");

    }

    static void dfs(int index){
        // 1. 체크인
        int idx = input[index]-'a';
        visited[idx] = true;
        selectedCount++;

        // 2. 목적지인가? -> length
        if(selectedCount == L){
            printPassword();
        } else {
            // 3. 연결된 곳 순회 -> index+1 ~ C
            for (int i = index+1; i < C; i++) {
                // 4. 갈 수 있는 가? -> x
                // 5. 간다.
                dfs(i);
            }
        }

        // 6. 체크아웃
        visited[idx] = false;
        selectedCount--;
    }

    static void printPassword(){
        boolean isPassword = false;
        int numConsonant = 0;
        int numVowel = 0;
        String password = "";

        for (int i = 0; i < 26; i++) {
            if(visited[i] == true){
                password += (char) (i + 'a');
                if (i==('a'-'a') || i==('e'-'a') || i==('i'-'a') || i==('o'-'a') || i==('u'-'a')) {
                    numConsonant++;
                } else {
                    numVowel++;
                }
            }
        }

        if(numConsonant>=1 && numVowel>=2){
            isPassword = true;
        }

        if(isPassword){
            System.out.println(password);
        }

    }

    static void sol(int current, int length, int ja, int mo, String pwd){
        // 1. 체크인 - 생략가능

        // 2. 목적지인가 length == L -> 자, 모 개수
        if(length == L){
            if(ja >= 2 && mo >= 1){
                System.out.println(pwd);
            }
        } else {
            // 3. 연결된 곳을 순회 current ~ C
            for (int i = current+1; i < C; i++) {
                // 4. 갈 수 있는가? - 생략 가능
                // 5. 간다 - 자, 모
                if(input[i] == 'a' || input[i]=='e' || input[i]=='e' || input[i]=='o' || input[i]=='u'){
                    sol(i, length+1, ja, mo+1, pwd+input[i]);
                } else {
                    sol(i, length+1, ja+1, mo, pwd+input[i]);
                }
            }
        }

        // 6. 체크아웃

    }
}
