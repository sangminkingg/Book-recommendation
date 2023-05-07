import streamlit as st

# 대시보드 URL
dashboard_url = "https://public.tableau.com/views/top30_16830926966980/1?:showVizHome=no&embed=true/language=ko-KR&:display_count=n&:origin=viz_share_link"

# Tableau Public 대시보드를 Streamlit 앱에 표시
st.markdown(f'<iframe src="{dashboard_url}" width="350%" height="2000" frameborder="0"></iframe>', unsafe_allow_html=True)
