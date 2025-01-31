

import random

def main():
  append_random_numbers([])
  append_random_words([])

def append_random_numbers(list, quantity=1):
  for _ in range(quantity):
    list.append(round(random.uniform(10, 100), 1))

def append_random_words(list, quantity=1):
  emotions = [
    "happiness",
    "sadness",
    "anger",
    "fear",
    "love",
    "surprise",
    "disgust",
    "excitement",
    "pride",
    "shame",
    "guilt",
    "contentment",
    "anxiety",
    "hope",
    "relief",
    "envy",
    "jealousy",
    "compassion",
    "boredom",
    "gratitude"
  ]
  for _ in range(quantity):
    list.append(random.choice(emotions))

if __name__ == '__main__':
  main()
  