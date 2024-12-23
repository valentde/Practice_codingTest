//2024-05-02
//[최고의 13위치 2 ](https://www.codetree.ai/missions/5/problems/best-place-of-13-2)
/*
    4중loop
    1x3 직사각형이 같은 행에 있지않다는 전제
*/

public class CT2_601_15to16 {
    static int G[][];

    public static void main(String[] args) {
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int n = sc.nextInt();
        G = new int[n][n];
        for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) G[i][j] = sc.nextInt();

        int ansMaxCoins = 0;
        for (int i = 0; i < n; i++) for (int j = 0; j < (n - 2); j++) {
                for (int k = i + 1; k < n; k++) for (int l = 0; l < (n - 2); l++) {
                        int cnt = G[i][j] + G[i][j + 1] + G[i][j + 2];
                        cnt += G[k][l] + G[k][l + 1] + G[k][l + 2];
                        if (ansMaxCoins < cnt)
                            ansMaxCoins = cnt;
                    }

            }
        System.out.println(ansMaxCoins);
    }


//[특정 수와 근접한 합 ](https://www.codetree.ai/missions/5/problems/sum-close-to-particular-number)
    private static int pick2ToMinus(int[] arr, int sum, int S, int twoSum, int k, int index) {
        if (k == 0) {
            return Math.abs(sum - twoSum - S);
        }

        int retMin=S;
        for (int i = index; i < arr.length; i++) {
            int retAbs = pick2ToMinus(arr, sum, S, twoSum + arr[i], k - 1, i + 1);
            if(retMin > retAbs)
                retMin = retAbs;
        }

        return retMin;
    }
    public static void main(String[] args) {
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int n=sc.nextInt(), s=sc.nextInt();
        int arr[] = new int[n], sum=0;
        for (int i = 0; i < n; i++)
            sum += arr[i] = sc.nextInt();

        System.out.println(pick2ToMinus(arr, sum, s, 0, 2, 0));



    }

}
