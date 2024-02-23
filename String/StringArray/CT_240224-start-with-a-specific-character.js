// [특정 문자로 시작하는 문자열 ](https://www.codetree.ai/missions/4/problems/strings-that-start-with-a-specific-character)

/*
    소수점 공백두고 출력방법
    console.log(cnt, (lenSum / cnt).toFixed(2));
    
    System.out.printf("%d %.2f", cnt, (double)lenSum / cnt);
    
    print(f"{cnt} {len_sum / cnt:.2f}")
    
    std::cout << fixed;
    std::cout.precision(2);
    std::cout << cnt << " " << (double)len_sum / cnt;
    
    printf("%d %.2f", cnt, (double)len_sum / cnt);
*/


const input = require('fs').readFileSync(0).toString().trim().split('\n');
let n = Number(input[0])
let ch = input[n + 1]
let cnt=0, sum=0
for(let i=1; i<n + 1; i++){
    if(ch !== input[i][0]) continue;

    ++cnt
    sum += input[i].length
} 

console.log(cnt, (sum/cnt).toFixed(2));