//[붙여서 합하기 ](https://www.codetree.ai/missions/4/problems/add-and-add)
#include <iostream>
#include <string>
using namespace std;

int main() {
    // int a, b;
    string a, b;
    cin >> a >> b;

    int ab = stoi(a + b);
    int ba = stoi(b + a);

    cout<< ab + ba;
}