# 練習題
import streamlit as st
st.title("成績評分系統")
number = st.number_input("請輸入數字", step=1, key="score") 
st.write(f"你輸入的數字是：{number}")
if number > 90:
    st.write("你的成績是A")
elif number > 80:
    st.write("你的成績是B")
elif number > 70:
    st.write("你的成績是C")
elif number > 60:
    st.write("你的成績是D")
else:
    st.write("你的成績是E")

st.title("數字金字塔")
number2 = st.number_input("請輸入數字", step=1, key="pyramid") 
st.write(f"你輸入的數字是：{number2}")
for i in range(1,number2+1):
     st.write(str(i)*i)


st.title("箭頭金字塔")
number3 = st.number_input("請輸入數字", step=1, key="3") 
for i in range()