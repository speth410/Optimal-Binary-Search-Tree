import random
import numpy as np
import pandas as pd
import datetime

def main():


    # 10 Keys
    p,q = generateProbability(10)

    startTime = datetime.datetime.now()

    e,w,root = optimalBST(p,q,10)

    endTime = datetime.datetime.now()
    executionTime = ((endTime - startTime).total_seconds())
    print("Completed OBST on 10 Keys in ", executionTime, "seconds.\n")

    output(e,w,root)

    # 100 Keys
    p,q = generateProbability(100)

    startTime = datetime.datetime.now()

    e,w,root = optimalBST(p,q,100)

    endTime = datetime.datetime.now()
    executionTime = ((endTime - startTime).total_seconds())
    print("Completed OBST on 100 Keys in ", executionTime, "seconds.\n")

    output(e,w,root)

    # 1000 Keys
    p,q = generateProbability(1000)

    startTime = datetime.datetime.now()

    e,w,root = optimalBST(p,q,1000)

    endTime = datetime.datetime.now()
    executionTime = ((endTime - startTime).total_seconds())
    print("Completed OBST on 1000 Keys in ", executionTime, "seconds.\n")

    output(e,w,root)

    # 10000 Keys
    p,q = generateProbability(10000)

    startTime = datetime.datetime.now()

    e,w,root = optimalBST(p,q,10000)

    endTime = datetime.datetime.now()
    executionTime = ((endTime - startTime).total_seconds())
    print("Completed OBST on 10000 Keys in ", executionTime, "seconds.\n")

    output(e,w,root)

    # 100000 Keys
    p,q = generateProbability(100000)

    startTime = datetime.datetime.now()

    e,w,root = optimalBST(p,q,100000)

    endTime = datetime.datetime.now()
    executionTime = ((endTime - startTime).total_seconds())
    print("Completed OBST on 100000 Keys in ", executionTime, "seconds.\n")

    output(e,w,root)

    # 1000000 Keys
    p,q = generateProbability(1000000)

    startTime = datetime.datetime.now()

    e,w,root = optimalBST(p,q,1000000)

    endTime = datetime.datetime.now()
    executionTime = ((endTime - startTime).total_seconds())
    print("Completed OBST on 1000000 Keys in ", executionTime, "seconds.\n")

    output(e,w,root)

    

def optimalBST(p,q,n):
    e = np.zeros((n+2,n+1))
    w = np.zeros((n+2,n+1))
    root = np.zeros((n+1,n+1))

    for i in range(1,n+2):
        e[i,i-1] = q[i-1]
        w[i,i-1] = q[i-1]
    for l in range(1,n+1):
        for i in range(1,n-l+2):
            j = i + l - 1
            e[i,j] = float('inf')
            w[i,j] = w[i,j-1] + p[j] + q[j]
            for r in range(i, j+1):
                t = e[i,r-1] + e[r+1,j] + w[i,j]
                if (t < e[i,j]):
                    e[i,j] = t
                    root[i,j] = r

    return e, w, root


def generateKeys(n):
    keys = []
    for i in range(n):
        keys.append(random.randrange(n))

    return keys

def generateProbability(n):
    p = np.zeros([n+1])
    q = np.zeros([n+1])

    probs = np.zeros([n*2+1])

    for i in range(n*2+1):
        probs[i] = random.random()

    #Adjust probability values so that the sum of all probs = 1
    total = sum(probs)
    
    for i in range(n*2+1):
        probs[i] = probs[i] / total
    
    #Assign p and q
    for i in range(n):
        p[i+1] = probs[i]

    for i in range(n+1):
        q[i] = probs[n+i]

    return p,q

def output(e,w,root):
    df = pd.DataFrame(e)
    df.to_csv("e_%d.csv" % len(e))

    df = pd.DataFrame(w)
    df.to_csv("w_%d.csv" % len(w))

    df = pd.DataFrame(root)
    df.to_csv("root_%d.csv" % len(root))


if __name__ == '__main__':
    main()