import streamlit as st
import pandas as pd
import os

#文本展示
st.title("小马")
st.header("哈基米 叮咚鸡")
st.subheader("哈基米~ 哈基米~ 曼波~")
st.text("哈基米莫南北绿豆阿西哈呀库~")
st.markdown("哈哈哈哈哈哈")
st.latex(r"数学公式: E=mc^2")

#数据展示
data = pd.DataFrame({
    "姓名": ["张三", "李四"],
    "年龄": [25, 30]
})
st.dataframe(data)        # 交互式表格
st.table(data)            # 静态表格
st.json({"key": "value"}) # JSON 数据

#媒体展示
# st.image("photos/哈基米.jpg", caption="哈基米")  # 显示图片
if st.button("点击播放"):
    st.audio("music/BACK SEAT.mp3")           # 播放音频
st.audio("music/Baby, Don't Cry.mp3")           # 播放音频
st.audio("music/Goodbye.mp3")           # 播放音频
# st.video("video/piano.mp4")             #播放视频

#交互组件
if st.button("点击我"):
    st.write("按钮被点击了")

# 复选框
if st.checkbox("显示数据"):
    st.dataframe(data)

# 单选框
option = st.radio("选择一个选项", ["A", "B", "C"])
st.write("你选择了:", option)

# 下拉选择
option = st.selectbox("选择一个选项", ["A", "B", "C"])

# 文本输入
name = st.text_input("请输入姓名")

# 滑块
age = st.slider("选择年龄", 0, 100, 25)


#布局管理
# 侧边栏
with st.sidebar:
    st.header("侧边栏")
    option = st.selectbox("侧边栏选择", ["1", "2"])

# 两列布局
col1, col2 = st.columns(2)
with col1:
    st.write("第一列")
with col2:
    st.write("第二列")

# .expander 折叠面板
with st.expander("点击展开"):
    st.write("隐藏的内容")


#缓存机制
@st.cache_data  # 缓存数据
def load_data():
    # 模拟耗时操作（实际场景可能是读取大文件、数据库查询等）
    import time
    time.sleep(2) # 暂停2秒，模拟耗时
    # 返回一个简单的DataFrame
    return pd.DataFrame({"数据": [1, 2, 3]})

data1 = load_data()
st.dataframe(data1)


#状态管理
# 初始化状态
if "count" not in st.session_state:
    st.session_state.count = 0

# 按钮点击增加计数
if st.button("增加"):
    st.session_state.count += 1

st.write("计数:", st.session_state.count)




