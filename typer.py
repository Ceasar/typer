"""
Start a timer for N seconds.

Type as many words as you can.

Then get stats. Also get any words you missed or that were slow.

You can use this to improve your typing. It can remember which words you're bad
at and train you.

There could also be some like machine-learning thing to try to teach you how
best to type or which you need to practice?

Doesn't just need to be words. It can be typing out sentences as well. Perhaps
even code. Then you can improve your code speed. We can also compare stats with
friends.

All at the command line.

It could even store data as file on your computer.

Maybe let user set max length.
"""
import os
import random
import time
import string

DICTIONARY = '/usr/share/dict/words'
with open('prideandprejudice.txt') as fp:
    words = [line.strip(string.whitespace) for line in fp.read().split('\n')]
    words = [line for line in words if len(line) > 1]

words_tried = 0
word_wins = 0
total_letters = 0
old_wpm = 0
wpm = 0
time_elapsed = 0
previous_time_elapsed = 0

words_typed = []

os.system('clear')
raw_input("Type words as fast as you can.")
start_time = time.time()
counter = 0
while True:
    os.system('clear')
    word = words[counter]
    for word_typed_wpm in words_typed:
        word_typed, line_typed, word_wpm, line_total_letters, line_time_taken = word_typed_wpm
        print("{}, {}, WPM: ({:02.2f}), Letters: {}, Time taken: {:03.2f}, Line WPM: {:02.2f}".format(
            "+" if word_typed == line_typed else "-",
            word_typed,
            word_wpm,
            line_total_letters,
            line_time_taken,
            int((line_total_letters / 5.0) / (line_time_taken / 60.0))
        ))
    if words_tried > 0:
        improvement = wpm - old_wpm
        print("WPM: {:02.2f} ({:02.2f}), Time elapsed: {}, Total letters: {}, Accuracy: {}%".format(wpm, improvement, int(time_elapsed), total_letters, accuracy))
    print(word)
    line = raw_input()
    line_words = list(line.split())
    words_tried += len(line_words)
    for prompt_word, line_word in zip(word.split(), line_words):
        if prompt_word == line_word:
            total_letters += len(line_word)
            word_wins += 1
    previous_time_elapsed = time_elapsed
    time_elapsed = time.time() - start_time
    time_taken = time_elapsed - previous_time_elapsed
    accuracy = int(float(word_wins) / words_tried * 100)
    lpm = int(total_letters / time_elapsed)
    if words_tried > 1:
        old_wpm = wpm
    wpm = int((total_letters / 5.0) / (time_elapsed / 60.0))
    words_typed.append((word,line,wpm,len(line),time_taken))
    counter += 1
