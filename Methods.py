from mpmath import *
from chaoticMaps import *
from sympy import *
import pickle
import os

precision = 1000
mp.dps = precision

def find_final(seq):

    i = len(str(seq)) - 1
    while i > 0 and str(seq)[i] == '0':
        i = i - 1
    return i


def lastDigits(x, nlast):

    x = Float(str(x), precision/2)
    indexSix = find_final(x)
    x = str(x)[2:indexSix+1]

    return mpf('0.' + str(x)[-nlast : ])


def iteration_logistic(x0, u, accuracy):

    if len(str(x0)) - 2 > accuracy:
        x = lastDigits(x0, accuracy)

    else:
        x = x0
    x = logistic(u, x)

    if len(str(x)) - 2 > accuracy:
        x = lastDigits(x, accuracy)
    return x


def cycles(x0, u, accuracy, max_position):

    # Create the directory
    newpath = './results' 
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    cyclespath = f'./results/cycles_u{str(u)[-1]}'
    if not os.path.exists(cyclespath):
        os.makedirs(cyclespath)

    freqpath = f'./results/frequency_u{str(u)[-1]}'
    if not os.path.exists(freqpath):
        os.makedirs(freqpath)

    for n in range(1, max_position + 1):
        if (n > accuracy):
            return False
        
        isNotEqual = True
        i = 1

        while isNotEqual:
            x = x0
            vec = []

            while len(str(x)) - 2 < n:
                x = iteration_logistic(x, u, accuracy)

            for _ in range(54):
                x = iteration_logistic(x, u, accuracy)

            for _ in range(i):
                x = iteration_logistic(x, u, accuracy)
                vec.append(str(x)[-n])

            vecCurr = []
            for _ in range(i):
                x = iteration_logistic(x, u, accuracy)
                vecCurr.append(str(x)[-n])

            if vecCurr == vec:
                isNotEqual = False
                file = open(cyclespath + f'/x{x0}u{u}.txt', 'a')
                file.write("Position: " + str(n) + "\n" +
                           "Sequence: " + ''.join(vecCurr) + "\n" +
                           "Period: " + str(i) + "\n\n")
                file.close()

                file = open(freqpath + f'/{str(n)}.pkl', 'wb')
                pickle.dump(str(''.join(vecCurr)), file)
                file.close()
                
            i = i + 1

def float_correct(x, k):
    x = Float(str(x), k)
    if len(str(x)) - 2 > k:
        x = str(x)[ : 2 + k]
    else:
        x = str(x)
    return x

def fixed(u, max_fixed_iteration, iteration_compare):
    # Create the directory
    newpath = './results' 
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    fixedpath = f'./results/fixed_u{str(u)[-1]}'
    if not os.path.exists(fixedpath):
        os.makedirs(fixedpath)
    
    xfixed = mpf("0.1")
    for _ in range(9):
        size_compare = []
        k = 1 + iteration_compare

        xfixed_tmp = xfixed

        for _ in range(max_fixed_iteration):
            xcurr = xfixed_tmp / 10
            step = mpf("0.1")
            y = mpf("0.0")

            for j in range(10):
                y = xcurr 
                for p in range(iteration_compare):
                    y = iteration_logistic(y, u, k)

                if str(y) == float_correct(xcurr, k):
                    file = open(fixedpath + f'/classes _u{u}.txt', 'a')
                    file.write(str(y) + "\n")
                    file.close()
                    size_compare.append(str(y))
                    xfixed_tmp = xcurr
                xcurr += step
            k = k + 1

        for i in range(len(size_compare) - 1):
            for j in range(i + 1, len(size_compare)):
                if len(size_compare[i]) == len(size_compare[j]):
                    xfixed_tmp = mpf(size_compare[i])
                    k_temp = len(size_compare[i]) - 2
                    for _ in range(max_fixed_iteration):
                        xcurr = xfixed_tmp / 10
                        step = mpf("0.1")
                        y = mpf("0.0")

                        for j in range(10):
                            y = xcurr 
                            for p in range(iteration_compare):
                                y = iteration_logistic(y, u, k_temp)

                            if str(y) == float_correct(xcurr, k_temp):
                                file = open(fixedpath + f'/classes _u{u}.txt', 'a')
                                file.write(str(y) + "\n")
                                file.close()
                                xfixed_tmp = xcurr
                            xcurr += step
                        k_temp = k_temp + 1
                        
        xfixed += mpf("0.1")


def save_iteration(x0, number_iterations, u, accuracy):
    # Create the directory
    newpath = './results' 
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    iterpath = f'./results/iteration'
    if not os.path.exists(iterpath):
        os.makedirs(iterpath)

    x = x0
    for i in range(number_iterations):
        x = iteration_logistic(x, u, accuracy)
        file = open(iterpath + f'/x{x0}u{u}.txt', 'a')
        file.write(f"iteration {i + 1} : {x}\n")
        file.close()


def frequency_experiment(u, s_f, max_position):
    
    freqpath = f'./results/frequency_u{str(u)[-1]}'
    if not os.path.exists(freqpath):
        print("You need to run the period experiment")
    
    else:

        for n in range(s_f + 2, max_position + 1):
            file = freqpath + f"/{str(n)}.pkl"
            with open(file, 'rb') as f:
                vec = pickle.load(f)

            avg = 0

            file = open(freqpath + '/mainCycle.txt', 'a')
            file.write((30 * "#") + "\n")
            file.write(f"Postion: {str(n)} \n")
            file.write((30 * "#") + "\n\n")

            for i in range(10):
                freq = 0
                for j in vec:
                    if (str(i) == j):
                        freq += 1

                file.write(f"Digit: {i}\n" +
                            f"Frequency: {freq}\n\n")
                avg += freq

            avg /= 10

            file.write(f"Average: {avg}\n\n\n")
            file.close()