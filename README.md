# Binary Code

One of the more mysterious concepts in computer science is binary code. Even though it is a fundamental building block concerning how computers function, programmers today can get away without a deep understanding of how it works. By the end of this lesson, you'll have that advantage!

### Prerequisites

For this lesson you'll need to have _Python 2.7_ installed. If you're on Mac or Linux, this should already be preinstalled on your system. If you're on Windows, you may need to [download it](http://www.python.org/download/releases/2.7.6/).

## Coding Example

Let's jump right into some code. Create a new Python file called `binary_example1.py`. Type this into it:

```py
num = 1
print num

for i in range(11):
	num = num << 1
	print num
```

Run it, and you'll see that this is what you get:

```sh
$ python binary_example1.py
1
2
4
8
16
32
64
128
256
512
1024
2048
```

I bet you're wondering what that `<<` thing does... We’ll get into that in a little while.

__Does anybody recognize those numbers from anywhere?__

## Game Time

Now, hop over to this game called [2048](http://gabrielecirulli.github.io/2048/). Play it for a little while. The objective is to use the arrow keys to move the numbers and combine (add) the matching ones together. It can be addicting, so don't get too carried away! ;)

After you've played it for a bit, you may start to notice a similarity between the numbers in the game and the Python code we just wrote.

__Why are the numbers in the game the same ones that came out of our Python program?__

I will give you a hint... Instead of thinking about the game as `2 + 2`, `4 + 4`, `8 + 8`, etc., think about it as `2 * 2`, `2 * 4`, `2 * 8`, and so on.

## 1s and 0s

By now you may be thinking, "I thought we were supposed to be learning about binary code! I thought that was all made up of `1`s and `0`s!" If you _are_ thinking that, you're exactly right! The difference is between how those numbers look to you and how they look to the computer.

__What, then, is binary code?__

Binary code is what you probably already think it is: sequences of `1`s and `0`s. It might look like `10011001` or `10101010`. But since we are humans, that code doesn't really mean anything to us! Also, why were we playing with `2`s, `4`s, and `8`s when binary is only made up of `0` and `1`?

Let's focus on answering a couple of key questions:

* Why is binary code made up of `1`s and `0`s?
* What does the binary code mean?

## Why is binary code made up of 1s and 0s?

The answer to this question goes back to how the very first computers where built. The most important piece of the answer is a little device called a **[transistor](http://en.wikipedia.org/wiki/Transistor)**.

A **transistor** is a switch, except transistors also have the ability to amplify the signal that is going into them. Because a transistor is a _switch_, it can either be `OFF` or `ON` (Just like a light switch at home). Because a transistor is an _amplifier_, many of them can be connected together in a circuit without the signal dying. You can put however many transistors you want into a circuit and the signal will still make it to the finish line.

It's not too much of a jump then to see how `0` is like `OFF`, and how `1` is like `ON` (You might have also seen other paired values in programming like `NO`/`YES` or `false`/`true`). This means that a transistor has the ability to _store data_, but it can only store a value of `0` or `1`. That's actually okay, because a computer designer could use as many transistors in a computer as he wants.

So that is the basics of how transistors came to be used in computer hardware. Having a bunch of `0`s and `1`s around may not seem to have an obvious use. We are about to look at how **the ability to store multiple `0`s and `1`s is incredibly powerful.**

## What does the binary code mean?

### Every piece of data has a binary representation

Let's look at `binary_example1.py` again.

```py
num = 1
print num

for i in range(11):
	num = num << 1
	print num
```

So, about that `<<` thing. `<<` is actually an _operator_ much like `+`, `-`, `*` or `/`. However, while `+-*/` are _arithmetic operators_, `<<` is a _bitwise operator_. It is called **left shift**, and it operates on the _underlying binary representation_ of the number to the left of `<<`. What this implies is that **for every number** (`1`, `2`, `3`, `4`, ...), **there is a binary code equivalent**.

How do we know what that binary code is? Well, `0` and `1` are freebies, because they are already part of the **binary number system** (which is made up of `0`s and `1`s). However, binary code is usually represented in groups of 8. So, the binary representation of `0` is `00000000`, and the binary representation of `1` is `00000001`.

A **bit** is an individual `0` or `1` in the binary code. A group of 8 bits is called an **octet**. A **byte** stores one **octet**, or 8 **bits**.

The **left shift operator** (`<<`) takes the binary version of the number to the left of the operator and _shifts_ all of the **bits** to the left. The number of places to shift is determined by the number to the right of the `<<` operator. So, `num << 1` just means _"shift `num`'s bits `1` place to the left"_.

So throughout our program, the variable `num` is backed by these values:

```py
00000001 # num = 1
00000010 # num = num << 1
00000100 # num = num << 1
00001000 # num = num << 1
00010000 # num = num << 1
00100000 # num = num << 1
01000000 # num = num << 1
10000000 # num = num << 1
```

See how the `1` bit shifts to the left with every cycle of the `for` loop? We can map these **octets** to our program output to see how they match up.

```py
00000001 # 1
00000010 # 2
00000100 # 4
00001000 # 8
00010000 # 16
00100000 # 32
01000000 # 64
10000000 # 128
...
```

What about `256`, `512`, `1024` and `2048`? Python knows that it needs another **byte** to store those larger numbers, so we get another **octet** to left shift into.

```py
00000000 00000001 # 1
00000000 00000010 # 2
00000000 00000100 # 4
00000000 00001000 # 8
00000000 00010000 # 16
00000000 00100000 # 32
00000000 01000000 # 64
00000000 10000000 # 128
00000001 00000000 # 256
00000010 00000000 # 512
00000100 00000000 # 1024
00001000 00000000 # 2048
```

Now we need to understand why the position of the `1` bit determines which number it represents.

## The Binary Number System

Let's make a new Python file and call it `binary_example2.py`. It's going to be a lot like our first example, but we are going to replace the **left shift** with another expression.

```py
num = 1
print num

for i in range(11):
	num = num * 2
	print num
```

**What do you think this program outputs?** Here's a hint: remember how after we played the _2048_ game I said to think about the numbers as `2 * 2`, `2 * 4`, `2 * 8`, and so on? Lo and behold!

```sh
$ python binary_example2.py
1
2
4
8
16
32
64
128
256
512
1024
2048
```

By using a mathematical device called a [**change of base**](http://en.wikipedia.org/wiki/Radix), binary values can be used to express more complex values than `0` and `1`.

#### Take a deep breath, it's time for some math!

Our natural counting system is more precisely called the **decimal system**, and it has a base of `10`. Bases work off of the position of the _digits_ in the number. The number of potential digits in a base is equal to the value of the base, so base 10 has 10 possible digits it can express numbers with. The digits always include `0`. If you count how many numbers are between `0` and `9`, you'll find there are `10`, so `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]` is the digit set for base 10.

To figure out the decimal value of a number in a different base, the value of each digit is multiplied by the base to the power of the digit's position (The _position_ of the digit
is 0 at the far right, then increases to the left). Then all those are added together. "To the power of" just means multiplying a number by itself that many times. This is called an __exponent__.

Let's explain the decimal number `123`. We are going to convert it from base 10 to base 10, so the number won't actually change, but breaking it down will help explain the concept:

* 3 is in the 0th positon, 2 is in the 1st position, 1 is in the 2nd position.
* The value of the 0th digit is `3`, and the base is 10, so its decimal value is `3 * 10 ^ 0`, or `3 * 1`. Any number to the 0th power is `1`. `3 * 1` equals `3`
* The value of the 1st digit is `2`, so its decimal value is `2 * 10 ^ 1`, or `2 * 10`, which equals `20`.
* The value of the 2nd digit is `1`, so its decimal value is `1 * 10 ^ 2`, or `1 * 10 * 10`, which equals `100`.
* Now we add them all together:

```
 100
  20
+  3
----
 123
````

The **binary system** is base 2, which contains only 2 digits including `0`. That only leaves room for one more, the digit `1`. These are our transistors!

Let's look at an example binary octet, `00101010`, and convert it to decimal:

* The value of the 0th digit is `0`, so its decimal value is `0` since any number times 0 equals 0.
* The value of the 1st digit is `1`, so its decimal value is `1 * 2 ^ 1`, or `1 * 2`, which equals `2`.
* The value of the 2nd digit is `0`
* The value of the 3rd digit is `1`, so its decimal value is `1 * 2 ^ 3`, or `1 * 2 * 2 * 2`, which equals `8`.
* The value of the 4th digit is `0`
* The value of the 5th digit is `1`, so its decimal value is `1 * 2 ^ 5`, or `1 * 2 * 2 * 2 * 2 * 2`, which equals `32`.
* The value of the 6th and 7th digits are `0`
* Now we add them all together, and since we are adding we can ignore the `0`s:

```
 32
  8
+ 2
---
 42 (the meaning of life, the universe and everything!)
```

# Storing Things Besides Numbers

So now we know how we can use the **binary number system** to express large numbers with just `1`s and `0`s. Well, even though numbers are useful and all, humans think in terms of words. Raw numbers don't leave us with a way to express readable text in a way that the computer can store.

Computer scientists were trying to solve this exact problem about 50 years ago. Computers needed to support the uppercase alphabet (26 characters), the lowercase alphabet (26 characters), numerals (10 characters), plus punctuation and special characters. Computers didn't have a lot of storage space at the time, so the scientists needed to figure out a way to fit a way to express those characters in the smallest amount of space per character.

It turned out that **8 bits** could store 256 different combinations (Binary `11111111` is equal to the decimal number 255), and so eventually **8 bits** became the compromise between space and flexibility for storing a single character.

So letters on a computer are just an illusion! At least an illusion as far as the computer is concerned.

Here's our last example, `binary_example3.py`. I am using the `ord()` and `chr()` functions to find the number value for a character, messing with that
number, then turning it back into a character.

```py
letter_a = "A"
letters = []

print "UPPER:"
for i in range(26):
  idx = ord(letter_a)
  new_letter = chr(idx + i)
  letters.append(new_letter)
  print new_letter

print "\nlower:"
for letter in letters:
  idx = ord(letter)
  shifted = idx + 32        # Why does adding 32 make it lowercase?
  new_letter = chr(shifted)
  print new_letter
```

Run the program and see what it does. What is so significant about adding 32? Well, there is a standard mapping of numbers to characters called
ASCII. [Check out the table](http://www.asciitable.com/) and see those numbers for yourself.

# Conclusion

Now you have a grasp of how computers handle binary code, and how binary code relates to computer data we humans can understand. We have just covered the basics here, and there are other different ways that different types of data are represented in binary. If you _really_ want to melt your brain,
check out how [floating point numbers](http://en.wikipedia.org/wiki/Floating_point) work!
