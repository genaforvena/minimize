#!/usr/bin/env python3

import random

def generate_random_matrix(k, l):
    for letter in ["A", "B", "C", "D"]:
        with open(letter + 'ij', 'w') as file:
            for i in range(0, k):
                string = ""
                for j in range(0, l):
                    if j == l - 1:
                        string += repr(random.uniform(-1, 1))
                    else:
                        string += repr(random.uniform(-1, 1)) + " "
                file.write(string + "\n")

if __name__ == "__main__":
    k = 10
    l = 10
    generate_random_matrix(k, l)
