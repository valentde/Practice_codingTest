// [짝수이면서 합이 5의 배수인 수 ](https://www.codetree.ai/missions/5/problems/an-even-number-with-a-multiple-of-5-in-the-sum)
function isOddEtc(n){
    if(n%2==1) return false;

    let carrySum= 0
    while(n>0){
        carrySum += (n % 10)
        n  = parseInt(n/10)
    }
    return carrySum %5 ==0 ? true : false;
}
let n = Number(require(`fs`).readFileSync(0).toString().trim())
process.stdout.write( isOddEtc(n) ? `Yes` : `No`)

// [함수를 이용한 369 게임 ](https://www.codetree.ai/missions/5/problems/369-games-using-functions)
function has369(i){
    while(i>0){
        let r = i % 10
        if(r==3 || r==6 || r==9) return true
        i= parseInt(i/10)
    }
    return false
}
function countReq(a, b){
    let count=0;
    for(let i=a; i<b+1; i++){
        if( i%3==0 || has369(i)) count++;
    }
    return count;
}

let [a, b] = require(`fs`).readFileSync(0).toString().trim().split(` `).map(Number)
console.log(countReq(a, b))

// [정수의 최솟값 ](https://www.codetree.ai/missions/5/problems/minimum-value-of-an-integer)
let arr = require('fs').readFileSync(0).toString().trim().split(' ').map(Number)
console.log(findMin(arr))

function findMin(arr){
    let min=arr[0]
    min = arr[0] < arr[1] ? arr[0] : arr[1]
    min = min < arr[2] ? min : arr[2]
    return min
}

// [1부터 특정 수까지의 합 ](https://www.codetree.ai/missions/5/problems/sum-from-1-to-a-certain-number)
let n = Number(require('fs').readFileSync(0).toString().trim())
console.log(sumFun(n))

function sumFun(n){
    let sum=0
    for(let i=1; i<n + 1; i++) sum += i;
    return Math.floor(sum/10);
}