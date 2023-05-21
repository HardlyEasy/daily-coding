Log of questions done in `#Summary`

Full question text in `#Easy #Intermediate #Hard`

# Summary
## Easy
```
[2015-11-02] Challenge #239 [Easy] A Game of Threes 
[2018-05-14] Challenge #361 [Easy] Tally Program
[2018-06-18] Challenge #364 [Easy] Create a Dice Roller
[2019-01-14] Challenge #372 [Easy] Perfectly balanced 
[2019-07-15] Challenge #379 [Easy] Progressive taxation 
[2020-03-09] Challenge #383 [Easy] Necklace matching
[2021-04-26] Challenge #387 [Easy] Caesar cipher 
[2021-05-24] Challenge #391 [Easy] The ABACABA sequence
[2021-06-07] Challenge #393 [Easy] Making change
[2021-07-19] Challenge #399 [Easy] Letter value sum
```
## Intermediate
```
[2015-10-28] Challenge #238 [Intermediate] Fallout Hacking Game
[2015-12-16] Challenge #245 [Intermediate] Ggggggg gggg Ggggg-ggggg!
[2018-07-11] Challenge #365 [Intermediate] Sales Commissions
[2019-03-13] Challenge #376 [Intermediate] The Revised Julian Calendar
```
## Hard
```

```

[toc]

# Easy

## [2015-11-02] Challenge #239 [Easy] A Game of Threes

### Background

Back in middle school, I had a peculiar way of dealing with super boring classes. I would take my handy pocket calculator and play a "Game of Threes". Here's how you play it:

First, you mash in a random large number to start with. Then, repeatedly do the following:

* If the number is divisible by 3, divide it by 3.
* If it's not, either add 1 or subtract 1 (to make it divisible by 3), then divide it by 3.

The game stops when you reach "1". 

While the game was originally a race against myself in order to hone quick math reflexes, it also poses an opportunity for some interesting programming challenges. Today, the challenge is to create a program that "plays" the Game of Threes.

### Challenge Description

The input is a single number: the number at which the game starts. Write a program that plays the Threes game, and outputs a valid sequence of steps you need to take to get to 1. Each step should be output as the number you start at, followed by either -1 or 1 (if you are adding/subtracting 1 before dividing), or 0 (if you are just dividing). The last line should simply be 1.

### Input Description

The input is a single number: the number at which the game starts.

    100

### Output Description

The output is a list of valid steps that must be taken to play the game. Each step is represented by the number you start at, followed by either -1 or 1 (if you are adding/subtracting 1 before dividing), or 0 (if you are just dividing). The last line should simply be 1.

    100 -1
    33 0
    11 1
    4 -1
    1

### Challenge Input

    31337357

### Fluff

Hi everyone! I am /u/Blackshell, one of the new moderators for this sub. I am very happy to meet everyone and contribute to the community (and to give /u/jnazario a little bit of a break). If you have any feedback for me, I would be happy to hear it. Lastly, as always, remember if you would like to propose a challenge to be posted, head over to /r/dailyprogrammer_ideas. 

## [2018-05-14] Challenge #361 [Easy] Tally Program

### Description

