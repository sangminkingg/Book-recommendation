
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt
import plotly.express as px


st.header('👨‍📝고객분석')


st.sidebar.markdown("""
    ## 고객 분석
    - [part 1. 나이별 분석](#part-1-age-analysis)
    - [part 2. 지역별 분석](#part-2-location-analysis)
    - [part 3. 유저별 분석](#part-3-user-analysis)
""")
st.write('')
st.write("""
- 도서평점을 부여한 고객들의 특성 및 취향에 대한 분석으로 도서 평점 데이터를 활용하여 고객들의 취향이나 평점 패턴 등을 분석하고 성별, 연령, 지역등 고객의 특성에 따른 평점 차이를 파악할 수 있다. 이를 통해 어떤 책이 어떤 특성을 가진 고객들이 어떤 책을 선호하는지를 파악할 수 있다. 
""")
st.write('')
st.write('')
st.write("""
### Dataset
""")
df_train = pd.read_csv('data/Country.csv')
st.dataframe(df_train)

st.write('')
st.write('')

js = "window.scrollTo(0, document.getElementById('part-1-age-analysis').offsetTop);"

    
st.markdown("<h3 id='part-1-age-analysis'>✅Part 1. 나이별 분석</h3>", unsafe_allow_html=True)

st.write("""
#### DATA 전처리

- 상위 1%인 0-15세를 모두 15세로 대체하며, 하위1%에 해당하는 67세-244세는 모두 67세로 대체

""")


st.write("""
##### ✔ 연령별 히스토그램
- 35세의 유저들이 가장 많았으며, 유저들의 평균나이는 약 36.7세 이다.
- 위 데이터를 통해 대상 독자층을 파악하여 적합한 캠페인이나 이벤트를 기획할 수도 있다. 
- 가장 많은 30대 독자들을 위한 추천도서를 선정하거나 해당 독자들과 비슷한 나이대의 작가의 작품을 소개하는 이벤트를 진행 할 수 있다.
-도서 큐레이션이 필요 할 시, 대상 독자층의 특성을 고려하여 결정 할 수 있다.
""")


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
df = pd.read_csv('data/Country.csv')

# 히스토그램 그리기
fig4 = plt.figure()
plt.hist(data=df, x='Age', bins=30, rwidth=0.8)
plt.title('Age Distribution') # 그래프 제목 설정
plt.xlabel('Age') # x축 레이블 설정
plt.ylabel('Count') # y축 레이블 설정

# 그래프 표시하기
st.pyplot(fig4)

st.write('')
st.write('')
st.write('')

js = "window.scrollTo(0, document.getElementById('part-2-location-analysis').offsetTop);"
  
st.markdown("<h3 id='part-2-location-analysis'>✅Part 2. 지역별 분석</h3>", unsafe_allow_html=True)

st.write("""
#### DATA 전처리

- Location(city, state, country) 로 구성.
- 해당 데이터는 사용자가 자유롭게 지역을 기입하는 방식으로 구성되어 있어 아래와 같이 국가정보 파악이 힘든 데이터가 있음을 발견(이상값과 결측값 수정 및 제거)
- 국가 정보만 있는 새로운 열 생성(국가명(Country)을 ISO-3166-1 alpha-3 국가 코드로 변환)
- 주 정보만 있는 새로운 열 생성
""")

st.write("""
   
     
""")

st.write("""
##### ✔ 상위 10개 나라별 평점 수
도서 이용량이 많은 나라는 미국이 압도적으로 가장 많으며 캐나다, 영국, 독일, 호주 등으로 분포되어있다.
- USA = 미국
- CAN = 캐나다
- GBR = 영국
- DEU = 독일
- AUS = 호주
- ESP = 스페인
- FRA = 프랑스
- PRT = 포르투갈
- NZL = 뉴질랜드
- MYS = 말레이시아
""")

st.write('')
st.write('')

st.write("""
- 지역별 특성을 고려하여 마케팅 전략을 수립 할 수 있다. 
- 만약 해당 결과가 온라인 서점 이용객들의 데이터라고 할 때, 미국, 캐나다, 영국, 독일, 호주 등에서는 도서 이용이 많은 것으로 파악되므로 해당 지역의 마케팅을 더욱 강화 한다면 세일즈를 증가시킬 수 있을 것이다. 
- 포르투갈과 뉴질랜드는 상대적으로 도서 이용이 적은 편이므로 도서 이용을 증가시킬 수 있는 홍보나 할인 이벤트를 마련할 수 있다.
""")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기

df_location = pd.read_csv('data/rating_count.csv')

fig3, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='index', y='Country', data=df_location, ax=ax)
ax.set_title('Number of ratings by country') # 그래프 제목 설정

# 그래프 표시하기
st.pyplot(fig3)


st.write("""
##### ✔ 상위 10개 나라별 평균 평점 수 
나라별 도서평균평점을 가장 높게 준 나라는 순서대로 우간다이며 가봉 리투아니아 과테말라가 뒤를 잇는다.
- UGA = 우간다
- GAB = 가봉
- LTU = 리투아니아
- GTM = 과테말라
- MUS = 모리셔스공화국
- VNM = 베트남
- BGD = 방글라데스
- GNB = 기니비사우
- AND = 안다우스
- BRN = 브루나이
""")

st.write('')
st.write('')

st.write("""
- 각 나라의 독서 문화와 평가하는 기준, 독서 인프라 등을 비교 분석할 수 있다.
- 예를 들어,  해당데이터에서 우간다와 가봉은 도서평균 평점이 높지만, 독서 인프라나 독서 이용률은 낮은것으로 판단된다. 따라서 독서환경 개선을 위하여 책 이용률을 높이기 위한 캠페인을 진행할 수 있다. 
- 각 나라의 독서 선호도를 고려하여 도서를 추천 할 수 있다. 
""")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기

df_avg = pd.read_csv('data/avg_country.csv')

fig2, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='Country', y='Rating-Per-Count', data=df_avg, ax=ax)
ax.set_title('Average rating by country') # 그래프 제목 설정

# 그래프 표시하기
st.pyplot(fig2)
st.write('')
st.write('')
st.write('')

js = "window.scrollTo(0, document.getElementById('part-3-user-analysis').offsetTop);"

st.markdown("<h3 id='part-3-user-analysi'>✅Part 3. 유저별 분석</h3>", unsafe_allow_html=True)
st.write('')
st.write('')

st.write("""
##### ✔ 상위 10위 유저별 최대 평점 수 
- USER_56601이 11143번의 평점 수를 기록했다.
- 그 뒤로 USER_54865, 52453, 73501 등이 높은 순위를 기록했다.
- 해당 데이터 결과를 통해 많은 평점을 남기는 유저를 탐지하고, 이들이 선호하는 책이나 작가를 추적하여 추천 시스템에 활용할 수 있다. 
- 이용자들에게 맞춤형 추천을 제공하고, 도서관 또는 서점의 고객 충성도를 높일 수 있을 것이다. 
- 해당 유저들을 대상으로 이벤트나 캠페인을 진행하여 이용자들의 활동을 촉진 할 수 있다.
""")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기

df_user = pd.read_csv('data/users.csv')

fig1, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='N_ratings', y='User-ID', data=df_user,palette='Set1')

# x축 레이블 90도 회전
ax.set_xticklabels(ax.get_xticklabels(), rotation=50)

# 그래프 제목 추가
ax.set_title('Maximum number of ratings for top 10 users', fontsize=16)

# 그래프 표시하기
st.pyplot(fig1)
