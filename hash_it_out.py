# digest[i] = ( ( 129 * message[i] ) XOR message[i-1] ) % 256

def inverseDigest(digest, prevMessage):
    #print("inversing:" + str(digest) + " with " + str(prevMessage))
    message = -1
    calcDigest = -1
    i = 0
    while calcDigest != digest:
        message = int(((digest + (256 * i)) ^ prevMessage) / 129)
        calcDigest = ((129 * message) ^ prevMessage) % 256
        i+=1
    return message

def answer(digest):
    message = []
    for i in range(len(digest)):
        if i == 0:
            message.append(inverseDigest(digest[i],0))
        else:
            message.append(inverseDigest(digest[i],message[i - 1]))
    return message

def main():
    li = [0,129,3,129,7,129,3,129,15,129,3,129,7,129,3,129]
    print(answer(li))

    li = [0,129,5,141,25,137,61,149,113,145,53,157,233,185,109,165]
    print(answer(li))

if __name__ == '__main__':
    main()