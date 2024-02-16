# [공백을 기준으로 출력 ](https://www.codetree.ai/missions/4/problems/output-based-on-space)

## 쥴단위 → 공백구분 후처리 (함수 대신 loop-if)
# if(str1[i] !== " ")
# if (str[i] != ' ')
# if (str[i] != ' ' & & str[i] != '\n')
# if(str.charAt(i) != ' ')
line1 = input()
line2 = input()

for w in line1.split():
    print(w, end='')
for w in line2.split():
    print(w, end='')

##  (JS) [문장1, 문장2] 배열 익숙 해지기
#        [문장, 문자1개] 배열 익숙 해지기
# let input =  require("fs").readFileSync(0).toString().trim().split("\n")
# let [str, a] = input;
# let [str1, str2] = input;

# [문자 개수 세기 ](https://www.codetree.ai/missions/4/problems/count-char)
line = input()
c = input()\

print(line.count(c))

# [문자열 범위 출력하기 ](https://www.codetree.ai/missions/4/problems/print-string-in-range)

### C++도 prnitf 사용함
# char str[101];
# fgets(str, 101, stdin);
# for(int i = 2; i < 10; i++) printf("%c", str[i]);
#
# string str;
# getline(std::cin, str);
# for(int i = 2; i < 10; i++) printf("%c", str[i]);
str = input()
print(str[2:10])