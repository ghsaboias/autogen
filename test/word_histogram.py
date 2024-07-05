# Count the words in a text and display them as a histogram

from collections import Counter
import matplotlib.pyplot as plt

text = """
Insert your text with at least 500 words here...
"""

# Split text into words
words = text.split()

# Count the occurrences of each word
word_counts = Counter(words)

# Prepare data for histogram
words = list(word_counts.keys())
counts = list(word_counts.values())

# Plot the histogram
plt.figure(figsize=(15, 6))
plt.bar(words, counts)
plt.xlabel('Words')
plt.ylabel('Counts')
plt.xticks(rotation=90)
plt.show()
