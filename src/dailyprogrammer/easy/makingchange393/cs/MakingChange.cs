using System;

namespace MakingChange {
    class Program {
        enum Coin {
            FiveDollarCoin = 500, DollarCoin = 100,
            Quarter = 25, Dime = 10, Nickel = 5, Penny = 1
        }
        
        static void Main(String[] args) {
            Console.WriteLine("change(0) => {0}", Change(0));
            Console.WriteLine("change(12) => {0}", Change(12));
            Console.WriteLine("change(468) => {0}", Change(468));
            Console.WriteLine("change(123456) => {0}", Change(123456));
        }
        // Prints number of coins needed of each coin denomination
        // Returns total number of coins needed across all coin values
        static int Change(int money) {
            int yourChange = 0;
            int[] coinValues = (int[])Enum.GetValues(typeof(Coin));
            Array.Reverse(coinValues);
            foreach(int value in coinValues ) {
                int remainder = money % value;
                int amtCoins = money / value;
                yourChange += amtCoins;
                money = remainder;
                Console.Write("{0} {1}, ", amtCoins, 
                    Enum.GetName(typeof(Coin), value));
            }
            Console.WriteLine();
            return yourChange;
        }
    } // end class
} // end namespace