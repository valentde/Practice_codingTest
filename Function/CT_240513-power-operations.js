// [두 수의 거듭제곱 ](https://www.codetree.ai/missions/5/problems/two-numbers-of-squares)
function pow(a, b){
    let n = a
    while(b-- >1){
        a *= n
    }
    return a
/*

    # a^b의 값을 반환합니다.
    def power(a, b):
    cnt = 1
    for _ in range(b):
        cnt *= a

    return cnt
*/

}
const [a, b] = require(`fs`).readFileSync(0).toString().trim().split(` `).map(Number)
console.log(pow(a, b))

//[사칙연산 함수 ](https://www.codetree.ai/missions/5/problems/quadratic-operations-function)
const input = require(`fs`).readFileSync(0).toString().trim()
const i = input.split(' ')
let a=Number(i[0]), c=Number(i[2])
console.log(operation(a, c, i[1], input))

function operation(a, c, mod, input){
   if(mod == '+')
        return input + ' = ' + (a + c)
   if(mod == '-')
        return input + ' = ' + (a - c)
   if(mod == '*')
        return input + ' = ' + a * c
   if(mod == '/')
        return input + ' = ' + parseInt(a / c)
    return `False`
}

// # [함수를 이용한 연속부분수열 여부 판단하기 ](https://www.codetree.ai/missions/5/problems/to-determine-whether-a-continuous-subsequence-is-made-using-a-function)
function isSubSequence(A, B){
    for(let i=0; i<A.length - B.length + 1; i++){
        let isSub=true
        for(let j=0; j<B.length; j++)
            if(A[i + j] != B[j]){
                isSub = false
                break
            }
        if(isSub) return true
    }
    return false
}

const i = require(`fs`).readFileSync(0).toString().trim().split(`\n`)
const [n1, n2] = i[0].split(` `).map(Number)
let A = i[1].split(` `).map(Number)
let B = i[2].split(` `).map(Number)
process.stdout.write( isSubSequence(A, B) ? `Yes` : `No`)

//[함수를 이용한 합과 소수 판별 ](https://www.codetree.ai/missions/5/problems/use-functions-to-determine-sums-and-decimals)
function isPrime(n){
    if(n==2) return true
    for(let i=3; i<Math.sqrt(n) + 1; i++){
        if(n % i == 0) return false
    }
    return true
}
function isDigitSumEven(n){
    let sum=0
    while(n){
        sum += n % 10
        n = parseInt(n / 10)
    }
    return sum%2==0 ? true : false
}

const [a, b] = require(`fs`).readFileSync(0).toString().trim().split(` `).map(Number)
let cnt=0
for(let i=a; i<b + 1; i++){
    if(i !=2 && i % 2 ==0) continue;
    if(isPrime(i))
        if(isDigitSumEven(i))
            ++cnt
}
console.log(cnt)


//[함수를 이용한 윤년 판별 ](https://www.codetree.ai/missions/5/problems/tell-the-function-using-a-leap-year)
function isLeap(y){
    if(y % 100== 0 && y%400!=0) return false;
    if(y % 4 == 0) return true;
    return false;
}
const y = Number(require(`fs`).readFileSync(0).toString().trim())
process.stdout.write(isLeap(y) ? `true` : `false`)

// [함수를 이용한 온전수 판별 ](https://www.codetree.ai/missions/5/problems/determining-the-whole-number-using-a-function)
const [a, b] = require(`fs`).readFileSync(0).toString().trim().split(` `).map(Number)
let cnt=0
for(let i=a; i<b + 1; i++){
    if(i%2==0 || i%10==5) continue
    if(i%3==0 && i%9 != 0) continue
    ++cnt
}
console.log(cnt)