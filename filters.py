from contrast import *
import random
import math
# pepper and salt filter
# we can easily see that the median filter is better than the avererage filter when 
# the noise is of type pepper and salt
# the best size of the median filter for image 2 is "5*5" but it generates a "blur"
def addingNoise(arr, height, width):
    resultArr = np.zeros((height, width), dtype=int)
    for i in range(height):
        for j in range(width):
            n = random.randint(0, 20)
            if n == 0:
                resultArr[i][j] = 0
            elif n == 20:
                resultArr[i][j] = 255
            else:
                resultArr[i][j] = arr[i][j]
    # plt.clf()
    # image = plt.imshow(Image.fromarray(arr))
    # plt.show()  # do not forget to add block = false
    # image = plt.imshow(Image.fromarray(resultArr))
    # plt.show()  # do not forget to add block = false
    return resultArr

# average filter


def averageFilter(arr, height, width, n):
    # assert n % 2 ==1
    resultArr = np.zeros((height, width), dtype=int)
    # averageFilter = np.ones((n, n), dtype=int)
    # print(averageFilter)
    endLine = height - n//2
    endColumn = width - n//2
    i = n//2
    while i < endLine:
        j=n//2
        while j < endColumn:
            # print((i,j))
            newVal=0
            for l in range(n):
                for k in range(n):
                    newVal+= arr[i-n//2+l][j-n//2+k]
            resultArr[i][j]=int(newVal/(n*n))
            j += 1
        i += 1
    newVal=0
    # print(resultArr)
    # plt.imshow(Image.fromarray(resultArr))
    # plt.show()  # do not forget to add block = false
    return  resultArr


def medianFilter(arr, height, width, n):
    resultArr = np.zeros((height, width), dtype=int)
    # averageFilter = np.ones((n, n), dtype=int)
    # print(averageFilter)
    endLine = height - n//2
    endColumn = width - n//2
    i = n//2
    while i < endLine:
        j=n//2
        while j < endColumn:
            median=[]
            for l in range(n):
                for k in range(n):
                    median.append(arr[i-n//2+l][j-n//2+k])
            median.sort()
            resultArr[i][j]=median[len(median)//2+1]         
            j += 1
        i += 1
    # plt.imshow(Image.fromarray(resultArr))
    # plt.show()  # do not forget to add block = false
    return  resultArr

# SNR: Signal to Noise Ratio
def calculateSNR(originalImg,processedImg,height,width):
    (meanOriginal,STDOriginal)=meanSTD(originalImg)
    part2=0
    for i in range(height):
        for j in range(width):
            part2+=((processedImg[i][j])**2)
    snr=(STDOriginal*(height*width))/(math.sqrt(part2))
    print(snr)
    print(snr)


def highPassFilter(arr, height, width):
    hightFilter = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
    resultArr = np.zeros((height, width), dtype=int)
    #print(hightFilter)
    n=3
    endLine = height - n//2
    endColumn = width - n//2
    i = n//2
    while i < endLine:
        j=n//2
        while j < endColumn:
            newVal=0
            for l in range(n):
                for k in range(n):
                    newVal+= arr[i-n//2+l][j-n//2+k]*hightFilter[l][k]
            resultArr[i][j]=int(newVal)
            j += 1
        i += 1
    # plt.imshow(Image.fromarray(arr))
    # plt.show()  # do not forget to add block = false
    # plt.imshow(Image.fromarray(resultArr))
    # plt.show()  # do not forget to add block = false
    return resultArr


# noisedArr=addingNoise(arr, height, width)
# arr1=averageFilter(noisedArr, height, width, 3)
# calculateSNR(arr, arr1, height, width)

# arr2=medianFilter(noisedArr, height, width, 5)
# calculateSNR(arr, arr2, height, width)
# arr2=medianFilter(noisedArr, height, width, 3)
# calculateSNR(arr, arr2, height, width)

# highPassFilter(arr, height, width)