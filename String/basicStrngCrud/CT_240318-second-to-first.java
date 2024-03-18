// [두 번째를 첫 번째로 ](https://www.codetree.ai/missions/4/problems/second-to-first)
public class Main {
    public static void main(String[] args) {
    String str = new java.util.Scanner(System.in).next();
    str = str.replace(str.charAt(1), str.charAt(0));
    System.out.println(str);
    }

/*
    다른풀이
문자열을 순회하면서 두 번째 문자를 첫 번째 문자로 교환합니다.
for i in range(len(string)):
	if string[i] == b:
		string = string[:i] + a + string[i + 1:]


*/
}