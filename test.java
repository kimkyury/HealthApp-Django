
import java.util.*;

class Main {
    public String solution (String str){
        String answer = "";
        int max = Integer.MIN_VALUE, pos;

        while((pos = str.indexOf(' '))!= -1){ // 띄어쓰기의 위치를 반환
            String tmp = str.substring(0, pos);
            int len = tmp.length();
            if (len > max) {
                max = len;
                answer = tmp;
            }
            str = str.substring(pos+1);
        }
    
        /*
        String [] s = str.split(" ");
        
        int len;
        for(String x : s){
            len = x.length();
            if ( max < len)
                max = len;
                answer = x;
        }
        */
        return answer; 
    }
    public static void main (String [] args){
        Main T = new Main();
    
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();

        System.out.print(T.solution(str));
    }
}