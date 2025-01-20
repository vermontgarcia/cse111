"""
Author: Vermont Garcia
Program: sentences
Purpose: Write a Python program that generates simple English sentences.

Milestone Requirements:
  Program must generate English sentences with four parts:
    - a determiner
    - a noun
    - a verb

Final Requirements:
  Program must generate English sentences with four parts adding:
    - a prepositional phrase

  To complete this prove assignment, your program must include at least these seven functions:

    - main
    - make_sentence
    - get_determiner
    - get_noun
    - get_verb
    - get_preposition
    - get_prepositional_phrase

Stretching and Exceeding Requirements:
  - Program add an additional call to include an additional prepositional phrase
  - Add functions:
    - get_adverv
    - get_adjective 

"""

import random

def main():
  tenses = ['past', 'present', 'future']
  quantities = [1,2]

  for i in range(len(quantities)):
    for j in range(len(tenses)):
      print(make_sentence(i, tenses[j]))
    

def get_determiner(quantity):
  """
    Return a randomly chosen determiner.
      A determiner is a word like "the", "a", "one", "some", "many".
        If quantity is 1, this function will return either 
          "a", "one", or "the".
        Otherwise this function will return either
          "some", "many", or "the".
    Parameter
      quantity: an integer.
          If quantity is 1, this function will return a determiner for a single noun.
          Otherwise this function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
  """
  if quantity == 1:
      words = ["a", "one", "the"]
  else:
      words = ["some", "many", "the"]
  # Randomly choose and return a determiner.
  word = random.choice(words)
  return word

def get_noun(quantity):
  """
    Return a randomly chosen noun.
      If quantity is 1, this function will return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"
      Otherwise, this function will return one of these ten plural nouns:
        "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"
    Parameter
      quantity: an integer that determines if the returned noun is single or plural.
    Return: a randomly chosen noun.
  """
  if quantity == 1:
    nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
  else:
    nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
  return random.choice(nouns)

def get_adjective():
  """
    Return a randomly chosen adjective from this list of adjectives:
      "beautiful", "brave", "clever", "friendly", "generous", "happy", "honest", "kind", "lazy", "loud",
      "modern", "mysterious", "powerful", "quiet", "quick", "serious", "shy", "strong", "tidy", "wise"
    Return: a randomly chosen adjective.
  """
  adjectives = [
    "beautiful",
    "brave",
    "clever",
    "friendly",
    "generous",
    "happy",
    "honest",
    "kind",
    "lazy",
    "loud",
    "modern",
    "mysterious",
    "powerful",
    "quiet",
    "quick",
    "serious",
    "shy",
    "strong",
    "tidy",
    "wise"
  ]
  return random.choice(adjectives)

def get_verb(quantity, tense):
  """
    Return a randomly chosen verb.
      If tense is "past", this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"
      If tense is "present" and quantity is 1, this function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"
      If tense is "present" and quantity is NOT 1, this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"
      If tense is "future", this function will return one of these ten verbs:
        "will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"
    Parameters
      quantity: an integer that determines if the returned verb is single or plural.
      tense: a string that determines the verb conjugation, either "past", "present" or "future".
    Return: a randomly chosen verb.
  """
  match tense:
    case 'past':
      tense = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    case 'future':
      tense = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    case 'present':
      if quantity == 1:
        tense = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
      else:
        tense = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
  return random.choice(tense)

def get_adverb():
  """
    Return a randomly chosen adverb from this list of adverbs:
      "quickly", "slowly", "softly", "loudly", "happily", "sadly", "brightly", "calmly", "eagerly", "gently",
      "bravely", "carefully", "quietly", "kindly", "lazily", "angrily", "beautifully", "patiently", "nervously", "wisely"
    Return: a randomly chosen adverb.
  """
  adverbs = [
    "quickly",
    "slowly",
    "softly",
    "loudly",
    "happily",
    "sadly",
    "brightly",
    "calmly",
    "eagerly",
    "gently",
    "bravely",
    "carefully",
    "quietly",
    "kindly",
    "lazily",
    "angrily",
    "beautifully",
    "patiently",
    "nervously",
    "wisely"
  ]
  return random.choice(adverbs)

def get_preposition():
  """
    Return a randomly chosen preposition from this list of prepositions:
      "about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
      "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over",
      "past", "to", "under", "with", "without"
    Return: a randomly chosen preposition.
  """
  prepositions = [
    "about",
    "above",
    "across",
    "after",
    "along",
    "around",
    "at",
    "before",
    "behind",
    "below",
    "beyond",
    "by",
    "despite",
    "except",
    "for",
    "from",
    "in",
    "into",
    "near",
    "of",
    "off",
    "on",
    "onto",
    "out",
    "over",
    "past",
    "to",
    "under",
    "with",
    "without"
  ]
  return random.choice(prepositions)

def get_prepositional_phrase(quantity):
  """
    Build and return a prepositional phrase composed of three words:
      a preposition,
      a determiner,
      and a noun
    by calling the get_preposition, get_determiner, and get_noun functions.
    Parameter
      quantity: an integer that determines if the determiner and noun in the prepositional phrase
        returned from this function should be single or pluaral.
    Return: a prepositional phrase.
  """
  preposition = get_preposition()
  determiner = get_determiner(quantity)
  noun = get_noun(quantity)

  return f'{preposition} {determiner} {noun}'

def make_sentence(quantity, tense):
  """
    Build and return a sentence with three words: 
      a determiner,
      an adjective,
      a noun,
      an adverb,
      a verb,
      and two prepositional phrases

    The grammatical quantity of the determiner and noun will match the number in the quantity parameter.
    The grammatical quantity and tense of the verb will match the number and tense in the quantity and tense parameters.
  """

  determiner = get_determiner(quantity)
  adjective = get_adjective()
  noun = get_noun(quantity)
  adverb = get_adverb()
  verb = get_verb(quantity, tense)
  prepositional_phrase = get_prepositional_phrase(quantity)
  prepositional_phrase_two = get_prepositional_phrase(quantity)

  return f'{determiner} {adjective} {noun} {prepositional_phrase} {adverb} {verb} {prepositional_phrase_two}'.capitalize()

main()