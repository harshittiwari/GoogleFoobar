def answer(heights):
    index = 0
    waterHeight = 0
    state = 0
    sIndex = -1
    lenHeights = len(heights)
    nHeights = heights[:]
    while index < lenHeights - 1:
        #print("on:" + str(heights[index]))
        if heights[index] > heights[index + 1]:
            state = 1
            sIndex = index
        elif heights[index] < heights[index + 1]:
            state = 0
            if sIndex >= 0 and heights[sIndex] >= heights[index]:
                waterHeight += fill(heights,sIndex,index + 1,nHeights)
                sIndex = -1
        index += 1
        #print("waterHeight:" + str(waterHeight))
        #print("state:" + str(state))
        #print("sIndex:" + str(sIndex))
        #print("nHeights:" + str(nHeights))
        #time.sleep(5)

    if sIndex >= 0:
        waterHeight += fill(heights,sIndex,index - 1,nHeights)

    #time.sleep(1000000)
    return waterHeight + (0 if waterHeight == 0 else answer(nHeights))

def fill(heights,sIndex,index,nHeights):
    #print("FILL")
    i = sIndex if heights[sIndex] < heights[index] else index
    #print("i:" + str(i))
    waterHeight = 0
    for j in range(sIndex + 1,index):
        waterHeight += heights[i] - heights[j]
        nHeights[j] = heights[i]
    return waterHeight

#state = 0 increasing
#state = 1 decreasing
def main():
    li = [1,4,2,5,1,2,3]
    print(answer(li))

    li = [5,4,3,3,4,3,2,2,5]
    print(answer(li))

if __name__ == '__main__':
    main()