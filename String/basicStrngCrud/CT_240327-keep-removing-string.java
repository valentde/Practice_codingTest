import java.util.Scanner;

public class Main {
    // [문자열 계속 지우기 ](https://www.codetree.ai/missions/4/problems/keep-removing-string)
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next(), b = sc.next();
        while (a.contains(b)){
            int index = a.indexOf(b);
            int lenB = b.length();

            a = a.substring(0, index) + a.substring(index + lenB);
        }
        System.out.println(a);
    }


// [e 제거하기 ](https://www.codetree.ai/missions/4/problems/e-to-remove)
    public static void main(String[] args) {
        String s = new java.util.Scanner(System.in).next();
        int deleteIdx = s.indexOf('e');
        System.out.println(s.substring(0, deleteIdx)
                        + s.substring(deleteIdx+1));
    }

}