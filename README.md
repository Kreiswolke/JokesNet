# JokesNet

##### 1) First task: Building a database of oneliner jokes.
##### 1.1) onelinefun.com -> Completed {~2700 items}
##### 1.2) funn2.com -> Completed {~300 items}
##### 1.3) jokesoftheday.net -> Completed, but site's html code is very inconsistent and further exceptions might have to be added {~7000 items}

##### 2) Train a network to produce funny jokes
##### 2.1) Train an LSTM model on the oneliner jokes corpus: -> Done using https://github.com/sherjilozair/char-rnn-tensorflow implementation, Results are rather mixed so far:
##### 2.1.1) Problems: - Generated words are readable but misspellings still likely 
##### - The content is often i) confusing ii) not funny iii) lacking consistent oneliner properties(e.g. 'Q: What is a ...?' But 'A: ...' is missing)
##### -> Corpus too small and generally basic word-relations are not covered (which results in a seemingly random concatenation of words) 
#### Idea: Use a progressive network approach: First train network on basic text data (e.g. wikipedia) and then add a network extension trained on the oneliner jokes task
