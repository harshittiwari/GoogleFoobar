class Name(object):
    def __init__(self, name):
        self.name = name
        self.lname = name.lower()
        self.score = 0
        self.CalculateScore()

    def CalculateScore(self):
        for ch in self.lname:
            self.score += ord(ch) - 96

def answer(names):
    li = [Name(x) for x in names]
    QuickSort(li, 0, len(li)-1)
    return [x.name for x in li]

def QuickSort(li, start, end):
    if start < end:
#             print ("quick sort called on:" + str(li[start:end + 1]))
        sep = Partition(li, start, end)
#             print ("sep:" + str(sep))
        QuickSort(li, start, sep - 1)
        QuickSort(li, sep + 1, end)

def Partition(li, start, end):
    x = li[end]
    y = start - 1
    for i in range(start, end):
        if li[i].score > x.score or (li[i].score == x.score and li[i].lname > x.lname):
#                 print(str(li[i]) + "<=" + str(x))
            y += 1
            li[y], li[i] = li[i], li[y]
            continue           
    li[end], li[y + 1] = li[y + 1], li[end]
    return y + 1

def main():
    li = ["annie", "bonnie", "liz"]
    print (answer(li))

    li = ["abcdefg", "vi"]
    print (answer(li))


if __name__ == '__main__':
    main()