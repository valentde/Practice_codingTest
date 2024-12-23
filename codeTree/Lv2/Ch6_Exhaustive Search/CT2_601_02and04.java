//2024-04-18
import java.util.Scanner;

public class CT2_601_02and04 {

    public static void main(String[] args) {
// [괄호 쌍 만들어주기 3 ](https://www.codetree.ai/missions/5/problems/pair-parentheses-3)
        char[] c = new Scanner(System.in).nextLine().toCharArray();
        int count=0;
        for (int i = 0; i < c.length; i++) {
            if(c[i] == ')') continue;
            for (int j = i + 1; j < c.length; j++) {
                if(c[j] == ')')
                    ++count;
            }
        }
        System.out.println(count);

// [최고의 13위치 ](https://www.codetree.ai/missions/5/problems/best-place-of-13)
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] G = new int[n][n];
        for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) G[i][j] = sc.nextInt();

        int max=0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - 2; j++) {
                int sum = G[i][j] + G[i][j+1] + G[i][j+2];
                if(max < sum) max = sum;
            }
        }
        System.out.println(max);
    }
}