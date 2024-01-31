// [중복되지 않는 숫자 중 최대 ](https://www.codetree.ai/missions/4/problems/max-of-unique-number)
// Count ing  배열 (중복횟수)
let i = require('fs').readFileSync(0).toString().trim().split('\n')
let n = Number(i[0])
let arr = i[1].split(' ').map(Number)

let countArr = Array(1001).fill(0) 
for (let e of arr) countArr[ e ]++

//내풀이 0부터 ---> (다른답) 뒤에서부터 forr ---> break
let ansMax = -1
for(let i=0; i<1002; i++){
    if(countArr[i] ==1)
        if(ansMax < i) 
            ansMax = i
}

console.log(ansMax)