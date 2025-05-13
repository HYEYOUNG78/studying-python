import java.util.*;

class Solution {
    public ArrayList<String> solution(String[] strArr) {
        ArrayList<String> answer = new ArrayList<>();
        for(int i = 0; i < strArr.length; i++) {
            if(i % 2 != 0){
                answer.add(strArr[i].toUpperCase());   
            } else {
                answer.add(strArr[i].toLowerCase());   
            }
        };
        return answer;
    }
}