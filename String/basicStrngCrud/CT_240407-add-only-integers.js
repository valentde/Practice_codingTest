// [정수만 더하기 ](https://www.codetree.ai/missions/4/problems/add-only-integers)
let s = require('fs').readFileSync(0).toString().trim()

let sum=0
for (let e of s){
    if(e>='0' && e<='9') sum += e - '0'
}

console.log(sum)