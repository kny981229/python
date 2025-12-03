import streamlit as st
import pandas as pd
st.title(" 초간단 CSV 분석기")
#st.write("CSV 파일을 업로드하면 기본 통계를 자동으로 보여줍니다.")
# uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])
csv_path = "sample_data.csv"
# CSV 읽기
df = pd.read_csv(csv_path)
st.subheader("데이터 미리보기 (앞 5줄)")
st.write(df.head())
st.subheader(" 기본 정보")
st.write(f"행(Row) 수: {df.shape[0]}")
st.write(f"열(Column) 수: {df.shape[1]}")
st.write("컬럼 목록:", list(df.columns))
st.subheader(" 기술 통계 (describe)")
st.write(df.describe())
st.subheader(" 결측치(NaN) 개수")
st.write(df.isna().sum())