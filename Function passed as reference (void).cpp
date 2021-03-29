#include <iostream>
#include <math.h> // adding the math.h library to use sqrt
using namespace std;

void f1(double x, int N, double& Z) // Use Z as reference
{
    while (N >= 0) // Loop to go amount of N times
    {
        Z = Z + (1/sqrt(x+N)); // the equation
        N--; // to stop the loop after the number of N times
    }

}


int main()
{
    double x,Z,result; // declaring
    int N; // declaring
    
    cout<<"Enter positive value for x: "; // prompt the user to enter something
    cin >> x; // user's input stored in x 
    
    cout<<"Enter positive value for N: "; // same like the previouse
    cin >> N; // same like the previouse
    
    f1(x,N,Z); // calling the function and now the Z is updated and passed as reference
    
    result = Z; // storing the passed variable into result variable
    cout << "Result: " << result; // printing
    return 0;
}
