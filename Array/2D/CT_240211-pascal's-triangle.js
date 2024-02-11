// [파스칼의 삼각형 ](https://www.codetree.ai/missions/4/problems/pascal's-triangle)

// 전체 0 초기화 -- 첫열과 중간 자리 1 재 초기화 - 파스칼
// for (let i = 0; i < n; i++) { arr[i][0] = 1; arr[i][i] = 1; }

const n = Number(require('fs').readFileSync(0).toString().trim())
let matrix = Array(n).fill(1).map( () => Array(n).fill(1))


for(let i=0; i<n; i++) for(let j=i+1; j<n; j++) matrix[i][j] =0

for(let i=1; i<n; i++){
     for(let j=1; j<=i; j++)
        matrix[i][j] = matrix[i - 1][j - 1] + matrix[i - 1][j];
}

for(let i=0; i<n; i++){
    str=``
    for(let j=0; j<=i; j++)
        str += matrix[i][j] + ` `
    console.log(str)
}


// [격자로 사각형 만들기 ](https://www.codetree.ai/missions/4/problems/print-grid-in-rectangle)
const n = Number(require('fs').readFileSync(0).toString().trim())
let matrix = Array(n).fill(0).map( () => Array(n).fill(0))


for(let i=0; i<n; i++) matrix[i][0] =1
for(let j=0; j<n; j++) matrix[0][j] =1


for(let i=1; i<n; i++){
     for(let j=1; j<n; j++)
        matrix[i][j] = matrix[i - 1][j - 1] + matrix[i - 1][j] + matrix[i][j - 1];
}

for(let i=0; i<n; i++){
    str=``
    for(let j=0; j<n; j++)
        str += matrix[i][j] + ` `
    console.log(str)
}

// [배열로 사각형 만들기 ](https://www.codetree.ai/missions/4/problems/print-array-in-rectangle)
const n = Number(require('fs').readFileSync(0).toString().trim())
let count=1 , j=n-1
let matrix = Array(5).fill(1).map( () => Array(5).fill(1))

for(let i=1; i<5; i++){
     for(let j=1; j<5; j++)
        matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1];
}

for(let row of matrix){
    str=``
    for(let v of row)
        str += v + ` `
    console.log(str)
}