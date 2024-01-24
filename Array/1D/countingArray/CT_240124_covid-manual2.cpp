//[코로나 메뉴얼2 ](https://www.codetree.ai/missions/4/problems/covid-manual2)

// [A, B, C, D] = [0, 1, 2, 3]
#include <iostream>
using namespace std;
int main() {

    int alphaArr[4] = {0};

    for(int tc=0; tc<3; tc++){
        char isIll;
        int temperature;
        cin >> isIll;
        cin >> temperature;

        int v=-1;
        if(temperature >= 37){
             v = (isIll=='Y') ? 0 : 1;
        }else{
             v = (isIll=='Y') ? 2: 3;
        }
        
        ++alphaArr[v];
    }
    for(int i=0; i<4; i++) printf("%d ", alphaArr[i]);
    if(alphaArr[0] >=2) cout<< "E";
    
    return 0;
}
//# [나눗셈의 나머지 ](https://www.codetree.ai/missions/4/problems/remainder-of-division/description)
#include <iostream>
using namespace std;
int main() {
    int a, b, quotient, remainder, sum=0;
    cin >> a >> b;

    int cntArr_remainder[b]  = {0};

// a가 1이하가 되기 전 까지 나눗셈을 반복
    // while(a>0){
    while(a>1){
        quotient = a / b;
        remainder= a % b;

        cntArr_remainder[ remainder ]++;

        a = quotient;
    }

    for(int i=0; i<b; i++) sum += cntArr_remainder[i]*cntArr_remainder[i];
    cout<< sum;

    return 0;
}