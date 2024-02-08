// [두 배열의 곱 ](https://www.codetree.ai/missions/4/problems/multiple-of-two-arrays)
const input = require("fs").readFileSync(0).toString().trim().split("\n");

let mat1 = Array(3).fill(0).map( () => Array(3).fill(0) )
let mat2 = Array(3).fill(0).map( () => Array(3).fill(0) )

for (let i = 0; i < 3; i++) mat1[i] = input[i].split(' ') .map(Number)
for (let i = 0; i < 3; i++) mat2[i] = input[i + 4].split(' ') .map(Number)


for (let i = 0; i < 3; i++){
    str = ``
    for (let j = 0; j < 3; j++)
        str += mat1[i][j] * mat2[i][j] + ` `
    console.log(str)
}