// [두 문자열을 이어붙였을 때 ](https://www.codetree.ai/missions/4/problems/when-two-strings-are-concatenated)
let [a, b] = require('fs').readFileSync(0).toString().trim().split('\n')

let str1 = [a, b].join(``)
let str2 = [b, a].join(``)

console.log( `true` ? str1 === str2 : `false`)