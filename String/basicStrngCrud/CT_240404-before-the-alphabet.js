// [그 전 알파벳 ](https://www.codetree.ai/missions/4/problems/before-the-alphabet)
let c = require('fs').readFileSync(0).toString().trim();

// let minusAscii = c.charCodeAt(0) - 1;
// if(minusAscii == 'a'.charCodeAt(0) - 1)
//      minusAscii = 'z'.charCodeAt(0)

let printC  = 
    (c == 'a') ? 'z' : String.fromCharCode(c.charCodeAt(0) - 1)

console.log(printC);

// [그 다음 알파벳 ](https://www.codetree.ai/missions/4/problems/next-alphabet)
let ch = require('fs').readFileSync(0).toString()

let asciiNum = ch.charCodeAt(0) + 1;
if(asciiNum == 'z'.charCodeAt(0) + 1)
    asciiNum = 'a'.charCodeAt(0)
console.log(String.fromCharCode(asciiNum));

// [아스키코드의 합과 차 ](https://www.codetree.ai/missions/4/problems/sum-and-subtract-in-ASCII)
let [a, b] = require('fs').readFileSync(0).toString().trim().split(' ')
let asciiA = a.charCodeAt(0),asciiB = b.charCodeAt(0)

let minus= asciiA-asciiB;
if(minus <0) minus *= -1;
console.log("%d %d", asciiA+asciiB, minus)

// [아스키코드 변환 ](https://www.codetree.ai/missions/4/problems/convert-to-ascii)
// x, a = input().split()
let [a, b] = require('fs').readFileSync(0).toString().trim().split(' ')

// b = (Number) b
b = Number(b);

console.log(`${a.charCodeAt(0)} ${String.fromCharCode(b)}`)


// [아스키코드표 맞추기 ](https://www.codetree.ai/missions/4/problems/chart-of-ASCII)
let asciiArray = require('fs').readFileSync(0).toString().trim().split(' ').map(Number);
str =``
for (let a of asciiArray)  str += String.fromCharCode(a) + ' '
console.log(str);