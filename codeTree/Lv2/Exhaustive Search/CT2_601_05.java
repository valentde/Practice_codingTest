//2024-04-19
// [체크판위에서 2 ](https://www.codetree.ai/missions/5/problems/on-the-checkboard-2)
import java.util.Scanner;
/*
    자바 String[] → char[]      변환
    자바 String[] → Cahracter[] 변환
*/
public class CT2_601_05 {
    static String[][] G;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int r=sc.nextInt(), c = sc.nextInt(); sc.nextLine();
        G = new String[r][c];
        for (int i = 0; i < r; i++) for (int j = 0; j < c; j++) G[i][j] = sc.next();

        System.out.println(countJump4(r, c, 0, 0, 4));
    }

    private static int countJump4(int row, int col, int r, int c, int times) {
        if(times ==1){
            if(r==row-1 && c==col-1) return 1;
            return 0;
        }
        // (1,1) ~ 2군데 ~ (r, c) 도착
        String flagColor = G[r][c];

        int retCount=0;
        for (int i = r + 1; i < row; i++) {
            for (int j = c + 1; j < col; j++) {
                if(G[i][j].equals(flagColor)) continue;
                retCount += countJump4(row, col, i, j, times - 1);
            }
        }
        return retCount;
    }
}