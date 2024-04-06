// [정수만 더하기 ](https://www.codetree.ai/missions/4/problems/add-only-integers)
let s = require('fs').readFileSync(0).toString().trim()

let sum=0
for (let e of s) if(e>='0' && e<='9') sum += e - '0'
console.log(sum)


// [대문자 소문자 바꾸기 ](https://www.codetree.ai/missions/4/problems/change-uppercase-and-lowercase)
let s = require('fs').readFileSync(0).toString().trim()
let ret=''

for(let e of s){
    // if(e>='A' && e<='Z') ret += e -'A'+'a'
    // if(e>='a' && e<='z') ret += e -'a'+'A'
    if(e>='A' && e<='Z') ret += e.toLowerCase()
    if(e>='a' && e<='z') ret += e.toUpperCase()

}

console.log(ret)