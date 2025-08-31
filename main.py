import streamlit as st
from few_shot import FewShotPosts
from post_generator import GeneratePost

length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

st.set_page_config(layout="wide")
def main():
    st.title("📣EchoPost – 🌐Let your ideas echo across LinkedIn.")

    col1, col2, col3 = st.columns(3)

    fs = FewShotPosts()
    with col1:
        selected_topic = st.selectbox("Topic For The Post", options=fs.get_tags())

    with col2:
        selected_length = st.selectbox("Length Of The Post", options=length_options)

    with col3:
        selected_language = st.selectbox("Language Of The Post", options=language_options)

    if st.button("Genereate My Post"):
        post = GeneratePost(selected_topic, selected_length, selected_language)
        st.write(post)

if __name__ == "__main__":
    main()