import praw
import time
import re
from collections import Counter

WORDS_DISPLAY = 25
reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("all")
submission = subreddit.stream.comments()

for comment in submission:
    if comment.body == "!word":
        wordlist = []
        post = reddit.submission(comment.submission)
        post.comments.replace_more(limit=9999, threshold=0)
        all_comments = post.comments.list()
        x = 0

        for comment1 in all_comments:
            text = list(filter(None, re.split('[;,. \*\n]',
                                              comment1.body.lower())))
            wordlist = wordlist + text
            x = x + 1

        print(str(x))
        wordfreq = Counter(wordlist)
        reply = "**WORD**  |**FREQUENCY** \n:------|:------ \n"
        for word, freq in wordfreq.most_common(WORDS_DISPLAY):
            reply = reply + word + "| " + str(freq) + " \n"
        reply = reply + "\n\n^I ^am ^a ^bot."

        comment.reply(reply)
        time.sleep(5)
