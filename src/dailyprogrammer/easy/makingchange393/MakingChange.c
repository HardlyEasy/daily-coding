#include <stdio.h>

// Sum all values in a int array
int sum(int any_list[], const int list_size) {
    int summed = 0;
    for(int i =0; i < list_size; i++) {
        summed += any_list[i];
    }
    return summed;
}

// Gives number of coins needed to make optimal change from money
int change(int money) {
    int coins[] = {500, 100, 25, 10, 5, 1};
    const int coins_len = sizeof coins / sizeof coins[0];
    int amt_coins[coins_len];
    for (int i = 0; i < coins_len; i++) {
        int coin = coins[i];
        int remainder = money % coin;
        amt_coins[i] = money / coin;
        money = remainder;
    }
    return sum(amt_coins, coins_len);
}

int main() {
    printf("change(0) => %i\n", change(0));
    printf("change(12) => %i\n", change(12));
    printf("change(468) => %i\n", change(468));
    printf("change(123456) => %i", change(123456));
    return 0;
}