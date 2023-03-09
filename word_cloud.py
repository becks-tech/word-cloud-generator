# Import necessary libraries
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Text data
def choose_file():
    text = input("filename: ")
    with open(text,'r') as f:
        text = f.read()
        return text

# Generate word cloud
def customize_wordcloud():
    bg_color = input("background color: ")
    font = int(input("font size: "))
    wordcloud = WordCloud(background_color=bg_color, max_font_size=font).generate(choose_file())
    return wordcloud

# Save word cloud
def save_cloud():
    file_name = input("enter file name to save: ")
    return file_name

# Plot word cloud
plt.imshow(customize_wordcloud(), interpolation='bilinear')
plt.axis("off")
plt.savefig(save_cloud())
plt.show()
