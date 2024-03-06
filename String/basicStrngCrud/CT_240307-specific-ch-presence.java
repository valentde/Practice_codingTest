// [특정 문자의 유무 ](https://www.codetree.ai/missions/4/problems/specific-character-presence)
public class Main {
    public static void main(String[] args) {
//          String input = new java.util.Scanner(System.in).nextLine();
         String input = new java.util.Scanner(System.in).nextLine().split(" ");

         System.out.format("%s ", input.contains("ee") ? "Yes" : "No");
         System.out.format("%s",input.contains("ab") ? "Yes" : "No");
    }
}

// [문자열의 특정 위치 찾기 ](https://www.codetree.ai/missions/4/problems/find-specific-location-in-spring)
/*
    string, a = tuple(input().split())
    let [str, a]  = require('fs').readFileSync(0).toString().trim().split(" ")
 */
public class Main {
    public static void main(String[] args) {
        String[] s = new java.util.Scanner(System.in).nextLine().split(" ");
        int indexOf = s[0].indexOf(s[1]);
        System.out.println(indexOf != -1 ? indexOf : "No" );
    }
}