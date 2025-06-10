package DAY01.P1713;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class MyMain {
    static int N, K;
    static People[] people;
    static People[] pictures;
    static int countPicture;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        K = sc.nextInt();

        countPicture = 0;
        people = new People[101];
        for (int i = 0; i < 101; i++) {
            people[i] = new People(i, 0, 0, false);
        }
        pictures = new People[N];
        for (int i = 0; i < K; i++) {
            int n = sc.nextInt();
            if(people[n].isIn == false){
                People p = new People(n, 1, i, true);
                if(countPicture == N){
                    Arrays.sort(pictures, new Comparator<People>() {
                        @Override
                        public int compare(People o1, People o2) {
                            int comp1 = o1.count - o2.count;
                            if(comp1 == 0){
                                return o1.timestamp - o2.timestamp;
                            } else {
                                return comp1;
                            }
                        }
                    });
                    people[pictures[0].num].isIn = false;
                    people[pictures[0].num].count = 0;
                    pictures[0] = p;
                } else {
                    pictures[countPicture] = p;
                    countPicture++;
                }
                people[n] = p;
            } else {
                people[n].count++;
            }
        }

        Arrays.sort(pictures, new Comparator<People>() {
            @Override
            public int compare(People o1, People o2) {
                return o1.num - o2.num;
            }
        });

        for (int i = 0; i < countPicture; i++) {
            System.out.print(pictures[i].num);
            System.out.print(" ");
        }
        System.out.println();

    }
}

class People {
    int num;
    int count;
    int timestamp;
    boolean isIn;

    public People(int num, int count, int timestamp, boolean isIn) {
        this.num = num;
        this.count = count;
        this.timestamp = timestamp;
        this.isIn = isIn;
    }

    @Override
    public String toString() {
        return "{" + num +
                ", " + count +
                ", " + timestamp +
                ", " + isIn +
                '}';
    }

}