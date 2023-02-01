package P11279;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static int N;
    static int cnt;
    static int[] heap;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        heap = new int[N+1];

        int x;
        for (int i = 0; i < N; i++) {
            x = Integer.parseInt(br.readLine());
            if (x > 0) {
                insert(x);
            } else {
                System.out.println(delete());
            }

        }

    }

    static void insert(int x) {
        heap[++cnt] = x;

        int index = cnt, current, parent;
        while(index > 1){
            current = heap[index];
            parent = heap[index/2];
            if(parent < current){
                heap[index] = parent;
                heap[index/2] = current;
            } else {
                break;
            }
            index /= 2;
        }

    }

    static int delete() {
        if(cnt == 0){
            return 0;
        }

        int max = heap[1];

        heap[1] = heap[cnt--];

        int index = 1, current, child1, child2 = 0, currentMax;
        while (2*index <= cnt) {
            current = heap[index];
            child1 = heap[2*index];
            child2 = 0;
            if(2*index+1 <= cnt) {
                child2 = heap[2*index+1];
            }

            currentMax = Math.max(current, Math.max(child1, child2));
            if (currentMax == current) {
                break;
            } else if (currentMax == child1) {
                heap[index] = child1;
                heap[2*index] = current;
                index = 2*index;
            } else {
                heap[index] = child2;
                heap[2*index+1] = current;
                index = 2*index+1;
            }

        }

        return max;
    }
}


class MaxHeap {
    List<Integer> list;

    public MaxHeap() {
        list = new ArrayList<>(100001);
        list.add(0);
    }

    public void insert(int val) {
        // 1. 마지막에 추가
        list.add(val);
        // 2. 부모랑 조건 비교, 교환
        int current = list.size()-1;
        int parent = current/2;
        while (true) {
            // 1. current가 root면 탈출
            // 2. 부모, 자식 조건을 만족하면 탈출
            if (parent == 0 || list.get(parent) >= list.get(current)) {
                break;
            }

            int temp = list.get(parent);
            list.set(parent, list.get(current));
            list.set(current, temp);

            current = parent;
            parent = current / 2;
        }
    }

    public int delete() {
        // 1. root 제거
        int top = list.get(1);
        // 2. 마지막 노드를 root로 이동
        list.set(1, list.get(list.size()-1));
        list.remove(list.size()-1);

        // 3. 왼쪽, 오른쪽 중 조건이 안맞는 것을 선택 후 조건에 맞게 SWAP
        int currentNode = 1;
        while(true) {
            int leftNode = currentNode*2;
            int rightNode = currentNode*2 + 1;

            if(leftNode >= list.size()) {
                break;
            }

            int targetValue = list.get(leftNode);
            int targetNode = leftNode;

            if (rightNode < list.size() && targetValue < list.get(rightNode)) {
                targetNode = rightNode;
                targetValue = list.get(rightNode);
            }

            if (list.get(currentNode) < targetValue) {
                int temp = list.get(currentNode);
                list.set(currentNode, list.get(targetNode));
                list.set(targetNode, temp);
                currentNode = targetNode;
            } else {
                break;
            }
        }

        return top;
   }
}