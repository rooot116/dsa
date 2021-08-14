#include<iostream>
using namespace std;
int a[10],n,s,i;
void linear_search(int a[],int n,int s)
{  int i;
    for(i=0;i<n;i++)
    {
        if(a[i]==s)
        {
        cout<<"element found at "<<i+1<<" position"<<endl;
        break;
        }
    }
    if(i==n)
    cout<<"element not there in the list"<<endl;
}
int main(){
    cout<<"enter the size"<<endl;
    cin>>n;
    cout<<"enter the elements"<<endl;
    for(int j=0;j<n;j++)
    cin>>a[j]; 
    cout<<"enter the element for searching"<<endl;
    cin>>s;
    linear_search(a,n,s);
}