
public class CT_240424_0601_07-11 {

// [마라톤 중간에 택시타기 2 ](https://www.codetree.ai/missions/5/problems/taking-a-taxi-in-the-middle-of-the-marathon-2)
    public static void main(String[] args) {
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int n = sc.nextInt();
        int[][] checkPoints = new int[n][2];
        for (int i = 0; i < n; i++) {
            checkPoints[i][0]=sc.nextInt();
            checkPoints[i][1]=sc.nextInt();
        }

        //Manhattan Distance = |x1-x2| + |y1-y2|
        int sum=Integer.MAX_VALUE;
        for (int skipPoint = 1; skipPoint < n - 1; skipPoint++) {
            int dist=0;
            int prevX=checkPoints[0][0], prevY=checkPoints[0][1];
            for (int i = 1; i < n; i++) {
                if(i == skipPoint) continue;
                int nowX = checkPoints[i][0], nowY=checkPoints[i][1];
                dist += Math.abs(nowX - prevX) + Math.abs(nowY - prevY);
                prevX = nowX;
                prevY = nowY;
            }
            if(sum > dist)
                sum = dist;
        }
        System.out.println(sum);
    }
// [원 모양으로 되어있는 방 ](https://www.codetree.ai/missions/5/problems/a-room-in-a-circle)
/*
     한방향 거리세기
     i - 기준점
     i - 기준점 + size(역방향이라 음수)
*/
    public static void main(String[] args) {
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int n = sc.nextInt(), people = 0;
        int[] rooms = new int[n];
        for (int i = 0; i < rooms.length; i++) people += rooms[i] = sc.nextInt(); // 누적합 & 입력 동시

        int ansMinDist = 10000003;
        for (int start = 0; start < n; start++) {
            int sum=0;
            for (int i = 0; i < n; i++) {
                if(i < start) sum += rooms[i] * (i - start + n);
                if(i > start) sum += rooms[i] * (i - start);
            }
            if(ansMinDist > sum)
                ansMinDist = sum;
        }
        System.out.println(ansMinDist);
    }
// [괄호 쌍 만들어주기 2 ](https://www.codetree.ai/missions/5/problems/pair-parentheses-2)
/*
    2개연속 괄호 쌍 경우의 수 (( )) : 내부 loop 시작인덱스 초기화, if indexing
     + 연속한 닫는 괄호 두 개
 */
    public static void main(String[] args) {
        char[] c = new Scanner(System.in).nextLine().toCharArray();

        int ansCount = 0;

/*
        for (int i = 0; i < c.length; i++)
            if (c[i] == '(')
                for (int j = i+1; j < c.length; j++)
                    if (c[j] == '(')
                        for (int k = j+1; k < c.length; k++)
                            if (c[k] == ')')
                                for (int l = k+1; l < c.length; l++)
                                    if (c[l] == ')') ++ansCount;
*/

        for (int i = 0; i < c.length - 3; i++) {
            if (c[i] == '(' && c[i + 1] == '(')
                for (int j = i + 2; j < c.length - 1; j++) {
                    if (c[j] == ')' && c[j + 1] == ')')
                        ++ansCount;
                }

        }
        System.out.println(ansCount);
    }
// [인접하지 않은 2개의 숫자 ](https://www.codetree.ai/missions/5/problems/two-non-adjacent-numbers)
// 단순합 문제인데 누적합으로 잘못 풀음
    public static void main(String[] args) {
        java.util.Scanner sc = new java.util.Scanner(System.in);

        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int ansMax = 0;
        // for문
        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 2; j < n; j++) {
                int sum = arr[i] + arr[j];
                if (ansMax < sum)
                    ansMax = sum;
            }
        }
        System.out.println(ansMax);
    }

// [씨 오 더블유 2 ](https://www.codetree.ai/missions/5/problems/c-o-w-2)
/*
    재귀함수 combine 실수
        for (int i = index + 1; i < c.length; i++) { i=0 초기값 넘겨버리는 문제
    item 개수적어서 if문 처리
*/
    public static void main(String[] args) {
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int n = sc.nextInt();sc.nextLine();
        char[] c = sc.nextLine().toCharArray();
//        char[] cow = {'C', 'O', 'W'};
        System.out.println(countCows(c, 0, 3));
    }

    private static int countCows(char[] c, int index, int bi) {
        if (bi == 0) {
            return 1;
        }
        int retCount=0;

        for (int i = index; i < c.length; i++) {
            if(bi==3 && c[i] == 'C') retCount += countCows(c, i + 1, bi-1);
            if(bi==2 && c[i] == 'O') retCount += countCows(c, i + 1, bi-1);
            if(bi==1 && c[i] == 'W') retCount += countCows(c, i + 1, bi-1);
        }
        return retCount;
    }

}
