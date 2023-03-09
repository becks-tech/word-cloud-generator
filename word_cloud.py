# Import necessary libraries
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Sample text data
def choose_file():
    text = input("filename: ")
    with open(text,'r') as f:
        text = f.read()
        return text

# Generate word cloud
bg_color = input("background color: ")
wordcloud = WordCloud(background_color=bg_color).generate(choose_file())

# Plot word cloud
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
