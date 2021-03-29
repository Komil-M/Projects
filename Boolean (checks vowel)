#include <iostream>

using namespace std;

bool isVowel(char c) // 
{
    char vowels [5] = {'a','e','i','o','u'}; // array containing a char list of vowels
    
    for (int i = 0; i > 5; i++) // loop that loops through the array in order to compare
    {
        if (i==c) // compares the array index with user input
        {
            
            return true; // returns true if a char matches with the user's input
        }
    
        else
        {
            
            return false; // returns false if it doesn't.
        }
    }
}

int main()
{
    bool output;
    char c;
    cout<<"Enter a character: "; // prompts the user for an input (c)
    cin >> c;
    
    output = isVowel(c); // calls the function and passes the input, 
                         //returns the bool answer and saves it in output variable
    
    if (output == true) // checks if the function returns true
    {
        cout << "Vowel"; 
    }
    
    else
    {
        cout << "Not Vowel";
    }
    

    return 0;
}

