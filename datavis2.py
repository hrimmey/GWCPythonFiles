import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from statistics import mean

# This gets the data from the JSON file
tweetFile = open("TwitterData.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

polarity = []
subjectivity = []

# This creates a loop that gets the polarity and subjectivity from each text in the JSON file

for i in tweetData:
    tb = TextBlob(i["text"])
    polarity.append(tb.polarity)
    subjectivity.append(tb.subjectivity)

# Textblob sample:
print(mean(polarity and subjectivity))


# This is the code for the histogram
plt.hist(polarity, bins = [-0.5, 0, 0.5, 1])
plt.xlabel('Polarity')
# How frequently tweets fall within this range
plt.ylabel('Frequency')
plt.title('Polarit Histogram')
plt.show()

plt.hist(subjectivity, bins = [-0.5, 0, 0.5, 1])
plt.xlabel('Subjectivity')
# How frequently tweets fall within this range
plt.ylabel('Frequency')
plt.title('Polarit Histogram')
plt.show()
