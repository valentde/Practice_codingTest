public class Main {
    public static void main(String[] args) {
        char[] chars = new java.util.Scanner(System.in).next().toCharArray();
        int countEe=0, countEb=0;
        // for문 2개보다 1개만 넣어서 내무에서 if로 해결
        for (int i = 0; i < chars.length -1; i++) if(chars[i]=='e' && chars[i+1]=='e') countEe++;
        for (int i = 0; i < chars.length -1; i++) if(chars[i]=='e' && chars[i+1]=='b') countEb++;

        System.out.format("%d %d", countEe, countEb);

    }
}