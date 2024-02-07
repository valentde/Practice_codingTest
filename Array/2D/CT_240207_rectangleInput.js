let inputSplited = require('fs').readFileSync(0).toString().trim().split(' ')
let [n, m] = inputSplited.map(Number)

// 2차원 배열 Define
let arr2d = Array(n).fill(0).map( () => Array(m).fill(0) )

// 2차원 배열 Input
let num=1
for(let i=0; i<n; i++) for(let j=0; j<m; j++) arr2d[i][j] = num++

// 2차원 배열 Print -forEach
for(let row of arr2d){
    let str=``
    for(let e of row){
        str += e + ' '
    }
    console.log(str)
}