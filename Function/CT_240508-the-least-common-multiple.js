// [최소공배수 구하기 ](https://www.codetree.ai/missions/5/problems/find-the-least-common-multiple)
let [n,m] = require(`fs`).readFileSync(0).toString().trim().split(' ').map(Number)
getLCM(n, m)

function getLCM(n, m){
    let gcd = getGCD(n, m)
    process.stdout.write( n*m/gcd  + '')
}

function getGCD(n, m){
    while(m != 0){
        let r = n % m;
        n = m
        m = r
    }
    return n
}
// [최대공약수 구하기 ](https://www.codetree.ai/missions/5/problems/find-the-greatest-common-divisor)
let [n, m] = require('fs').readFileSync(0).toString().trim().split(' ').map(Number)
getGCD(n, m)

function getGCD(n, m){
    let big = (n > m) ? n : m
    let sma = (n < m) ? n : m

    for(let i=sma; i>0; i--)
        if(big % i == 0 && sma%i ==0){
            process.stdout.write(i + '')
            break;
        }
}

// [숫자로 이루어진 사각형 ](https://www.codetree.ai/missions/5/problems/rectangle-with-a-number)
let n = Number(require(`fs`).readFileSync(0).toString().trim())
printOneDigitSquare(n)

function printOneDigitSquare(n){
    let num=1
    for(let i=0; i<n; i++){
        let str =``
        for(let j=0; j<n; j++){
            // process.stdout.write(toString(num));

            // process.stdout.write(cnt + " ");
            // cnt++

            str += num + ` `
            num = (++num==10) ? 1 : num
        }
        // process.stdout.write(`\n`)
        console.log(str)
    }
}

// [함수를 이용해 직사각형 만들기 ](https://www.codetree.ai/missions/5/problems/create-a-rectangle-using-a-function)
let [n, m] = require('fs').readFileSync(0).toString().trim().split(' ').map(Number)
printnmSquare(n, m)

function printnmSquare(n, m){
    for(let i=0; i<n; i++){
        for(let j=0; j<m; j++) process.stdout.write(`1`)
        console.log()
    }
}
// [반복 출력하기 ](https://www.codetree.ai/missions/5/problems/repeated-output)
let N = Number(require('fs').readFileSync(0).toString().trim())
print_str(N)

function print_str(n){
    for(let i=0; i<n; i++) process.stdout.write(`12345^&*()_\n`)
}

// [별 찍는 것을 5번 반복하기 ](https://www.codetree.ai/missions/5/problems/repeat-shooting-the-stars-five-times)
function print10Stars(){
    process.stdout.write(`**********\n`)
}
for (let i=0; i<5; i++)
    print10Stars();

