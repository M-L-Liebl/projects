#!/usr/bin/env python3

import random
import time

def createlist()->list:
    result = []
    for i in range(1_000_000):
        result.append(random.randint(1,10_000_000))
    return result


def quicksort(liste:list) -> list:
    if len(liste) <= 1:
        return liste
    else:
        lower = [li for li in liste if li < liste[0]]
        upper = [li for li in liste if li > liste[0]]
        return quicksort(lower) + [liste[0]] + quicksort(upper)


if __name__=="__main__":
    start = time.time()
    liste = createlist()
    print(liste[0:20])
    liste_sorted = quicksort(liste)
    print("\n-----------------\n")
    print(liste_sorted[0:20])
    end = time.time()
    print(f"time: {end-start}")
