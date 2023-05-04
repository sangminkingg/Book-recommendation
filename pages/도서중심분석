import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt
import plotly.express as px


st.header('📖출판사분석')


st.sidebar.markdown("""
    ## 출판사 분석
    - [part 1. 도서 분석](#part-1-book-analysis)
    - [part 2. 작가 분석](#part-2-author-analysis)
    - [part 3. 출판년도 분석](#part-3-year_publication-analysis)
    - [part 4. 출판사 분석](#part-4-publisher-analysis)
""")
st.write('')
st.write("""
- 출판사나 도서 기업의 입장에서 도서 평점을 활용한 분석이다. 출판사/도서기업이 가지고 있는 고객 데이터와 평점 등을 통해 출판사/도서기업의 데이터가 고객의 평점에 어떠한 영향을 미치는지를 분석하여 고객의 선호도를 분석한다.
""")
st.write('')
st.write('')


js = "window.scrollTo(0, document.getElementById('part-1-age-analysis').offsetTop);"

    
st.markdown("<h3 id='part-1-age-analysis'>✅Part 1. 도서 분석</h3>", unsafe_allow_html=True)

st.write('')
st.write('')
st.write("""
- 예를들어 Harry Potter 단어가 포함된 단어를 찾으면 해당 정보를 아래와 같이 찾을 수 있음
- 같은 책이라도 에디션에 따라 나뉘는 종류가 다르게 경우가 있다
""")

st.write("""
##### ✔ 상위 10위 도서별 평점수
- Wild Animus 책이 21번으로 가장 많은 평점이 달렸습니다.
- 그 뒤로 Where the Heart Is (Oprah's Book Club (Paperback)), The Da Vinci Code, The Red Tent (Bestselling Backlist) 등이 다음 평점 수를 기록했다.
""")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기

df_book = pd.read_csv('data/popbooks.csv')

fig1, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='N_ratings', y='Book-Title', data=df_book,palette='Set1')

# x축 레이블 90도 회전
ax.set_xticklabels(ax.get_xticklabels(), rotation=50)

# 그래프 제목 추가
ax.set_title('Top10 Books most read by users', fontsize=16)

# 그래프 표시하기
st.pyplot(fig1)
