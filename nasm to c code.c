#include <stdio.h>
#include <stdlib.h>

// Had to read and understand assembly language code and then convert the nasm into C, and so this is the outcome.

int fun1(char var1)
{
    if (var1 == 'm') // checking if var1 is equal to m
    {
        fun2m(); // calling fun2m if they were equal
    }
    
    fun2a(1,3); // calling function while "pushing" 1 and 3 (Pushing according to nasm)
}

int fun2m(int var2) 
{
    int var4 = 2; // initializing var4 with 2
    int var5 = var2; // initializing var5 with the passed parameter
    
    var4 = var4 * var5; // multypilying and re-assigning the var4 with new value
    
    fun3(var4); // calling the function and passing the multiplied numbers
    
    
    
}

int fun2a(int num1, int num2) // num1 and num2 are the numbers that were "pushed"
{
    int var2 = num1; // using the passed paramaters to assign to var 2 
    int var3 = num2; // using the passed paramaters to assign to var 3 
    
    var2 = var2 + var3; // adding the 2 numberes
    
    fun2m(var2); // calling the function and passing the addition of the 2 numbers
}

int fun3(int var) // this function prints
{
    printf("%s = %d", "var", var); // prints and uses the passed paramter in it.
}


int main() // the _start of the nasm
{
    char var1 = 'a';
    fun1(var1); // calling the function fun1 and passing the var1 which contains char 'a'

    return 0;
}
