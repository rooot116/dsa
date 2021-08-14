#include <iostream>
using namespace std;
int main()
{
    int r, c, a[100][100], b[100][100], sum[100][100], i, j;
    cout << "Enter number of rows : ";
    cin >> r;
    cout << "Enter number of columns : ";
    cin >> c;
    cout << endl << "Enter elements of 1st matrix: " << endl;

    for(i = 0; i < r; ++i)
       for(j = 0; j < c; ++j)
       {
           cout << "Enter element a" << i + 1 << j + 1 << " : ";
           cin >> a[i][j];
       }
    cout << endl << "Enter elements of 2nd matrix: " << endl;
    for(i = 0; i < r; ++i)
       for(j = 0; j < c; ++j)
       {
           cout << "Enter element b" << i + 1 << j + 1 << " : ";
           cin >> b[i][j];
       }

    // Adding Two matrices
    for(i = 0; i < r; ++i)       //order of O(n^2)
        for(j = 0; j < c; ++j)
            sum[i][j] = a[i][j] + b[i][j]; //space i,j,r,c-4 r*c+r*c if r=c O(r^2)

    // Displaying the resultant sum matrix.
    cout << endl << "Sum of two matrix is: " << endl;
    for(i = 0; i < r; ++i)
        for(j = 0; j < c; ++j)
        {
            cout << sum[i][j] << "  ";
            if(j == c - 1)
                cout << endl;
        }

    return 0;
}