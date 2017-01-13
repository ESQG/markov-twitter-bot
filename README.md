This is a very primitive Markov bot I made with a classmate.  It would be better with more evenly sized text files, and bigger ones--but WARNING: I didn't optimize for memory at all.  (In the future I'll look into weighted selection methods.)  There's also a bit of asymmetry when using multiple files.

To run this script to make a bot, you need a verified Twitter account, to make an app, and to store the four keystrings it gives you into your shell environment.

For those less familiar with shell commands (as I was until the day before we made this), you need a file secrets.sh which must contain the following four lines, fill in your keys (no spaces!):

export TWITTER_CONSUMER_KEY="blah"
export TWITTER_CONSUMER_SECRET_KEY="blah"
export TWITTER_ACCESS_TOKEN_KEY="blah"
export TWITTER_ACCESS_TOKEN_SECRET="blah"

Then to put these variables into your shell environment so the Python script can use them, you type the command to run secrets.sh as a shell script:

source secrets.sh

(You can also run letsdothis.sh instead, which will do that, and run the Python script for 2-grams in all .txt files in the directory.)

To run the bot script, provide at least one file name, and an integer n (1 or more) for ngram length.  For example:

python our_markov.py gettysburg.txt tom_sawyer.txt 2

For the length and number of files I've provided, 2 is the best; 3 is too inflexible as there isn't enough data.

Outputs a tweet after posting it.

$ python markov.py tom_sawyer.txt 2
Tom? Now you get to the judge; but his own clothing forlornly. "I reckon I was so brim-full of exultation that was really worthy the name.

Or:
$ python markov.py gettysburg.txt tom_sawyer.txt 2

She makes me feel so bad to think he said in a degree which he thanked the widow hunted for him outside till his ears flapped again.