
import java.util.*;

 class Main {

    public String solution(String str) {
        String answer = "";

        int ascii;
        for(char c : str.toCharArray()){
            ascii = c;
            if ( ascii >= 97) 
                answer += Character.toUpperCase(c);
            else
                answer += Character.toLowerCase(c);
        }
        
        return answer;
    }

    public static void main(String [] args){
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        String str = kb.next();

        System.out.print(T.solution(str));
    }
}