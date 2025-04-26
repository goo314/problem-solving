import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int n = prices.length;
        int[] answer = new int[n];
        
        Stack<Integer> s = new Stack<>();
        s.push(0);
        
        for(int i=1; i<n; i++) {
            int price = prices[i];
            while (!s.isEmpty() && prices[i] < prices[s.peek()]) {
                answer[s.peek()] = i - s.peek();
                s.pop();
            }
            s.push(i);
        }
        
        while (!s.isEmpty()) {
            answer[s.peek()] = n-1-s.peek();
            s.pop();
        }
        
        return answer;
    }
}
