import wikipedia

from wordcloud import WordCloud,STOPWORDS

import matplotlib.pyplot as plt

# 위키백관 사전의 컨텐츠 제목을 명시
wiki = wikipedia.page('MachineLearning')
# 이 페이지의 텍스트 컨텐츠를 추출
text = wiki.content

# 중지어 제외  (중지어 : 특별한 의미를 갖는다고 보기 힘든 단어어)
s_words = STOPWORDS.union({'one','two','using','first','make','ise'})

# wordcloud 생성
wordcloud = WordCloud(width = 2000,height = 1500,
                      stopwords=s_words).generate(text)

plt.figure(figsize=(40,30))
# 화면에 이미지를 그려줌
plt.imshow(wordcloud)
plt.show()