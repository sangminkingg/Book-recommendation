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
##### ✔ 상위 10위 도서별 이용횟수
- Rich Shapero 작가의 "wildAnimus" 가 가장 이용률이 높게 나왔다.  
- 가장 많이 이용한 도서는 차례로 WildAnimus by Rich Shapero , The Davinchi Code by Dan Brown, The Lovely Bones: A Novel, Divine Secrets of the Ya-Ya Sisterhood: A Novel by Alice Sebold 이다. 
""")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기

df_popbook = pd.read_csv('data/popbooks.csv')
df_popbook
fig1, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='N_ratings', y='Book-Title', data=df_popbook,palette='Set1')

# x축 레이블 90도 회전
ax.set_xticklabels(ax.get_xticklabels(), rotation=50)

# 그래프 제목 추가
ax.set_title('Top10 Books most read by users', fontsize=16)

# 그래프 표시하기
st.pyplot(fig1)

st.write('')
st.write('')




st.write("""
##### ✔ 상위 10위 도서별 평균 평점
- 도서당 평점의 갯수의 평균이 3.57이므로 N_ratings(이용 후기 개수)가 4 개이상 중 가장 평점좋은 도서는 다음과 같다

""")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기

df_avg = pd.read_csv('data/goodratingbooks.csv')

fig3, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='avg_rating', y='Book-Title', data=df_avg,palette='Set1')

# x축 레이블 90도 회전
ax.set_xticklabels(ax.get_xticklabels(), rotation=50)

# 그래프 제목 추가
ax.set_title('Top10 Books most read by users', fontsize=16)

# 그래프 표시하기
st.pyplot(fig3)

st.write('')
st.write('')
js = "window.scrollTo(0, document.getElementById('part-2-location-analysis').offsetTop);"




