import wikipedia
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
wiki = wikipedia.page('MachineLearning')
text = wiki.content
s_words = STOPWORDS.union({'one','two','using','first','make','ise'})
wordcloud = WordCloud(width = 2000,height = 1500,
                      stopwords=s_words).generate(text)

plt.figure(figsize=(40,30))
plt.imshow(wordcloud)
plt.show()