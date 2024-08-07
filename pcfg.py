# -*- coding: utf-8 -*-
"""PCFG.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jtqx7H4svuEyVCGdKCf7Zp-hUbVJEPT4
"""

import pickle

class Rule:
    def __init__(self, left, right, probability):
        self.left = left
        self.right = right
        self.probability = probability

def find_rule_with_word(terminal):
    return [rule for rule in rules if terminal in rule.right]

def find_possible_combinations(x, y):
    return [((x, i), (i+1, y)) for i in range(x, y)]

Z = int(input("Enter no of rules: "))
rules = []
for i in range(Z):
    print("-" * 10)
    print(f"Rule {i+1}")
    key = input("Enter left side of the rule: ").upper()
    value = input("Enter right side of the rule in single string: ").upper().split()
    probability = float(input("Enter probability of the rule: "))
    rule = Rule(key, value, probability)
    rules.append(rule)

pickle.dump(rules, open("rules.data", "wb"))

rules = pickle.load(open("rules.data", "rb"))
words = [input(f"Enter word {i+1}: ").upper() for i in range(int(input("Enter no of words: ")))]

matrix = [[[] for j in range(len(words))] for i in range(len(words))]
for i in range(len(words)):
    for j in range(len(words)):
        if i + j < len(words):
            if i == 0:
                matrix[j][j] = find_rule_with_word(words[j])
            else:
                x = j
                y = i + j
                data = []
                for k in find_possible_combinations(x, y):
                    for left in matrix[k[0][0]][k[0][1]]:
                        for right in matrix[k[1][0]][k[1][1]]:
                            for rule in rules:
                                if rule.right == [left.left, right.left]:
                                    probability = left.probability * right.probability * rule.probability
                                    data.append(Rule(rule.left, rule.right, probability))
                matrix[x][y] = data

if len(matrix[0][-1]) > 0 and all(rule.left == "S" for rule in matrix[0][-1]):
    prob = sum(rule.probability for rule in matrix[0][-1])
    print(f"The probability of the input sentence is {prob}")
else:V0T
    print("The input sentence is not valid according to the grammar rules.")