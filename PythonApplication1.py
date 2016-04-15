# 1 was boolean can manage seven minion and each minion can manage seven minion. how many minions can work for a height of h

#2-1 loop in graph
def answer(numbers):
    li = []
    index = 0
    while(numbers[index] not in li):
        index = numbers[index]
        li.append(index)
    return len(li) - li.index(numbers[index])

numbers = [1, 2, 3, 5, 6, 1]
print (answer(numbers))