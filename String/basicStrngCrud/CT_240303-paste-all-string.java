// [문자열 전부 붙이기 ](https://www.codetree.ai/missions/4/problems/paste-all-string)
import java.util.Scanner;
import java.util.StringJoiner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] str = new String[10];
        String strAll = "";
        int n = sc.nextInt();

        for(int i = 0; i < n; i++) str[i] = sc.next();

        StringBuilder sb = new StringBuilder();
        StringJoiner joiner = new StringJoiner("");

        for(int i = 0; i < n; i++)
            strAll += str[i];                         160ms
            strAll = String.join("", strAll, str[i]); 142, 172ms
            joiner.add(str[i]);                       144ms
            sb.append(str[i]);                        144, 139, 167ms
        
        System.out.println(strAll);
        System.out.println(joiner.toString());
    }
}