import java.util.Scanner;
//484ms
public class BJ_240307_12891 {

/*
    DNA 문자열은 모든 문자열에 등장하는 문자가 {‘A’, ‘C’, ‘G’, ‘T’} 인 문자열
    부분분자열의 길이, 그리고 {‘A’, ‘C’, ‘G’, ‘T’} 가 각각 몇번 이상 등장해야 비밀번호로 사용할 수 있는지

    (1) dna.substring(i, i + lenP) 이용하면 시간소과
*/
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int lenS = sc.nextInt(), lenP = sc.nextInt();
        sc.nextLine();
        String dna = sc.nextLine().toLowerCase(); //소문자 변환
        int[] item = new int[]{sc.nextInt(), sc.nextInt(), sc.nextInt(), sc.nextInt()}; //a,c,g,t


        int ansCount = 0;
        char[] chArr = dna.toLowerCase().toCharArray(); //문자열 → char[] 문자배열
        int[] v = new int[4]; //a,c,g,t
        for (int i = 0; i < lenP; i++)
            v[getCharIndex(chArr[i])]++;

        for (int i = 0; i < lenS - lenP + 1; i++) {

            boolean isAllGreaterEqual = true;
            for (int j = 0; j < 4; j++)
                if (item[j] > v[j]) {
                    isAllGreaterEqual = false;
                    break;
                }
            if (isAllGreaterEqual)
                ansCount++;

            v[getCharIndex(chArr[i])]--;
//            v[ getCharIndex(chArr[i + lenP - 1])]++;
            if (i + lenP < lenS)
                v[getCharIndex(chArr[i + lenP])]++;
        }
        System.out.println(ansCount);
    }

    private static int getCharIndex(char c) {
        if (c == 'a') return 0;
        if (c == 'c') return 1;
        if (c == 'g') return 2;
        if (c == 't') return 3;
        return -1;
    }
}
