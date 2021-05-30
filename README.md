<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="400" height="400">
  </a>

  <h3 align="center">Algo Showcase</h3>

  <p align="center">
  Illustration by <a href="https://icons8.com/illustrations/author/5dbc313c01d03600167c33bc">Thierry Fousse</a> from <a href="https://icons8.com/illustrations">Ouch!</a>
  
<br />
</p>
<br />

<!-- ABOUT THE PROJECT -->

## About The Project

This repository contains a collection of algorithms and solutions to exercises from codewars. Feel free to take a look a the directory to jump to any problem or solution.

<!-- TABLE OF CONTENTS -->
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ul>
    <!---------------------------- -->
<li>
      <a href="https://github.com/DZuko/Algo-Showcase/blob/main/code/rail_fence_cipher.py">Rail Fence Cipher</a>
      <ul>
        <li>
Create two functions to encode and then decode a string using the Rail Fence Cipher. This cipher is used to encode a string by placing each character successively in a diagonal along a set of "rails". First start off moving diagonally and down. When you reach the bottom, reverse direction and move diagonally and up until you reach the top rail. Continue until you reach the end of the string. Each "rail" is then read left to right to derive the encoded string.
</li>
      </ul>
    </li>
        <br/>
<!------------------------------>
    <li>
      <a href="https://github.com/DZuko/Algo-Showcase/blob/main/code/rot13.py">Rotate 13</a>
      <ul>
        <li>ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher. Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".</li>
      </ul>
    </li>
        <br/>
<!-- -------------------------- -->
<li>
      <a href="https://github.com/DZuko/Algo-Showcase/blob/main/code/hamming_numbers.py">Hamming Numbers</a>
      <ul>
        <li>
A Hamming number is a positive integer of the form 2i3j5k, for some non-negative integers i, j, and k. Write a function that computes the nth smallest Hamming number.
</li>
      </ul>
    </li>
        <br/>
<!-- -------------------------- -->
<li>
      <a href="https://github.com/DZuko/Algo-Showcase/blob/main/code/snail.py">Snail</a>
      <ul>
        <li>
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.  
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]. <a href="https://miro.medium.com/max/702/1*f3yEq5LHQIq0Vk2K_9kuRw.png">See this image as a visual example.</a>   
</li>
      </ul>
    </li>
        <br/>
<!-- -------------------------- -->
<li>
      <a href="https://github.com/DZuko/Algo-Showcase/blob/main/code/explosive_sum.py">Explosive Sum</a>
      <ul>
        <li>
In number theory and combinatorics, a partition of a positive integer n, also called an integer partition, is a way of writing n as a sum of positive integers. 
Two sums that differ only in the order of their summands are considered the same partition. If order matters, the sum becomes a composition. 
For example, 4 can be partitioned in five distinct ways.  Write a function to find the amount of ways to partition an integer.
</li>
      </ul>
    </li>
    <br/>
<!-- -------------------------- -->
<li>
      <a href="https://github.com/DZuko/Algo-Showcase/blob/main/code/twice_linear.py">Twice Linear</a>
      <ul>
        <li>
Consider a sequence u where u is defined as follows:
The number u(0) = 1 is the first one in u.
For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
There are no other numbers in u.
Example:
u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...

Task:
Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered sequence u (ordered with < so there are no duplicates).

</li>
      </ul>
    </li>
    <br/>
<!-- -------------------------- -->
<li>
      <a href="https://github.com/DZuko/Algo-Showcase/blob/main/code/bit_counting.py">Bit Counting</a>
      <ul>
        <li>
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative. Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case.
</li>
      </ul>
    </li>
        <br/>

<!-- -------------------------- -->
<li>
      <a href="https://github.com/DZuko/Algo-Showcase/blob/main/code/range_extraction.py">Range Extraction</a>
      <ul>
        <li>
A format for expressing an ordered list of integers is to use a comma separated list of either individual integers or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.
</li>
      </ul>
    </li>
        <br/>
<!-- -------------------------- -->
   <li>
      <a href="https://github.com/DZuko/Algo-Showcase/blob/main/code/digital_root.py">Digital Root</a>
      <ul>
        <li>Digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has more than one digit continue reducing in this way until a single-digit number is produced. 
 The input will be a non-negative integer.</li>
      </ul>
    </li>
        <br/>
<!-- -------------------------- -->
<li>
      <a href="https://github.com/DZuko/Algo-Showcase/blob/main/code/counting_car_mileage.py">Counting Car Mileage</a>
      <ul>
        <li>
Let's make it so Bob never misses another interesting number. We've hacked into his car's computer, and we have a box hooked up that reads mileage numbers. We've got a box glued to his dash that lights up yellow or green depending on whether it receives a 1 or a 2 (respectively).

It's up to you, intrepid warrior, to glue the parts together. Write the function that parses the mileage number input, and returns a 2 if the number is "interesting" (see below), a 1 if an interesting number occurs within the next two miles, or a 0 if the number is not interesting.

Interesting numbers are 3-or-more digit numbers that meet one or more of the following criteria:

Any digit followed by all zeros: 100, 90000
Every digit is the same number: 1111
The digits are sequential, incementing†: 1234
The digits are sequential, decrementing‡: 4321
The digits are a palindrome: 1221 or 73837
The digits match one of the values in the awesome_phrases array

</li>
      </ul>
    </li>
        <br/>
<!-- -------------------------- -->
<li>
      <a href="https://github.com/DZuko/Algo-Showcase/blob/main/code/counting_duplicates.py">Counting Duplicates</a>
      <ul>
        <li>
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
</li>
      </ul>
    </li>
        <br/>
<!-- -------------------------- -->
<li>
      <a href="https://github.com/DZuko/Algo-Showcase/blob/main/code/find_the_missing_letter.py">Find the missing letter </a>
      <ul>
        <li>
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array. You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2. The array will always contain letters in only one case. Example: ['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'
</li>
      </ul>
    </li>
        <br/>
<!-- -------------------------- -->
<li>
      <a href="https://github.com/DZuko/Algo-Showcase/blob/main/code/hashtag_generator.py">Hashtag Generator</a>
      <ul>
        <li>
 The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator! Here's the deal: It must start with a hashtag (#). All words must have their first letter capitalized. If the final result is longer than 140 chars it must return false. If the input or the result is an empty string it must return false.
</li>
      </ul>
    </li>
        <br/>
<!-- -------------------------- -->
<li>
      <a href="https://github.com/DZuko/Algo-Showcase/blob/main/code/pep8_variable_converter.py">Pep8 Variable Converter</a>
      <ul>
        <li>
Write simple pep8 variable converter method  All words must have a "_" between them.
</li>
      </ul>
    </li>
    <br/>
<!-- -------------------------- -->
<li>
      <a href="https://github.com/DZuko/Algo-Showcase/blob/main/code/available_ingredients.py">Available Ingredients</a>
      <ul>
        <li>
Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.
</li>
      </ul>
    </li>
<!-- -------------------------- -->
