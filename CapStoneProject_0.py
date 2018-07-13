import nltk
import matplotlib.pyplot as plt
from nltk.tokenize import RegexpTokenizer
import seaborn as sns

# text processing goes through the followng steps :
# 1-tokenize the text in single words
# 2-put all the words in lower case
# 3- remove stop words such as

# read the file
with open('job_skills.csv',  'r') as myfile:
  article = myfile.read()

# instantiate a tokenizer with RegexpTokenizer and use it to create tokens (words) from the text
tokenizer = RegexpTokenizer('\w+')
tokens = tokenizer.tokenize(article)
print(tokens)

# create list of lower case tokens
words = []

# Loop through list tokens and make lower case
for word in tokens:
    words.append(word.lower())


# remove stopwords such as 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're"

sw = nltk.corpus.stopwords.words('english')
print(sw[:10])

# Initialize new list that will contain text without stop words
words_ns = []

# Add to words_ns all words that are in words but not in sw
for word in words:
    if word not in sw:
        words_ns.append(word)

# Print several list items as sanity check
print(words_ns[:20])

# adjust the plot margins.
plt.subplots_adjust(left=0.15, bottom=0.25, right=0.9, top=0.8)

# Figures inline and set visualization style
# matplotlib inline
sns.set()

# Create freq dist and plot
freqdist1 = nltk.FreqDist(words_ns)
freqdist1.plot(25)



