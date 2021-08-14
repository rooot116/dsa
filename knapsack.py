def fractional_knapsack(profit, weight, capacity):
    index = list(range(len(profit)))
    ratio = [p/w for p, w in zip(profit, weight)]
    index.sort(key=lambda i: ratio[i], reverse=True)
 
    max_value = 0
    fractions = [0]*len(profit)
    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_value += profit[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity/weight[i]
            max_value += profit[i]*capacity/weight[i]
            break
 
    return max_value, fractions
 
 
n = int(input('Enter number of items: '))
profit = input('Enter the values of the {} item(s) in order: '.format(n)).split()
profit = [int(p) for p in profit]
weight = input('Enter the positive weights of the {} item(s) in order: '.format(n)).split()
weight = [int(w) for w in weight]
capacity = int(input('Enter maximum weight: '))
max_value, fractions = fractional_knapsack(profit, weight, capacity)
print('The maximum profit of items that can be carried:', max_value)
print('The fractions in which the items should be taken:', fractions)