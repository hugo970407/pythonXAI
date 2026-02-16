import streamlit as st
number = st.number_input("請輸入數字", step=1) 
# step=1 表示單位以及增減的數字, min_value 表示最小值, max_value 表示最大值
st.write(f"你輸入的數字是：{number}")

st.markdown("### 練習")

# 練習題
number = st.number_input("請輸入數字", step=1) 
st.write(f"你輸入的數字是：{number}")


st.markdown("### 練習")
if st.button("按我！"):
    st.balloons()