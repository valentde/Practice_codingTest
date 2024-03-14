/*
 pos +=1 인이유는 겹치는 부분도 부분문자열로 봄

 부분 문자여 개수 풀이법 3가지

 */import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String strA = sc.next();
        String strB = sc.next();

        int pos=0, ansCount=0;
        while ( (pos = strA.indexOf(strB, pos)) != -1){
//            pos += strB.length();
            ++pos;
            ++ansCount;
        }

        System.out.println(ansCount);


    }
}