import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from surprise import Reader, Dataset, KNNBasic
import streamlit as st
import matplotlib as plt
import plotly.express as px


st.header('📖도서추천알고리즘')


st.sidebar.markdown("""
    ## 도서 중심 분석
    - [part 1. 협업 필터링 기반의 추천 시스템](#part-1-book)
    - [part 2. 콘텐츠 기반 필터링 기반의 추천 시스템](#part-2-book)
    - [part 3. 행렬 인수분해  기반의 추천 시스템](#part-3-book)
    - [part 4. 딥 러닝 모델 기반의 추천 시스템](#part-4-book)
    - [part 5. 앙상블 기법을 사용한 추천 시스템](#part-5-book)
    - [part 6. 하이퍼마라미터 최적화를 통한 추천 시스템](#part-6-book)
""")
st.write('')
st.write("""
- 출판사나 도서 기업의 입장에서 도서 평점을 활용한 분석이다. 출판사/도서기업이 가지고 있는 고객 데이터와 평점 등을 통해 출판사/도서기업의 데이터가 고객의 평점에 어떠한 영향을 미치는지를 분석하여 고객의 선호도를 분석한다.
""")
st.write(""" 
## Model Test 결과
- 가장 높은 점수를 받은 모델은 RMSE 점수 3.3974점인 SVD 와 아이템기반협업필터링 모델이다.
""")
st.write('')
st.write('')
st.write(""" 
### Dataset
""")

df_train = pd.read_csv('data/TRAIN.csv')
st.dataframe(df_train)
st.write('')
st.write('-> Dataset Book-Title을 추천시스템에 직접 입력해보세요')
 
    
st.markdown("<h3 id='part-1-book'>✅Part 1. 협업 필터링 기반의 추천 시스템</h3>", unsafe_allow_html=True)
st.write('결과물: 사용자 기반 협업 필터링 및 아이템 기반 협업 필터링 모델을 구현하고, 이들 모델의 평점 예측 성능을 평가한다. RMSE 값으로 성능을 비교하여 어떤 협업 필터링 방법이 더 나은 성능을 보이는지 결정한다.')
st.write('')
st.write("""
✔ 사용자기반 협업필터링
- 사용자 기반 협업 필터링(User-based Collaborative Filtering)은 도서 추천 시스템에서 가장 기본적인 방법 중 하나이다. 이 방법은 사용자 간의 유사도를 계산하고, 비슷한 취향을 가진 사용자들이 선호한 도서를 추천해주는 방식이다.
""")
st.write('')
st.write("""
✔ 아이템기반 협업필터링
- 아이템 기반 협업 필터링(Item-based Collaborative Filtering)은 사용자가 아닌 아이템을 중심으로 유사도를 계산하여 추천하는 방식. 사용자가 평가한 아이템들의 유사도를 계산하여 추천하고자 하는 아이템과 가장 유사한 아이템들을 찾아서 추천한다.
""")
st.write('✔ 아이템기반 협업필터링')

# 데이터 불러오기
train = pd.read_csv('data/TRAIN.csv')

# 평점이 4점 이상인 데이터만 사용
train = train[train['Book-Rating'] >= 4]

# 사용자-아이템 행렬 생성
pivot_data = train.pivot_table(index='User-ID', columns='Book-Title', values='Book-Rating', fill_value=0)

# 코사인 유사도 계산
cos_sim = cosine_similarity(pivot_data.T)

# 아이템 기반 협업 필터링 (KNNBasic) 모델 구축
reader = Reader(rating_scale=(1, 10))
data = Dataset.load_from_df(train[['User-ID', 'Book-Title', 'Book-Rating']], reader)
trainset = data.build_full_trainset()
sim_options = {'name': 'cosine', 'user_based': False}
item_based_cf = KNNBasic(sim_options=sim_options)
item_based_cf.fit(trainset)

# 사용자가 선택한 책과 유사한 책 5개 추천
def recommend_books(book_title):
    book_rating = pivot_data[book_title]
    similar_books_index = np.unique(np.argsort(cos_sim[pivot_data.columns.get_loc(book_title)])[-6:-1])
    similar_books = list(pivot_data.columns[similar_books_index])
    recommended_books = []
    for book in similar_books:
        _, _, _, est, _ = item_based_cf.predict(uid=book_title, iid=book)
        if est >= 4.0:
            recommended_books.append(book)
    return recommended_books

# Streamlit 앱 구성
st.title('Book Recommender')
book_title = st.text_input('Enter a book title', key='book_input')
if book_title in pivot_data.columns:
    recommended_books = recommend_books(book_title)
    if len(recommended_books) > 0:
        st.write('Recommended books:')
        for book in recommended_books:
            st.write('- ' + book)
    else:
        st.write('No recommended books')
