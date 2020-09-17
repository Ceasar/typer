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

with open('/usr/share/dict/words') as fp:
    words = fp.read().split()

start_time = time.time()
words_tried = 0
word_wins = 0
total_letters = 0
old_wpm = 0
os.system('clear')
raw_input("Type words as fast as you can.")
while True:
    os.system('clear')
    word = random.choice(words)
    if words_tried > 0:
        improvement = wpm - old_wpm
        print("I: {:02.2f}, WPM: {:02.2f}, Time elapsed: {}, Total letters: {}, Accuracy: {}%".format(improvement, wpm, int(time_elapsed), total_letters, accuracy))
    print(word)
    line = raw_input()
    words_tried += 1
    if line == word:
        total_letters += len(word)
        word_wins += 1
    time_elapsed = time.time() - start_time
    accuracy = int(float(word_wins) / words_tried * 100)
    lpm = int(total_letters / time_elapsed)
    if words_tried > 1:
        old_wpm = wpm
    wpm = int(total_letters / 5) / (time_elapsed / 60)
