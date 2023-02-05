package DAY01.P1713;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.*;

public class Main {
    static int N,K;
    static Person[] people;
    static int[] inputs;
    public static void main(String[] args) throws FileNotFoundException {
        System.setIn(new FileInputStream("src/DAY02/BOJ1713/input.txt"));
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        K = sc.nextInt();

        inputs=new int[K];
        people = new Person[101];

        List<Person> list = new ArrayList<>();
        for (int i = 0; i < K; i++) {
            int num = sc.nextInt();
            if(people[num]==null){
                people[num] = new Person(num, 0, 0, false);
            }
            if(people[num].isIn==true){
                people[num].count++;
            }else{
                if(list.size()==N){
                    Collections.sort(list);
                    Person removeTarget = list.remove(N - 1);
                    removeTarget.isIn=false;
                    removeTarget.count=0;
                }
                people[num].count=1;
                people[num].isIn=true;
                people[num].timestamp=i;
                list.add(people[num]);
            }
        }
        Collections.sort(list, new Comparator<Person>() {
            @Override
            public int compare(Person o1, Person o2) {
                return o1.num-o2.num;
            }
        });
        for (int i = 0; i < list.size(); i++) {
            System.out.print(list.get(i).num);
            System.out.print(" ");
        }
        System.out.println();
    }
}

class Person implements Comparable<Person>{
    int num;
    int count;
    int timestamp;
    boolean isIn;

    public Person(int num, int count, int timestamp, boolean isIn) {
        this.num = num;
        this.count = count;
        this.timestamp = timestamp;
        this.isIn = isIn;
    }

    @Override //빼야할 후보자를 제일 끝으로 보냄
    public int compareTo(Person o2) {
        int comp1=o2.count-count;
        if(comp1==0){
            return o2.timestamp-timestamp;
        }
        return comp1;
    }
}