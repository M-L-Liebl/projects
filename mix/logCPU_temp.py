"""
Logs the CPU temperature a predefined time, displays temperature in graph afterwards

MAKE SURE THAT log() greps the right line and get_Temps() get the right temperature (regex...)
"""

import os
import sys
import time
import re
import matplotlib.pyplot as plt


def init_log():
    with open('log','w') as f:
        f.write("")


def log():
    os.system('sensors | grep CPU >> log') # check if right line is grepped

def get_Temps()->list[float]:
    with open('log', 'r') as f:
        lines = f.readlines()
    # check if correct regex for temperature
    temps = [float(re.search(r'\+([0-9]{2}.[0-9])°C',line.strip()).group(1)) for line in lines]
    return temps[1:]

def plot_Temp(temps):
    x = [i for i in range(1,len(temps)+1)]
    plt.plot(x,temps, 'o-')
    plt.xlabel("time in seconds")
    plt.ylabel("temperature in °C")
    plt.grid()
    plt.show()

# Print iterations progress
def printProgressBar (iteration, total, prefix = ' ', suffix = ' ', decimals = 1, length = 100, fill = '#', printEnd = '\r'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str), e.g. █
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()


if __name__=="__main__":
    init_log()
    t = int(sys.argv[1])
    for i in range(t):
        log()
        time.sleep(1)
        printProgressBar(i+1, t)
        
    plot_Temp(get_Temps())