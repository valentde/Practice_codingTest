// (JS)
// Array(개수) 만쓰면 초기값=NaN🙁
// for-in != .forEach(function(){}) 완전히 다름


// ### 특정값(0) 전까지 입력받기
// ❌한꺼번에 입력받기❌ ( C , C++, JAVA)
// int arr[99]; //[ C ] ,[ C++ ]
// int[] arr = new int[99]; //[JAVA]
//
// for(int i = 0; i < 99; i++) {
// scanf("%d", &arr[i]); //[ C ]
// std::cin>> arr[i];        //[ C++ ]
// arr[i] = sc.nextInt(); //[JAVA]
//
// 	if(arr[i] == 0) break;	//★
// 	...나머지연산...
// }
//
// ⭕한꺼번에 입력받기⭕ → for-if-break
// (PY) arr = list(map(int, input().split()))
// (JS) let arr = require("fs").readFileSync(0).toString().trim().split(" ").map(Number);

// [주사위 놀이 ](https://www.codetree.ai/missions/4/problems/play-with-dice)
let arr = require('fs').readFileSync(0).toString().trim().split(' ').map(Number)

let countArr = Array(6 + 1).fill(0)
// for (let e in arr) countArr[ e ]++
arr.forEach(e => countArr[e]++)

for(let i=1; i<countArr.length; i++) console.log(i + ` - ` + countArr[i])

 // [1-9 개수 세기 ](https://www.codetree.ai/missions/4/problems/count-one-to-nine)
input = require('fs').readFileSync(0).toString().trim().split('\n')
n = Number(input[0])
arr = input[1].split(' ').map(Number)

let countArr = Array(9 + 1).fill(0)
for(let i=0; i<arr.length; i++)
    countArr[ arr[i] ]++

for(let i=1; i<10; i++) console.log(countArr[i])


// [십의 자리 숫자 ](https://www.codetree.ai/missions/4/problems/number-of-tens-digit)
let arr = require('fs').readFileSync(0).toString().trim().split(' ').map(Number)

let countArr = Array(10 + 1).fill(0)

// arr.forEach(v => countArr[ parseInt(v/10) ]++)
for(let i=0; i<arr.length; i++){
    v = arr[i]
    if(v==0) break;
    countArr[ parseInt(v/10) ]++
}

for(let i=1; i<10; i++) console.log(`${i} - ${countArr[i]}`)