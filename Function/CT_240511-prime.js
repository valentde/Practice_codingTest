function isPrime(n){
    if(n ==2) return true
    for(let i=3; i<Math.sqrt(n) +1; i+=2){
        if(n % i ==0) return false;
    }

    if(n == 1)
        return false;
        
    return true
}

const [a, b] = require('fs').readFileSync(0).toString().trim().split(' ').map(Number)

let sum=0
if(a==2) sum =2

for(let i=a; i<b + 1; i++){
    if(i%2==0) continue
    if(isPrime(i))
        sum += i
}

process.stdout.write( (b==1 ? 0 : sum) + ``)