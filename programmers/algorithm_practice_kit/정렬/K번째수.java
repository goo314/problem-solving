import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int n = commands.length;
        int[] answer = new int[n];
        
        for(int c=0; c<n; c++) {
            int[] cmd = commands[c];
            int i=cmd[0]; int j=cmd[1]; int k=cmd[2];
            
            int[] tmp = Arrays.copyOfRange(array, i-1, j);
            Arrays.sort(tmp);
            answer[c] = tmp[k-1];
        }

        return answer;
    }
}
