// [문자열 거꾸로 출력하기 ](https://www.codetree.ai/missions/4/problems/print-string-backward)
const input = require('fs').readFileSync(0).toString().trim().split('\n')

for (let str of input){
    if(str === 'END') break;
    let s =''
    let len = str.length
    for(let i=len -1; i>=0; i--) s += str[i]
/*
    이중for문이면  str += input[i][j];
    .split('').reverse().join('')

    new StringBuilder(word).reverse();
*/
    console.log(s)
}

// [일치하는 문자열의 수 ](https://www.codetree.ai/missions/4/problems/num-of-correct-string)
/*
n, str = input().split()
n = int(n)
cnt=0
for _ in range(n):
    if str == input():
        cnt += 1
print(cnt)
*/
