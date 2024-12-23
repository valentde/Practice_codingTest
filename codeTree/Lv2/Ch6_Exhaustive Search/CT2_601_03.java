//2024-04-20
// [일렬로 서있는 소 2 ](https://www.codetree.ai/missions/5/problems/cattle-in-a-rowing-up-2)
import java.util.Arrays;
import java.util.Scanner;

public class CT2_601_03 {
    static int[] A;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        A = new int[n];
        for (int i = 0; i < n; i++) A[i] = sc.nextInt();

        System.out.println(countCombinePick3(n, new int[3], 0, 0));
    }

    private static int countCombinePick3(int n, int[] bucket, int bi, int index) {
        if (bi == 3){
//            if(bucket[0] > bucket[1]) return 0;
//            if(bucket[0] > bucket[2]) return 0;
//            if(bucket[1] > bucket[2]) return 0;
            if (bucket[0] <= bucket[1] && bucket[1] <= bucket[2]) return 1;
//            System.out.println(Arrays.toString(bucket));
            return 0;
        }

        int retCount =0;
        for (int i = index; i < n; i++) {
//            bucket[bi] = i;
            bucket[bi] = A[i];
            retCount += countCombinePick3(n, bucket, bi + 1, i+1);
//            bucket[bi] = -1;
        }
        return retCount;
    }
}