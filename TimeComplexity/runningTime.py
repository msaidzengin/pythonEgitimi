import time


def main():

    for i in range(100):
        print(i)


if __name__== "__main__":

    startTime = time.time()
    main()
    endTime = time.time()

    totalTime = endTime - startTime
    print('Time:', totalTime)
