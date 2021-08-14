#include <iostream>
using namespace std;
int euclid(int a, int b)
{
    int r;
    while(b != 0)        //space-O(1) a,b,r-1
    {
         r = a % b; 
         a = b; 
         b = r; 
    }
    return a; 
}
 int main()
{
    int a ,b;
    cin>>a>>b;
   cout<<"gcd of two numbers is "<<euclid(a, b);
   return 0;
}
