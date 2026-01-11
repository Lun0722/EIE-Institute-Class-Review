import streamlit as st
from gtts import gTTS
import os

st.set_page_config(page_title="AI 課後複習 App", layout="centered")
st.title("📚 課後複習語音生成 App")

# 文字輸入
text = st.text_area("請輸入文章或單字", height=150)

if st.button("生成語音"):
    if not text.strip():
        st.warning("請先輸入文字")
    else:
        audio_file = "lesson_audio.mp3"
        tts = gTTS(text=text, lang="en")
        tts.save(audio_file)

        st.success("語音生成完成！🎉")
        st.audio(audio_file, format="audio/mp3")

# 清理檔案
if st.button("清理音檔"):
    if os.path.exists("lesson_audio.mp3"):
        os.remove("lesson_audio.mp3")
        st.success("音檔已清理 ✅")
    else:
        st.info("沒有音檔可以清理")
