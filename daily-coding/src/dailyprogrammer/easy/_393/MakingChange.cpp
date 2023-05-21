#include <iostream>
#include <array>
using namespace std;

// Sum all values in a int array
int sum(int any_list[], const int list_size) {
    int summed = 0;
    for (int i =0; i < list_size; i++) {
        summed += any_list[i];
    }
    return summed;
}

// Gives number of coins needed to make optimal change from money
int change(int money) {
    // Using C array way, there is the std::array and vector C++ way also
    int coins[] = {500, 100, 25, 10, 5, 1};
    const int amt_coins = sizeof coins / sizeof coins[0]; 
    int coins_given[amt_coins];
    for (int i =0; i < amt_coins; i++) {
        int curr_coin = coins[i];
        int remainder = money % curr_coin;
        coins_given[i] = money / curr_coin;
        money = remainder;
    }
    return sum(coins_given, amt_coins);
}

int main() {
    cout << "change(0) => " << change(0) << endl;
    cout << "change(12) => " << change(12) << endl;
    cout << "change(468) => " << change(468) << endl;
    cout << "change(123456) => " << change(123456) << endl;
    return 0;
}