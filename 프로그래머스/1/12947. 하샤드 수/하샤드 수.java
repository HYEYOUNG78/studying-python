import java.util.*;

class Solution {
    public boolean solution(int x) {
        int num = x;
        ArrayList<Integer> list = new ArrayList<>();
        
        while(num > 0) {
            list.add(num % 10);
            num /= 10;
        }
        
        int sum = list.get(0);
        for(int i = 1; i < list.size(); i++) {
            sum += list.get(i);
        }
        
        if(x % sum != 0) {
            return false;
        }
        return true;
    }
}