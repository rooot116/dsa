#include<iostream>
using namespace std;
#define max 100
int a[max],n,s,low=0,high,mid;
void binary_search(int a[],int n,int s)
{ 
    high=n;
   while(low<=high)
    {
        mid=(low+high)/2;
        if(a[mid]==s)
        {
            cout<<"element found at "<<mid+1<<" position"<<endl;
            break;
        }
        else if(a[mid]>s)
            high=mid-1;
        else 
            low=mid+1;
    }
    if(low>high)
    cout<<"element not there in the list"<<endl;
}
int main()
{
 cout<<"enter size of the array";
 cin>>n;
 cout<<"enter the elements"<<endl;
 for(int j=0;j<n;j++)
      cin>>a[j];
 cout<<"enter the element to be found"<<endl;
 cin>>s;
 binary_search(a,n,s);
}