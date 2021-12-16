# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from wordcloud import WordCloud, STOPWORDS
import pandas as pd
import glob
import matplotlib.pyplot as plt
header_list = ["Keyword", "Frequency"]

path = r"/Users/matthew/PycharmProjects/pythonProject4/covidmay"
all_files = glob.glob(path + "/*.csv")
li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, names=header_list)
    li.append(df)

data1 = pd.concat(li, axis=0, ignore_index=True)
S = set(
    ["china", "wuhan", "wuhanvirus", "hate", "democrats", "trump", "fuck", "fucking", "realdonaldtrump", "ass", "iran",
     "lies", "shit", "chinese", "biden", "russia", "fake", "japan", "korea", "india", "asiavirus", "damn"])

d = {}
for a, x in data1.values:
    a = str(a).lower()
    #     d[a] +=  int(x)
    dig = int(x)
    if (a in S):
        if (a in d):
            d[a] += dig
        else:
            d[a] = dig
print(d)

comment_words = "";
stop_words = ["nan", "get"]

# wordcloud = WordCloud()
# wordcloud.generate_from_frequencies(d)
# plt.figure()
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.show()


final_wordcloud = WordCloud(width=800, height=800,
                            background_color='black',
                            stopwords=STOPWORDS.add("nan"),
                            min_font_size=10).generate_from_frequencies(frequencies=d)
# Displaying the WordCloud
plt.figure(figsize=(10, 10), facecolor=None)
plt.imshow(final_wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()