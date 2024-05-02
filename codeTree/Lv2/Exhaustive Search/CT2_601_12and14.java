//2024-04-29
// [Carry 피하기 2 ](https://www.codetree.ai/missions/5/problems/escaping-carry-2)
/*
    예제 [522, 6, 7311]는 isCarry 해당외는데 1개밖에 없어서 테케에서 막히 수 있음
*/
import java.util.Arrays;

public class CT2_601_12and14 {

    public static void main(String[] args) {
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int n = sc.nextInt();
        int[] num = new int[n];
        for (int i = 0; i < n; i++) num[i] = sc.nextInt();

        int maxSum = combine3num(num, n, 3, new int[3], 0, -1);
        System.out.println(maxSum);
    }

    private static int combine3num(int[] num, int n, int k, int[] bucket, int index, int paraSum) {
        if (k == 0) {
            if( ! isCarry(bucket)) return -1;
/*          carry 계산 기존최댓값(para) 과 비교는 밖에서 하겠지머...
            int sum=0; if(paraSum < sum) paraSum = sum;
*/
            return bucket[0] + bucket[1] + bucket[2];
        }

        for (int i = index; i < n; i++) {
            bucket[bucket.length - k]  = num[i];
//            bucket[bucket.length - k]  = i;
            int retSum = combine3num(num, n, k - 1, bucket, i + 1, -1);
            if(paraSum < retSum)
                paraSum = retSum;
        }
        return paraSum;
    }

    private static boolean isCarry(int[] n) {
        int a=n[0], b=n[1], c=n[2];
        while (a > 0 || b > 0 || c > 0) {
            int r1=a%10, r2=b%10, r3=c%10;
            if(r1+r2+r3 >= 10) return false;
            a /= 10;
            b /= 10;
            c /= 10;
        }
//        System.out.println(Arrays.toString(n));
        return true;
    }

// [숨은 단어 찾기 2 ](https://www.codetree.ai/missions/5/problems/find-hidden-words-2)
    static int n, m, dir[][] = {{-1,-1}, {-1,0}, {-1,1}, {0,1}, {1,1}, {1,0}, {1,-1}, {0,-1}};
    static char[][] G;
    private static int countLeeWithDirection(int r, int c, int direction, int k) {
        if(k==0) return 1;

        int retCnt=0;
        for (int i = 0; i < dir.length; i++) {
            int nr = r+dir[i][0], nc=c+dir[i][1];
            if(nr<0 || nc<0 || nr>=n || nc>= m) continue;
            if(k == 2 && G[nr][nc] == 'E') retCnt += countLeeWithDirection(nr, nc,  i, k - 1);
            if(k == 1 && G[nr][nc] == 'E' && direction == i) retCnt += countLeeWithDirection(nr, nc,  i, k - 1);
        }

        return retCnt;
    }
    public static void main(String[] args) {
        java.util.Scanner sc = new java.util.Scanner(System.in);
        n=sc.nextInt();
        m=sc.nextInt();
        sc.nextLine();
        G = new char[n][m];
        for (int i = 0; i < n; i++) G[i] = sc.nextLine().toCharArray();

        int ansCnt=0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if(G[i][j] == 'L')
                    ansCnt += countLeeWithDirection(i, j, -1, 2);
            }
        }
        System.out.println(ansCnt);



    }
}