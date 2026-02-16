import streamlit as st
import os
folderPath = "markdown"
files = os.listdir(folderPath)
files_name = []
for f in files:
    if f.endswith(".md"):
        files_name.append(f)
print(files_name)

for f in files_name:
    with open(f"{folderPath}/{f}", "r", encoding="utf-8") as file:
        content = file.read()
    with st.expander(f[:-3]):
        st.markdown(content)


# with st.expander("class1 課堂筆記"):
#     st.markdown(
#     """
#     # Class1 課堂筆記
#     ## 你好，這裡是 H1
#     ### 這裡是 H2
#     #### 這裡是 H3
#     ##### 這裡是 H4

#     # 這裡是程式區塊
#     ```python
#     print("Hello World") # 可以顯示文字
#     ```
#     """
#     )

# # with st.expander("class1 課堂筆記"):
#     st.markdown(
#     """
 

# ---

# # 📘 Python 基礎語法筆記整理

# ## 一、`len()` 長度函數

# ### 🔹 功能

# `len()` 用來計算「長度」。

# 可以算：

# * 字串有幾個字
# * 串列有幾個元素
# * 其他可計數的資料

# ---

# ### 🔹 範例

# ```python
# len('')
# ```

# 👉 空字串，長度是 **0**

# ```python
# len('a')
# ```

# 👉 長度是 **1**

# ```python
# len('bb')
# ```

# 👉 長度是 **2**

# ```python
# len("ccc")
# ```

# 👉 長度是 **3**

# ```python
# len("dddd")
# ```

# 👉 長度是 **4**

# ---

# ### ✅ 重點觀念

# * 每一個字元都算 1 個長度
# * 單引號 `' '` 和 雙引號 `" "` 都可以表示字串

# ---

# # 二、`float()` 轉換成小數

# ### 🔹 功能

# `float()` 可以把資料轉換成「浮點數（小數）」。

# ---

# ### 🔹 範例

# ```python
# float(True)
# ```

# 👉 `True` 會變成 **1.0**

# ```python
# float(123)
# ```

# 👉 變成 **123.0**

# ```python
# float("hello")
# ```

# ❌ 會發生錯誤！

# 因為 `"hello"` 不是數字，無法轉成小數。

# ---

# ### ✅ 重點觀念

# | 原本資料     | 轉換結果 |
# | -------- | ---- |
# | True     | 1.0  |
# | False    | 0.0  |
# | 整數       | 變成小數 |
# | 文字(不是數字) | ❌ 錯誤 |

# ---

# # 三、`for` 迴圈與 `range()`

# `for` 迴圈可以重複執行程式。

# ---

# ## 🔹 基本寫法

# ```python
# for 變數 in range(開始, 結束):
#     要執行的程式
# ```

# 👉 **注意：結束數字不會被包含！**

# ---

# ## 範例一

# ```python
# for i in range(2, 6):
#     print(i)
# ```

# 輸出結果：

# ```
# 2
# 3
# 4
# 5
# ```

# 👉 6 不會被印出來！

# ---

# ## 範例二（設定間隔）

# ```python
# for i in range(2, 10, 2):
#     print(i)
# ```

# 輸出結果：

# ```
# 2
# 4
# 6
# 8
# ```

# ---

# ### 🔹 `range(開始, 結束, 間隔)`

# | 位置   | 意思       |
# | ---- | -------- |
# | 第1個數 | 起始值      |
# | 第2個數 | 結束值（不包含） |
# | 第3個數 | 每次增加多少   |

# ---

# # 🎯 本頁重點整理

# ### 1️⃣ `len()`

# * 計算長度
# * 空字串長度是 0

# ### 2️⃣ `float()`

# * 把資料轉成小數
# * 不能把非數字字串轉成 float

# ### 3️⃣ `for + range()`

# * 用來重複執行
# * 結束數字「不包含」
# * 可以設定間隔

# ---

#     """
#     )