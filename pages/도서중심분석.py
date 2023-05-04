import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt
import plotly.express as px


st.header('📖도서 중심 분석')


st.sidebar.markdown("""
    ## 도서 중심 분석
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



js = "window.scrollTo(0, document.getElementById('part-1-book-analysis').offsetTop);"

    
st.markdown("<h3 id='part-1-book-analysis'>✅Part 1. 도서 분석</h3>", unsafe_allow_html=True)

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
- 도서당 평점의 갯수의 평균이 3.57이므로 N_ratings(이용 후기 개수)가 4 개 기준 가장 평점좋은 도서는 다음과 같다

""")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기

df_goodrating = pd.read_csv('data/goodratingbooks.csv')
df_goodrating


st.write('')
st.write('')



js = "window.scrollTo(0, document.getElementById('part-1-book-analysis').offsetTop);"

    
st.markdown("<h3 id='part-2-author-analysis'>✅Part 2.  분석</h3>", unsafe_allow_html=True)

st.write('')
st.write('')


st.write("""
##### ✔ 유저들이 가장 많이 찾은 상위10 인기 작가 
- 유저들의 도서 이용 횟수 기준 상위 작가는 Stephen King(8467회), Nora Roberts(6934회), John Grisham(5283회), James Patterson(5020회)이다. 
""")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#데이터불러오기
df_topreadauthor = pd.read_csv('data/topreadauthor.csv')
fig1, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='count', y='author', data = df_topreadauthor, palette='Set2')

# x축 레이블 90도 회전
ax.set_xticklabels(ax.get_xticklabels(), rotation=50)

# 그래프 제목 추가
ax.set_title('Top10 Authors most read by users', fontsize=16)

# 그래프 표시하기
st.pyplot(fig1)


st.write('')
st.write('')
js = "window.scrollTo(0, document.getElementById('part-2-author-analysis').offsetTop);"

st.write('')
st.write('')



st.write("""
##### ✔ 유저들의 평균평점이 높았던  상위10 인기 작가 
- 유저들의 평균평점이 높았던 작가는 Clamp(6.18점), Shel Silverstein(6.08점), Nick Bantock Antoine de Saint-Exupéry (5.74점), Dr. Seuss(5.67) 순 이다. 
""")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#데이터불러오기
df_topratingauthor = pd.read_csv('data/topratingauthor.csv')
fig1, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='Book-Rating', y='Book-Author', data =df_topratingauthor, palette='pastel')

# x축 레이블 90도 회전
ax.set_xticklabels(ax.get_xticklabels(), rotation=50)

# 그래프 제목 추가
ax.set_title('Top10 Authors best rated by users', fontsize=16)

# 그래프 표시하기
st.pyplot(fig1)

st.write('')
st.write('')
js = "window.scrollTo(0, document.getElementById('part-2-author-analysis').offsetTop);"

st.write('')
st.write('')


js = "window.scrollTo(0, document.getElementById('part-3-year_publication-analysis').offsetTop);"

st.markdown("<h3 id='part-3-year_publication-analysis'>✅Part 3. 출판년도 분석</h3>", unsafe_allow_html=True)


st.write("""
##### ✔ 유저들이 가장 많이 찾은 상위10 인기 작가 
- 이상치 확인,-1 값 또는 1950년보다 작거나 2010년보다 큰 값을 가지는 셀에 대해, 해당 셀을 NaN으로 변환 후,해당 결측치를 평균값으로 대체
- 최근으로 갈 수 록 출판이 많은 것으로 보여짐. 
""")


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#데이터불러오기
df_year = pd.read_csv('data/YearPublication (1).csv')

# 각 연도별 빈도수 구하기
year_counts = df_year['Year-Of-Publication'].value_counts()

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.bar(year_counts.index, year_counts.values)
plt.title("Year-Of-Publication counts")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()