5 Friends \(let's call them a, b, c, d and e\) are playing a game and need to keep track of the scores. Each time someone scores a point, the letter of his name is typed in lowercase. If someone loses a point, the letter of his name is typed in uppercase. Give the resulting score from highest to lowest.

### Input Description

A series of characters indicating who scored a point. Examples:

    abcde
    dbbaCEDbdAacCEAadcB

### Output Description

The score of every player, sorted from highest to lowest. Examples:

    a:1, b:1, c:1, d:1, e:1
    b:2, d:2, a:1, c:0, e:-2

### Challenge Input

    EbAAdbBEaBaaBBdAccbeebaec

### Credit

This challenge was suggested by user /u/TheMsDosNerd, many thanks! If you have any challenge ideas, please share them in /r/dailyprogrammer_ideas and there's a good chance we'll use them.

## [2018-06-18] Challenge #364 [Easy] Create a Dice Roller 

### Description

I love playing D&D with my friends, and my favorite part is creating character sheets \(my DM is notorious for killing us all off by level 3 or so\). One major part of making character sheets is rolling the character's stats. Sadly, I have lost all my dice, so I'm asking for your help to make a dice roller for me to use!

### Input description

Your input will contain one or more lines, where each line will be in the form of "NdM"; for example:

    3d6
    4d12
    1d10
    5d4

If you've ever played D&D you probably recognize those, but for the rest of you, this is what those mean:

The first number is the number of dice to roll, the d just means "dice", it's just used to split up the two numbers, and the second number is how many sides the dice have. So the above example of "3d6" means "roll 3 6\-sided dice". Also, just in case you didn't know, in D&D, not all the dice we roll are the normal cubes. A d6 is a cube, because it's a 6\-sided die, but a d20 has twenty sides, so it looks a lot closer to a ball than a cube.

The first number, the number of dice to roll, can be any integer between 1 and 100, inclusive.

The second number, the number of sides of the dice, can be any integer between 2 and 100, inclusive.

### Output description

You should output the sum of all the rolls of that specified die, each on their own line. so if your input is "3d6", the output should look something like

    14

Just a single number, you rolled 3 6\-sided dice, and they added up to 14.

### Challenge Input

    5d12
    6d4
    1d2
    1d8
    3d6
    4d20
    100d100

### Challenge Output

    [some number between 5 and 60, probably closer to 32 or 33]
    [some number between 6 and 24, probably around 15]
    [you get the idea]
    [...]

### Notes/Hints

A dice roll is basically the same as picking a random number between 1 and 6 \(or 12, or 20, or however many sides the die has\). You should use some way of randomly selecting a number within a range based off of your input. Many common languages have random number generators available, but at least a few of them will give the same "random" numbers every time you use the program. In my opinion that's not very random. If you run your code 3\+ times with the same inputs and it gives the same outputs, that wouldn't be super useful for a game of D&D, would it? If that happens with your code, try to find a way around that. I'm guessing for some of the newer folks, this might be one of the trickier parts to get correct.

Don't just multiply your roll by the number of dice, please. I don't know if any of you were thinking about doing that, but I was. The problem is that if you do that, it eliminates a lot of possible values. For example, there's no way to roll 14 from 3d6 if you just roll it once and multiply by 3. Setting up a loop to roll each die is probably your best bet here.

### Bonus

In addition to the sum of all dice rolls for your output, print out the result of each roll on the same line, using a format that looks something like

    14: 6 3 5
    22: 10 7 1 4
    9: 9
    11: 3 2 2 1 3

You could also try setting it up so that you can manually input more rolls. that way you can just leave the program open and every time you want to roll more dice, you just type it in and hit enter.

### Credit

This challenge was suggested by user /u/Fishy_Mc_Fish_Face, many thanks!

Have a good challenge idea? Consider submitting it to [r/dailyprogrammer\_ideas](https://www.reddit.com/r/dailyprogrammer_ideas)

## [2019-01-14] Challenge #372 [Easy] Perfectly balanced 

Given a string containing only the characters `x` and `y`, find whether there are the same number of `x`s and `y`s.

    balanced("xxxyyy") => true
    balanced("yyyxxx") => true
    balanced("xxxyyyy") => false
    balanced("yyxyxxyxxyyyyxxxyxyx") => true
    balanced("xyxxxxyyyxyxxyxxyy") => false
    balanced("") => true
    balanced("x") => false

### Optional bonus

Given a string containing only lowercase letters, find whether every letter that appears in the string appears the same number of times. Don't forget to handle the empty string (`""`) correctly!

    balanced_bonus("xxxyyyzzz") => true
    balanced_bonus("abccbaabccba") => true
    balanced_bonus("xxxyyyzzzz") => false
    balanced_bonus("abcdefghijklmnopqrstuvwxyz") => true
    balanced_bonus("pqq") => false
    balanced_bonus("fdedfdeffeddefeeeefddf") => false
    balanced_bonus("www") => true
    balanced_bonus("x") => true
    balanced_bonus("") => true

Note that `balanced_bonus` behaves differently than `balanced` for a few inputs, e.g. `"x"`.

## [2019-07-15] Challenge #379 [Easy] Progressive taxation 

### Challenge

The nation of Examplania has the following income tax brackets:

    income cap      marginal tax rate
      ¤10,000           0.00 (0%)
      ¤30,000           0.10 (10%)
     ¤100,000           0.25 (25%)
        --              0.40 (40%)

If you're not familiar with how tax brackets work, see the section below for an explanation.

Given a whole-number income amount up to ¤100,000,000, find the amount of tax owed in Examplania. Round down to a whole number of ¤.

### Examples

    tax(0) => 0
    tax(10000) => 0
    tax(10009) => 0
    tax(10010) => 1
    tax(12000) => 200
    tax(56789) => 8697
    tax(1234567) => 473326

### Optional improvement

One way to improve your code is to make it easy to swap out different tax brackets, for instance by having the table in an input file. If you do this, you may assume that both the income caps and marginal tax rates are in increasing order, the highest bracket has no income cap, and all tax rates are whole numbers of percent (no more than two decimal places).

However, because this is an Easy challenge, this part is optional, and you may hard code the tax brackets if you wish.

### How tax brackets work

A tax bracket is a range of income based on the income caps, and each tax bracket has a corresponding marginal tax rate, which applies to income within the bracket. In our example, the tax bracket for the range ¤10,000 to ¤30,000 has a marginal tax rate of 10%. Here's what that means for each bracket:

* If your income is less than ¤10,000, you owe 0 income tax.
* If your income is between ¤10,000 and ¤30,000, you owe 10% income tax on the income that exceeds ¤10,000. For instance, if your income is ¤18,000, then your income in the 10% bracket is ¤8,000. So your income tax is 10% of ¤8,000, or ¤800.
* If your income is between ¤30,000 and ¤100,000, then you owe 10% of your income between ¤10,000 and ¤30,000, plus 25% of your income over ¤30,000.
* And finally, if your income is over ¤100,000, then you owe 10% of your income from ¤10,000 to ¤30,000, plus 25% of your income from ¤30,000 to ¤100,000, plus 40% of your income above ¤100,000.

One aspect of progressive taxation is that increasing your income will never decrease the amount of tax that you owe, or your overall tax rate (except for rounding).

### Optional bonus

The overall tax rate is simply the total tax divided by the total income. For example, an income of ¤256,250 has an overall tax of ¤82,000, which is an overall tax rate of exactly 32%:

    82000 = 0.00 × 10000 + 0.10 × 20000 + 0.25 × 70000 + 0.40 × 156250
    82000 = 0.32 × 256250

Given a target overall tax rate, find the income amount that would be taxed at that overall rate in Examplania:

    overall(0.00) => 0 (or anything up to 10000)
    overall(0.06) => 25000
    overall(0.09) => 34375
    overall(0.32) => 256250
    overall(0.40) => NaN (or anything to signify that no such income value exists)

You may get somewhat different answers because of rounding, but as long as it's close that's fine.

The simplest possibility is just to iterate and check the overall tax rate for each possible income. That works fine, but if you want a performance boost, check out binary search. You can also use algebra to reduce the number of calculations needed; just make it so that your code still gives correct answers if you swap out a different set of tax brackets.

## [2020-03-09] Challenge #383 [Easy] Necklace matching

### Challenge

Imagine a necklace with lettered beads that can slide along the string. [Here's an example image.](https://www.craftkitsandsupplies.com/images/Beads/Alpha_Beads/Wood_Alphabet_Beads_26217.jpg) In this example, you could take the `N` off `NICOLE` and slide it around to the other end to make `ICOLEN`. Do it again to get `COLENI`, and so on. For the purpose of today's challenge, we'll say that the strings `"nicole"`, `"icolen"`, and `"coleni"` describe the same necklace.

Generally, two strings describe the same necklace if you can remove some number of letters from the beginning of one, attach them to the end in their original ordering, and get the other string. Reordering the letters in some other way does not, in general, produce a string that describes the same necklace.

Write a function that returns whether two strings describe the same necklace.

### Examples

    same_necklace("nicole", "icolen") => true
    same_necklace("nicole", "lenico") => true
    same_necklace("nicole", "coneli") => false
    same_necklace("aabaaaaabaab", "aabaabaabaaa") => true
    same_necklace("abc", "cba") => false
    same_necklace("xxyyy", "xxxyy") => false
    same_necklace("xyxxz", "xxyxz") => false
    same_necklace("x", "x") => true
    same_necklace("x", "xx") => false
    same_necklace("x", "") => false
    same_necklace("", "") => true

### Optional Bonus 1

If you have a string of N letters and you move each letter one at a time from the start to the end, you'll eventually get back to the string you started with, after N steps. Sometimes, you'll see the same string you started with before N steps. For instance, if you start with `"abcabcabc"`, you'll see the same string (`"abcabcabc"`) 3 times over the course of moving a letter 9 times.

Write a function that returns the number of times you encounter the same starting string if you move each letter in the string from the start to the end, one at a time.

    repeats("abc") => 1
    repeats("abcabcabc") => 3
    repeats("abcabcabcx") => 1
    repeats("aaaaaa") => 6
    repeats("a") => 1
    repeats("") => 1

### Optional Bonus 2

There is exactly one set of four words in [the enable1 word list](https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt) that all describe the same necklace. Find the four words.

## [2021-04-26] Challenge #387 [Easy] Caesar cipher

### Warmup

Given a lowercase letter and a number between 0 and 26, return that letter Caesar shifted by that number. To Caesar shift a letter by a number, advance it in the alphabet by that many steps, wrapping around from `z` back to `a`:

    warmup('a', 0) => 'a'
    warmup('a', 1) => 'b'
    warmup('a', 5) => 'f'
    warmup('a', 26) => 'a'
    warmup('d', 15) => 's'
    warmup('z', 1) => 'a'
    warmup('q', 22) => 'm'

Hint: taking a number modulo 26 will wrap around from 25 back to 0. This is commonly represented using the modulus operator `%`. For example, `29 % 26 = 3`. Finding a way to map from the letters a-z to the numbers 0-25 and back will help.

### Challenge

Given a string of lowercase letters and a number, return a string with each letter Caesar shifted by the given amount.

    caesar("a", 1) => "b"
    caesar("abcz", 1) => "bcda"
    caesar("irk", 13) => "vex"
    caesar("fusion", 6) => "layout"
    caesar("dailyprogrammer", 6) => "jgorevxumxgsskx"
    caesar("jgorevxumxgsskx", 20) => "dailyprogrammer"

Hint: you can use the `warmup` function as a helper function.

### Optional bonus 1

Correctly handle capital letters and non-letter characters. Capital letters should also be shifted like lowercase letters, but remain capitalized. Leave non-letter characters, such as spaces and punctuation, unshifted.

    caesar("Daily Programmer!", 6) => "Jgore Vxumxgsskx!"

If you speak a language that doesn't use the 26-letter A-Z alphabet that English does, handle strings in that language in whatever way makes the most sense to you! In English, if a string is encoded using the number N, you can decode it using the number 26 - N. Make sure that for your language, there's some similar way to decode strings.

### Optional bonus 2

Given a string of English text that has been Caesar shifted by some number between 0 and 26, write a function to make a best guess of what the original string was. You can typically do this by hand easily enough, but the challenge is to write a program to do it automatically. Decode the following strings:

    Zol abyulk tl puav h ulda.

    Tfdv ef wlikyvi, wfi uvrky rnrzkj pfl rcc nzky erjkp, szx, gfzekp kvvky.

    Qv wzlmz bw uiqvbiqv iqz-axmml dmtwkqbg, i aeittwe vmmla bw jmib qba eqvoa nwzbg-bpzmm bquma mdmzg amkwvl, zqopb?

One simple way is by using a letter frequency table. Assign each letter in the string a score, with 3 for `a`, -1 for `b`, 1 for `c`, etc., as follows:

    3,-1,1,1,4,0,0,2,2,-5,-2,1,0,2,3,0,-6,2,2,3,1,-1,0,-5,0,-7

The average score of the letters in a string will tell you how its letter distribution compares to typical English. Higher is better. Typical English will have an average score around 2, and strings of random letters will have an average score around 0. Just test out each possible shift for the string, and take the one with the highest score. There are other good ways to do it, though.

*(This challenge is based on [Challenge #47 [easy]](https://www.reddit.com/r/dailyprogrammer/comments/t33vi/522012_challenge_47_easy/), originally posted by u/oskar_s in May 2012.)*

## [2021-05-24] Challenge #391 [Easy] The ABACABA sequence

### Background

The ABACABA sequence is defined as follows: the first iteration is the first letter of the alphabet (`a`). To form the second iteration, you take the second letter (`b`) and put the first iteration (just `a` in this case) before and after it, to get `aba`. For each subsequent iteration, place a copy of the previous iteration on either side of the next letter of the alphabet.

Here are the first 5 iterations of the sequence:

    a
    aba
    abacaba
    abacabadabacaba
    abacabadabacabaeabacabadabacaba

The 26th and final iteration (i.e. the one that adds the `z`) is 67,108,863 characters long. If you use one byte for each character, this takes up just under 64 megabytes of space.

### Challenge

Write a program to print the 26th iteration of the ABACABA sequence.

If it's easier for you, it's also fine to print one character per line, instead of all the characters on a single line.

Just printing the output can take a few minutes, depending on your setup. Feel free to test it out on something smaller instead, like the 20th iteration, which is only about 1 megabyte.

### Optional bonus

Complete the challenge using O(n) memory, where n is the iteration number.

If you don't know what that means, here's another way to say it that's roughly equivalent in this case. You can have as many variables as you want, but they must each hold either a single number or character, or a structure (list, vector, dict, string, map, tree, etc.) whose size never gets much larger than 26. If a function calls itself recursively, the call stack must also be limited to a depth of about 26. (This is definitely an oversimplification, but that's the basic idea. Feel free to ask if you want to know about whether any particular approach uses O(n) memory.)

*(This is a repost of [Challenge #56 [easy]](https://www.reddit.com/r/dailyprogrammer/comments/u0tdt/5232012_challenge_56_easy/), originally posted by u/oskar_s in May 2012.)*

## [2021-06-07] Challenge #393 [Easy] Making change 

The country of Examplania has coins that are worth 1, 5, 10, 25, 100, and 500 currency units. At the Zeroth Bank of Examplania, you are trained to make various amounts of money by using as many ¤500 coins as possible, then as many ¤100 coins as possible, and so on down.

For instance, if you want to give someone ¤468, you would give them four ¤100 coins, two ¤25 coins, one ¤10 coin, one ¤5 coin, and three ¤1 coins, for a total of 11 coins.

Write a function to return the number of coins you use to make a given amount of change.

    change(0) => 0
    change(12) => 3
    change(468) => 11
    change(123456) => 254

*(This is a repost of [Challenge #65 [easy]](https://www.reddit.com/r/dailyprogrammer/comments/v3a89/6152012_challenge_65_easy/), originally posted by u/oskar_s in June 2012.)*

## [2021-07-19] Challenge #399 [Easy] Letter value sum 

### Challenge

Assign every lowercase letter a value, from 1 for `a` to 26 for `z`. Given a string of lowercase letters, find the sum of the values of the letters in the string.

    lettersum("") => 0
    lettersum("a") => 1
    lettersum("z") => 26
    lettersum("cab") => 6
    lettersum("excellent") => 100
    lettersum("microspectrophotometries") => 317

### Optional bonus challenges

Use [the enable1 word list](https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt) for the optional bonus challenges.

1. `microspectrophotometries` is the only word with a letter sum of 317. Find the only word with a letter sum of 319.
1. How many words have an odd letter sum?
1. There are 1921 words with a letter sum of 100, making it the second most common letter sum. What letter sum is most common, and how many words have it?
1. `zyzzyva` and `biodegradabilities` have the same letter sum as each other (151), and their lengths differ by 11 letters. Find the other pair of words with the same letter sum whose lengths differ by 11 letters.
1. `cytotoxicity` and `unreservedness` have the same letter sum as each other (188), and they have no letters in common. Find a pair of words that have no letters in common, and that have the same letter sum, which is larger than 188. (There are two such pairs, and one word appears in both pairs.)
1. The list of word `{ geographically, eavesdropper, woodworker, oxymorons }` contains 4 words. Each word in the list has both a different number of letters, and a different letter sum. The list is sorted both in descending order of word length, and ascending order of letter sum. What's the longest such list you can find?

*(This challenge is a repost of [Challenge #52 [easy]](https://www.reddit.com/r/dailyprogrammer/comments/tmnfq/5142012_challenge_52_easy/), originally posted by u/rya11111 in May 2012.)*

It's been fun getting a little activity going in here these last 13 weeks. However, this will be my last post to this subreddit for the time being. Here's hoping another moderator will post some challenges soon!

# Intermediate

## [2015-10-28] Challenge #238 [Intermediate] Fallout Hacking Game 

### Description

The popular video games *Fallout 3* and *Fallout: New Vegas* have [a computer "hacking" minigame](http://gamewiki.net/Fallout_3/Hacking_Guide) where the player must correctly guess the correct password from a list of same-length words. Your challenge is to implement this game yourself.

The game operates similarly to the classic board game [Mastermind](http://en.wikipedia.org/wiki/Mastermind_(board_game\)). The player has only 4 guesses and on each incorrect guess the computer will indicate how many letter *positions* are correct.

For example, if the password is MIND and the player guesses MEND, the game will indicate that 3 out of 4 positions are correct (M_ND). If the password is COMPUTE and the player guesses PLAYFUL, the game will report 0/7. While some of the letters match, they're in the wrong position.

Ask the player for a difficulty (very easy, easy, average, hard, very hard), then present the player with 5 to 15 words of the same length. The length can be 4 to 15 letters. More words and letters make for a harder puzzle. The player then has 4 guesses, and on each incorrect guess indicate the number of correct positions.

Here's an example game:

    Difficulty (1-5)? 3
    SCORPION
    FLOGGING
    CROPPERS
    MIGRAINE
    FOOTNOTE
    REFINERY
    VAULTING
    VICARAGE
    PROTRACT
    DESCENTS
    Guess (4 left)? migraine
    0/8 correct
    Guess (3 left)? protract
    2/8 correct
    Guess (2 left)? croppers
    8/8 correct
    You win!

You can draw words from our favorite dictionary file: [enable1.txt](http://code.google.com/p/dotnetperls-controls/downloads/detail?name=enable1.txt). Your program should completely ignore case when making the position checks.

There may be ways to increase the difficulty of the game, perhaps even making it impossible to guarantee a solution, based on your particular selection of words. For example, your program could supply words that have little letter position overlap so that guesses reveal as little information to the player as possible.

### Credit

This challenge was created by user /u/skeeto. If you have any challenge ideas please share them on /r/dailyprogrammer_ideas and there's a good chance we'll use them.  

## [2015-12-16] Challenge #245 [Intermediate] Ggggggg gggg Ggggg-ggggg! 

We have discovered a new species of aliens! They look like [this](https://www.redditstatic.com/about/assets/reddit-alien.png) and are trying to communicate with us using the /r/ggggg subreddit! As you might have been able to tell, though, it is awfully hard to understand what they're saying since their super-advanced alphabet only makes use of two letters: "g" and "G". Fortunately, their numbers, spacing and punctuation are the same.

We are going to write a program to translate to and from our alphabet to theirs, so we can be enlightened by their intelligence.

Feel free to code either the encoding program, the decoding program, or both.

^Also, ^please ^do ^not ^actually ^harass ^the ^residents ^of ^/r/ggggg.

### Part 1: Decoding

First, we need to be able to understand what the Ggggg aliens are saying. Fortunately, they are cooperative in this matter, and they helpfully include a "key" to translate between their g-based letters and our Latin letters. Your decoder program needs to read this key from the first line of the input, then use it to translate the rest of the input.

### Sample decoder input 1

    H GgG d gGg e ggG l GGg o gGG r Ggg w ggg
    GgGggGGGgGGggGG, ggggGGGggGGggGg!

### Sample decoder output 1

    Hello, world!

**Explanation:** Reading the input, the key is:

* H = GgG
* d = gGg
* e = ggG
* l = GGg
* o = gGG
* r = Ggg
* w = ggg

When we read the message from left to right, we can divide it into letters like so (alternating letters bolded):

&gt; **GgG**ggG**GGg**GGg**gGG**, **ggg**gGG**Ggg**GGg**gGg**!

Take those letter groups and turn them into letters using the key, and you get "Hello, world!"

### Sample decoder input 2

    a GgG d GggGg e GggGG g GGGgg h GGGgG i GGGGg l GGGGG m ggg o GGg p Gggg r gG y ggG
    GGGgGGGgGGggGGgGggG /gG/GggGgGgGGGGGgGGGGGggGGggggGGGgGGGgggGGgGggggggGggGGgG!

Note that the letters are *not* guaranteed to be of equal length.

### Sample decoder output 2

    hooray /r/dailyprogrammer!


### Part 2: Encoding

Next, we will go in the other direction. Come up with a key based on the letters "g" and "G" that maps all the letters in a given message to Ggggg equivalents, use it to translate the message, then output both the key and the translated message. You can double-check your work using the decoding script from part 1.

### Sample input

    Hello, world!

### Sample output

    H GgG d gGg e ggG l GGg o gGG r Ggg w ggg
    GgGggGGGgGGggGG, ggggGGGggGGggGg!

Your key (and thus message) may end up being completely different than the one provided here. That's fine, as long as it can be translated back.

### Part 2.1 (Bonus points): Compression

Just as it annoys us to see someone typing "llliiiiikkkeeee ttttthhhiiiisssss", the Ggggg aliens don't actually enjoy unnecessary verbosity. Modify your encoding script to create a key that results in the *shortest possible Ggggg message*. You should be able to decode the output using the same decoder used in part 1 (the second sample input/output in part 1 is actually compressed).

Here's a [hint](https://en.wikipedia.org/wiki/Variable-length_code).

### Sample input:

    Here's the thing. You said a "jackdaw is a crow."
    Is it in the same family? Yes. No one's arguing that.
    As someone who is a scientist who studies crows, I am telling you, specifically, in science, no one calls jackdaws crows. If you want to be "specific" like you said, then you shouldn't either. They're not the same thing.
    If you're saying "crow family" you're referring to the taxonomic grouping of Corvidae, which includes things from nutcrackers to blue jays to ravens.
    So your reasoning for calling a jackdaw a crow is because random people "call the black ones crows?" Let's get grackles and blackbirds in there, then, too.
    Also, calling someone a human or an ape? It's not one or the other, that's not how taxonomy works. They're both. A jackdaw is a jackdaw and a member of the crow family. But that's not what you said. You said a jackdaw is a crow, which is not true unless you're okay with calling all members of the crow family crows, which means you'd call blue jays, ravens, and other birds crows, too. Which you said you don't.
    It's okay to just admit you're wrong, you know?

### Sample output:

Found here (a bit too big to paste in the challenge itself): http://www.hastebin.com/raw/inihibehux.txt

Remember you can test your decoder on this message, too!

--------

C GgggGgg H GgggGgG T GgggGGg a gGg c GGggG d GggG e GgG g ggGgG h GGgGg i gGGg j GgggGGG l gGGG m ggGGg n GGgGG o ggg p ggGGG r GGGg s GGGG t GGgggG u ggGgg v Ggggg w GGggggg y GGggggG
GgggGGgGGgGggGGgGGGG GGggGGGgGggGggGGGgGGGGgGGGgGGggGgGGgG GGggggggGgGGGG ggGGGGGGggggggGGGgggGGGGGgGGggG gGgGGgGGGggG GggGgGGgGGGGGGggGggGggGGGGGGGGGgGGggG gggGggggGgGGGGg gGgGGgggG /GGGg/GggGgGggGGggGGGGGggggGggGGGGGGggggggGgGGGGggGgggGGgggGGgGgGGGGg_gGGgGggGGgGgGgGGGG. GgggGgGgGgGggggGgG gGg GGggGgggggggGGG GGggGGGgGggGggGGGgGGGGgGGGgGGggGgGGgG gGGgGggGGgGgGg? GgggGgggggggGGgGgG GgggGGGggggGGgGGgGG ggGggGGGG gggGggggGgGGGGg GGgggGGGgGgGgGGGGgGgG!

## [2018-07-11] Challenge #365 [Intermediate] Sales Commissions 

### Description

You're a regional manager for an office beverage sales company, and right now you're in charge of paying your sales team they're monthly commissions.

Sales people get paid using the following formula for the total commission: commission is 6.2% of profit, with no commission for any product to total less than zero.

### Input Description

You'll be given two matrices showing the sales figure per salesperson for each product they sold, and the expenses by product per salesperson. Example:

    Revenue 

            Frank   Jane
    Tea       120    145
    Coffee    243    265

    Expenses

            Frank   Jane
    Tea       130     59
    Coffee    143    198

### Output Description

Your program should calculate the commission for each salesperson for the month. Example:


                    Frank   Jane
    Commission       6.20   9.49

### Challenge Input

    Revenue

                Johnver Vanston Danbree Vansey  Mundyke
    Tea             190     140    1926     14      143
    Coffee          325      19     293   1491      162
    Water           682      14     852     56      659
    Milk            829     140     609    120       87

    Expenses

                Johnver Vanston Danbree Vansey  Mundyke
    Tea             120      65     890     54      430
    Coffee          300      10      23    802      235
    Water            50     299    1290     12      145
    Milk             67     254      89    129       76

### Challenge Output

                Johnver Vanston Danbree Vansey  Mundyke
    Commission       92       5     113     45       32

### Credit

I grabbed this challenge from Figure 3 of an APL\3000 overview in a [1977 issue of HP Journal](http://www.hpl.hp.com/hpjournal/pdfs/IssuePDFs/1977-07.pdf). If you have an interest in either computer history or the APL family of languages (Dyalog APL, J, etc) this might be interesting to you. 

## [2019-03-13] Challenge #376 [Intermediate] The Revised Julian Calendar

### Background

[The Revised Julian Calendar](https://www.timeanddate.com/calendar/revised-julian-calendar.html) is a calendar system very similar to the familiar Gregorian Calendar, but slightly more accurate in terms of average year length. The Revised Julian Calendar has a leap day on Feb 29th of leap years as follows:

* Years that are evenly divisible by 4 are leap years.
* Exception: Years that are evenly divisible by 100 are not leap years.
* Exception to the exception: Years for which the remainder when divided by 900 is either 200 or 600 are leap years.

For instance, 2000 is an exception to the exception: the remainder when dividing 2000 by 900 is 200. So 2000 is a leap year in the Revised Julian Calendar.

### Challenge

Given two positive year numbers (with the second one greater than or equal to the first), find out how many leap days (Feb 29ths) appear between Jan 1 of the first year, and Jan 1 of the second year in the Revised Julian Calendar. This is equivalent to asking how many leap years there are in the interval between the two years, including the first but excluding the second.

    leaps(2016, 2017) => 1
    leaps(2019, 2020) => 0
    leaps(1900, 1901) => 0
    leaps(2000, 2001) => 1
    leaps(2800, 2801) => 0
    leaps(123456, 123456) => 0
    leaps(1234, 5678) => 1077
    leaps(123456, 7891011) => 1881475

For this challenge, you must handle very large years efficiently, much faster than checking each year in the range.

    leaps(123456789101112, 1314151617181920) => 288412747246240

### Optional bonus

Some day in the distant future, the Gregorian Calendar and the Revised Julian Calendar will agree that the day is Feb 29th, but they'll disagree about what year it is. Find the first such year (efficiently).