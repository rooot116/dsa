#include<iostream>
using namespace std;

int max(int a, int b) { 
	return (a > b)? a : b; 
} 

int knapsack(int W, int w[], int V[], int n) 
{
	if (n == 0 || W == 0) 
		return 0; 
	
	if (w[n-1] > W) 
		return knapsack(W, w, V, n-1); 
	
	else 
		return max( V[n-1] + knapsack(W-w[n-1], w, V, n-1), knapsack(W, w, V, n-1) ); 
} 

int main() 
{
	int w[] = {5, 4, 6, 3};  
	int V[] = {10, 40, 30, 50};    
	int  W = 10; 
	int n = 4;
	int Max;

    cout<<"Profit\tWeight\t\n"<<endl;
	for (int i = 0; i < n; i++) 
	{ 
		cout<<V[i]<<"\t"<<w[i]<<endl;
	}

cout<<"\n"<<endl;
	Max = knapsack(W, w, V, n); 
	cout<<"Maximum profit we can obtain usiing 0/1 knapsack = "<< Max<<endl;
	return 0; 
} 
