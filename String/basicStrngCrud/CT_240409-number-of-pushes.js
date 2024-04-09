// [미는 횟수 ](https://www.codetree.ai/missions/4/problems/number-of-pushes)
let [a, b] = require('fs').readFileSync(0).toString().trim().split("\n")
let len=a.length, n=1;

while(n < len){
    //배열 오른쪽으로 밀기
    a = a.slice(-1) + a.slice(0, len-1)
    // let back = a.slice(-1)
    // for(let i=len-1; i>0; i--) a[i] = a[i-1]
    // a[0] = back

    if(a === b) break;
    ++n;
}

console.log(n == len ? -1 : n)

// [문자열의 개수 ](https://www.codetree.ai/missions/4/problems/number-of-spring)
// 문자열의 개수와 홀수번째 문자열 출력
const input = require('fs').readFileSync(0).toString().trim().split("\n")
let cntStr=0
let oddS = ''

while(input[cntStr++] !== '0'){
    if(cntStr %2 ===1) oddS += input[cntStr - 1] + "\n"
}
console.log(cntStr - 1);
console.log(oddS);

const input = require('fs').readFileSync(0).toString().trim().split('\n')