else:
    st.write('Enter a valid book title')
js = "window.scrollTo(0, document.getElementById('part-2-book').offsetTop);"
st.markdown("<h3 id='part-2-book'>✅Part 2. 콘텐츠 기반 필터링 기반의 추천 시스템</h3>", unsafe_allow_html=True)
st.write('결과물: 책의 속성(저자, 출판사, 장르 등)을 기반으로 한 콘텐츠 기반 필터링 모델을 구현하고, 모델의 평점 예측 성능을 평가한다. 협업 필터링 모델과 성능을 비교하여 콘텐츠 기반 필터링의 효과를 분석한다.')
st.write('')
js = "window.scrollTo(0, document.getElementById('part-3-book').offsetTop);"
st.markdown("<h3 id='part-3-book'>✅Part 3. 행렬 인수분해  기반의 추천 시스템</h3>", unsafe_allow_html=True)
st.write('결과물: SVD와 ALS와 같은 행렬 인수분해 기법을 사용하여 모델을 구현하고, 모델의 평점 예측 성능을 평가한다. 다른 추천 시스템과 성능을 비교하여 행렬 인수분해의 효과를 분석한다.')
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from surprise import Reader, Dataset
from surprise import SVD
import streamlit as st

# 데이터 불러오기
train = pd.read_csv('data/TRAIN.csv')

# 평점이 4점 이상인 데이터만 사용
train = train[train['Book-Rating'] >= 4]

# 사용자-아이템 행렬 생성
pivot_data = train.pivot_table(index='User-ID', columns='Book-Title', values='Book-Rating', fill_value=0)

# SVD 모델 구축
reader = Reader(rating_scale=(1, 10))
data = Dataset.load_from_df(train[['User-ID', 'Book-Title', 'Book-Rating']], reader)
trainset = data.build_full_trainset()
svd_model = SVD(n_factors=20, reg_all=0.02)
svd_model.fit(trainset)

# 사용자가 선택한 책과 유사한 책 5개 추천
def recommend_books(book_title):
    book_rating = pivot_data[book_title]
    similar_books_index = np.unique(np.argsort(cos_sim[pivot_data.columns.get_loc(book_title)])[-6:-1])
    similar_books = list(pivot_data.columns[similar_books_index])
    recommended_books = []
    for book in similar_books:
        _, _, _, est, _ = svd_model.predict(uid=book_title, iid=book)
        if est >= 4.0:
            recommended_books.append(book)
    return recommended_books

# Streamlit 앱 구성
st.title('Book Recommender')
book_title = st.text_input('Enter a book title', key='input')
if book_title in pivot_data.columns:
    recommended_books = recommend_books(book_title)
    if len(recommended_books) > 0:
        st.write('Recommended books:')
        for book in recommended_books:
            st.write('- ' + book)
    else:
        st.write('No recommended books')
else:
    st.write('Enter a valid book title')

st.write('')
js = "window.scrollTo(0, document.getElementById('part-4-book').offsetTop);"
st.markdown("<h3 id='part-4-book'>✅Part 4. 딥 러닝 모델 기반의 추천 시스템</h3>", unsafe_allow_html=True)
st.write('결과물: 딥 러닝 모델(신경망 기반 추천 모델 또는 잠재 요인 모델)을 구현하고, 모델의 평점 예측 성능을 평가한다. 다른 추천 시스템과 성능을 비교하여 딥 러닝 기반 추천 시스템의 효과를 분석한다.')
st.write('')
js = "window.scrollTo(0, document.getElementById('part-5-book').offsetTop);"
st.markdown("<h3 id='part-5-book'>✅Part 5. 앙상블 기법을 사용한 추천 시스템</h3>", unsafe_allow_html=True)
st.write('결과물: 여러 추천 시스템 모델을 결합하여 앙상블 모델을 구현한다. 가중 평균, 스태킹(Stacking) 등의 앙상블 기법을 적용하여 모델의 평점 예측 성능을 평가한다. 단일 모델과 성능을 비교하여 앙상블 기법의 효과를 분석한다.')
st.write('')
js = "window.scrollTo(0, document.getElementById('part-6-book').offsetTop);"
st.markdown("<h3 id='part-6-book'>✅Part 6. 하이퍼마라미터 최적화를 통한 추천 시스템</h3>", unsafe_allow_html=True)
st.write('결과물: 그리드 서치, 랜덤 서치, 베이지안 최적화 등의 기법을 사용하여 모델의 하이퍼파라미터를 최적화한다. 최적화된 하이퍼파라미터를 사용하여 모델의 성능을 평가하고, 기본 하이퍼파라미터를 사용한 모델과 성능을 비교하여 최적화 기법의 효과를 분석한다.')



