// [동전이 있는 위치 ](https://www.codetree.ai/missions/4/problems/Where-coins-are-located)
const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");

let [n, m] = input[0].split(" ").map(Number);
let placed = Array(n).fill(0).map( () => Array(n).fill(0) );

for (let i = 1; i < m+1; i++) {
   let [r, c] = input[i].split(" ").map(Number);
   placed[r - 1][c - 1] = 1;
}

for (let i = 0; i < n; i++) {
    str = ``
    for(let j=0; j<n; j++) str += placed[i][j] + ` `
    console.log(str)
}