//[문자열의 특정 위치 찾기 2 ](https://www.codetree.ai/missions/4/problems/find-specific-location-in-spring-2)
#include <iostream>
#include <string>

int main() {
    std::string w[ 5 ]= {"apple", "banana", "grape", "blueberry", "orange"};

    char c;
    std::cin >> c;
    int count=0;

    for(int i=0; i<5; i++){
        if(w[i].length()<3) continue;
        if(w[i][2]==c || w[i][3]==c) {
            count++;    
            std::cout << w[i] << std::endl;
        }
    }

    std::cout << count;

    return 0;
}