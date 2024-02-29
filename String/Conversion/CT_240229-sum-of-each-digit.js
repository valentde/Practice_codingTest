// [각 자리 숫자들의 합 ](https://www.codetree.ai/missions/4/problems/sum-of-each-digit)
let n = Number(require('fs').readFileSync(0).toString().trim().split(` `))
let sum =0
let str = n.toString()
for(let i=0; i<str.length; i++)
    sum += Number(str[i])

console.log(sum)

// [두 수의 합과 1 ](https://www.codetree.ai/missions/4/problems/two-nums-sum-and-1)
let [n, m] = require('fs').readFileSync(0).toString().trim().split(` `).map(Number)
let sum = n + m
let str = sum.toString(), count=0
for(let i=0; i<str.length; i++)
    if(str[i] == '1') count++;

console.log(count)