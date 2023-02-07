// TODO: LCA memozation으로 구하기

package DAY06.p11438;
import java.io.*;
import java.util.*;

public class Main {
    static int[] dep = new int[100001];
    static int[] chk = new int[100001];
    static int[][] arr = new int[18][100001];
    static ArrayList<ArrayList<Integer>> adjList = new ArrayList<>();

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int i,j,n,m;

        st = new StringTokenizer(br.readLine());

        //N : 정점의 개수
        n = Integer.parseInt(st.nextToken());

        //N까지 인접리스트를 만들어 줌(초기화)
        for(i=0;i<=n;i++) {
            adjList.add(new ArrayList<>());
            chk[i] = 0;
        }

        //인접리스트 생성
        for(i=1;i<=n-1;i++) {
            int a, b;
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            adjList.get(a).add(b);
            adjList.get(b).add(a);
            //arr[0][b] = a;
        }

        //Depth(깊이)를 구하는 탐색
        getDepth(1,1);

        //i랑 j가 무엇을 뜻하는지?
        //2^i조상까지 구한다고 했었고
        //2^17까지 조상을 구해놓는다면 배열값이 부족하진 않겠구나
        for(i=1;i<=17;i++) {
            for(j=1;j<=n;j++) {
                //j의 2^i번째 조상을 dp로 구함
                arr[i][j] = arr[i-1][arr[i-1][j]];
            }
        }

        st = new StringTokenizer(br.readLine());
        //m이 쿼리의 개수
        m = Integer.parseInt(st.nextToken());

        for(i=1;i<=m;i++) {
            int a, b;
            int depa, depb;
            int temp;
            int ans;

            st = new StringTokenizer(br.readLine());
            //lca(a,b)
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());

            //a랑 b의 depth
            //dep이라는 배열에 depth가 들어가 있음
            depa = dep[a];
            depb = dep[b];

            //a를 감소시키면서 계산 진행할 것임
            //depth가 큰것을 a로 위치시킨다.
            //swap(a,b)
            if(depa < depb) {
                temp = depa;
                depa = depb;
                depb = temp;

                temp = a;
                a = b;
                b = temp;
            }

            //a와 b의 depth를 맞춘다.
            //a의 depth가 13이라고 하고
            //b의 depth가 2

            //a의 depth가 13
            //b의 depth가 2
            //j=3일때
            //2^3 = 8 (13 - 8) >= 2 // 8만큼 더 올라갈 수 있다
            //j=2일때
            //5, 2
            //2^2 = 4 (5 - 4) >= 2
            //j=1일때
            //2^1 = 2 (5 - 2) >= 2 // 2만큼 더 올라갈 수 있다
            //j=0일때
            //2^0 = 1 (3 - 1) >= 2 // 1만큼 더 올라갈 수 있다
            for(j=17;j>=0;j--) {
                //math.pow(a^b)
                //2^j을 가져오겠다.
                //a의 depth - 2^j >= b의 depth보다 클 경우
                if(depa - (int)Math.pow(2, j) >= depb) {
                    //depth 조절
                    depa = depa - (int)Math.pow(2, j);
                    //a의 j번째 조상
                    a = arr[j][a];
                }
                if(depa == depb) {
                    break;
                }
            }

            ans = a;

            //두 a,b를 같이 올리는거
            //depth를 7이라고 가정
            //a!=b
            //depa = 7, depb = 7
            //a!=b 2^3 = 8
            if(a!=b) {
                for(j=17;j>=0;j--) {
                    if(arr[j][a] != arr[j][b]) {
                        //a의 2^j번째 조상과 b의 2^j번째 조상이 같다면
                        //a와 b를 올리겠다
                        a = arr[j][a];
                        b = arr[j][b];
                    }
                    //올라가다 보면 LCA에 도달한다.
                    ans = arr[j][a];
                }
            }
            bw.write(ans + "\n");
        }
        bw.flush();
    }

    //탐색 method
    static void getDepth(int current, int depth) {
        int i, dest;
        //한번 방문한 곳은 방문하지 않음
        chk[current] = 1;

        //현재(current)점에 depth를 저장한다.
        dep[current] = depth;

        //인접리스트
        for(i=0;i<adjList.get(current).size();i++) {
            //adjList.get(current).size -> current점의 degree
            dest = adjList.get(current).get(i);
            //dest -> current 리스트의 i번째 원소
            //방문하지 않은 점일때
            if(chk[dest] == 0) {
                //dest 점의 직계조상은 current이다.
                arr[0][dest] = current;

                //DFS 진행
                getDepth(dest, depth+1);
            }
        }
    }

}
