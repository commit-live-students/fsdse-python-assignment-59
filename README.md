# Write a function to find numbers divisible by two numbers.
Define a function that takes 3 parameters(all positive integers) in this order:
num1, num2, end_num

Function should return a list of all numbers less than end_num that are divisible by both num1 and num2.

_Example:_

**Input:**


    2, 3, 13
    

**Output:**


    [6, 12]
    
    
_Challenge:_
Write the function without using for-loop.

ANSWER:----

#include <bits/stdc++.h> 
using namespace std; 
  
int countDivisibles(int A, int B, int M) 
{ 
    //Variable to store the counter 
    int counter = 0; 
  
    // Running a loop from A to B and check 
    // if a number is divisible by M. 
   for (int i = A; i <= B; i++) 
        if (i % M == 0) 
            counter++; 
  
   return counter; 
} 
  
// Driver code 
int main() 
{ 
    //A and B define the range, M is the dividend 
    int A = 30, B = 100, M = 30; 
  
    // Printing the result 
   cout << countDivisibles(A, B, M) << endl; 
  
   return 0; 
} 
