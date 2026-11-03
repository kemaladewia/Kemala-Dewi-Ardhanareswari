glossary = {
    'variable' : 'A name that refers to a value stores in memory.',
    'string' : 'A series of characters, written inside quotes.',
    'list' : 'A collection of items in a particular order.',
    'loop' : 'A way to run the same block of code repeatedly.',
    'tuple' : 'A list whose items cannot be changed.',
    'dictionary' : ' A collection of key-value pairs.',
    'conditional test' : ' An expression that evaluates to True or False.',
    'slice' : 'A spesific group of items taken from a list.',
    'comment' : 'A note in a program that Phyton ignores.',
    'list comprehension' : 'A compact way to build a list in one line.',
}

for word, meaning in glossary.items():
    print(f"{word.title()}: {meaning}\n")