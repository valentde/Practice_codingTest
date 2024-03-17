public class Main {

// [a로 채워넣기 ](https://www.codetree.ai/missions/4/problems/filling-with-a)
    public static void main(String[] args) {
        String input = new java.util.Scanner(System.in).next();
        char[] charr = input.toCharArray();
        charr[1] = charr[charr.length -2]= 'a';
        String valueof = String.valueOf(charr);
        System.out.println(valueof);
    }
// [문자 교체하기 ](https://www.codetree.ai/missions/4/problems/changing-char)
    public static void main(String[] args) {
        String[] starr = new java.util.Scanner(System.in).nextLine().split(" ");

        StringBuilder sbd = new StringBuilder(starr[1]);
        sbd.replace(0, 2, starr[0].substring(0, 2));

        System.out.println(sbd.toString());
    }
// [첫 번째와 두 번째 교환 ](https://www.codetree.ai/missions/4/problems/exchange-1st-and-2nd)
    public static void main(String[] args) {
        String str = new java.util.Scanner(System.in).nextLine();

        char c1 = str.charAt(0), c2 = str.charAt(1);
        char[] charr = str.toCharArray();
        for (int i = 0; i <charr.length; i++) {
            char c = charr[i];
            if(c == c1) charr[i] = c2;
            if(c == c2) charr[i] = c1;
        }
        System.out.println(String.valueOf(charr));
    }
}