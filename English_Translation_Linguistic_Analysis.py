import streamlit as st
from google import genai
from google.genai import types
import re
from gtts import gTTS
import io
import json
import os

# 1. Khởi tạo Client kết nối API sử dụng Secrets của Streamlit
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

# Định nghĩa mô hình thế hệ mới chuẩn xác
MODEL_NAME = 'gemini-3.5-flash'

# Đường dẫn tệp lưu trữ lịch sử cục bộ trên ổ cứng
HISTORY_FILE = "history_db.json"

def load_persistent_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("history", []), data.get("extracted_en_clean", "")
        except Exception:
            return [], ""
    return [], ""

# (Các phần hàm xử lý giao diện và logic bổ sung của Boss giữ nguyên phía dưới)