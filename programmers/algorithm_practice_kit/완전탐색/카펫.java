import java.util.*;

class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        
        int n = brown + yellow;
        for(int i=3; i*i<=n; i++) {
            if(n%i != 0){
                continue;
            }
            int j = n / i;
            if (yellow == (i-2)*(j-2)) {
                answer[0] = j;
                answer[1] = i;
                break;
            }
        }
        
        return answer;
    }
}
