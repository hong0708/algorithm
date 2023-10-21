package programmers;

import java.util.*;

public class k번째수 {
    class Solution {
        public int[] solution(int[] array, int[][] commands) {
            int[] answer = new int[commands.length];

            for (int i = 0; i < commands.length; i++) {

                int[] impl = new int[commands[i].length];
                int loc = 0;
                for (int j = commands[i][0]; j <= commands[i][1]; j++) {
                    impl[loc] = array[j - 1];
                    loc += 1;
                }

                Arrays.sort(impl);
                answer[i] = impl[commands[i][2]];

            }

            return answer;
        }
    }
}
