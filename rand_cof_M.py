#!/usr/bin/env python3

import random

if __name__ == "__main__":
    with open('random.txt','w') as file:
        k = 10
        l = 10
        for i in range(0, k):
            string = ""
            for j in range(0, l):
                if j == l - 1:
                    string += repr(random.uniform(-1, 1))
                else:
                    string += repr(random.uniform(-1, 1)) + " "
            file.write(string + "\n")
