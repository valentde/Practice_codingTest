// [대각선으로 숫자 채우기 ](https://www.codetree.ai/missions/4/problems/diagonal-numbering)

// while내부 값 대입 2번 → 1번 줄이기
// Array.from(Array(n), () => Array(m).fill(0)
// Array(n).fill(0).map( () => Array(m).fill(0) )

const [n, m] = require('fs').readFileSync(0).toString().trim().split(' ').map(Number)
let matrix = Array(n).fill(0).map( () => Array(m).fill(0) )
let num=1

for(let col=0; col<m; col++){
    let r=0, c=col
    matrix[r][c] = num++

    while(c-1>=0 && r+1<n){
        --c
        ++r
        matrix[r][c] = num++
    }
}

// 마지막열에서 아래쪽으로
for(let row=1; row<n; row++){
    let r=row, c=m-1
    matrix[r][c] = num++
    while(c-1>=0 && r+1<n){
        --c
        ++r
        matrix[r][c] = num++
    }
}

for(let r=0; r<n; r++){    
    str = ``
    for(let c=0; c<m; c++) str += matrix[r][c] + ' '
    console.log(str)
}