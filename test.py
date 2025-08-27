import streamlit as st

st.set_page_config(page_title="성격 유형별 스포츠 추천", page_icon="🏅", layout="centered")

st.title("🏅 성격 유형 기반 스포츠 추천 사이트")
st.write("당신의 성격과 체력 수준에 맞는 스포츠를 추천해드립니다!")

# ---------------- 입력 파트 ----------------
# 성격 유형 선택
personality = st.selectbox(
    "당신의 성격 유형을 골라주세요:",
    ["활발하고 사교적인 성격", "차분하고 인내심 강한 성격", "도전적이고 승부욕 강한 성격", 
     "창의적이고 자유로운 성격", "집중 잘하고 혼자 하는 성격"]
)

# 운동 목적 선택
goal = st.radio(
    "운동 목적은 무엇인가요?",
    ["건강 유지", "다이어트", "경쟁에서 이기기", "재미", "사회성 향상"]
)

# 체력 수준 슬라이더
fitness = st.slider("당신의 체력 수준을 선택하세요:", 1, 5, 3)

# ---------------- 추천 로직 ----------------
recommendations = []

if personality == "활발하고 사교적인 성격":
    if fitness <= 2:
        recommendations = ["⚽ 풋살", "🏓 탁구"]
    elif fitness <= 4:
        recommendations = ["⚽ 축구", "🏀 농구"]
    else:
        recommendations = ["🏉 럭비", "🏀 농구"]

elif personality == "차분하고 인내심 강한 성격":
    if fitness <= 2:
        recommendations = ["🧘 요가", "🚶‍♂️ 가벼운 조깅"]
    elif fitness <= 4:
        recommendations = ["🏊 수영", "🚴 자전거"]
    else:
        recommendations = ["🥋 주짓수", "🏃 마라톤"]

elif personality == "도전적이고 승부욕 강한 성격":
    if fitness <= 2:
        recommendations = ["🏓 탁구", "🎯 다트"]
    elif fitness <= 4:
        recommendations = ["🥋 주짓수", "🤼 유도"]
    else:
        recommendations = ["🥋 주짓수", "🥊 복싱", "🥋 태권도"]

elif personality == "창의적이고 자유로운 성격":
    if fitness <= 2:
        recommendations = ["🩰 발레", "🧘 요가"]
    elif fitness <= 4:
        recommendations = ["💃 댄스", "🛹 스케이트보드"]
    else:
        recommendations = ["🤸‍♂️ 체조", "🏄 서핑"]

elif personality == "집중 잘하고 혼자 하는 성격":
    if fitness <= 2:
        recommendations = ["🎳 볼링", "🎯 양궁"]
    elif fitness <= 4:
        recommendations = ["🏌️ 골프", "🏹 양궁"]
    else:
        recommendations = ["🏊 철인 3종 경기", "🚵 산악 자전거"]

# ---------------- 출력 파트 ----------------
st.subheader("🎉 추천 결과 🎉")
if recommendations:
    for sport in recommendations:
        st.write(f"- {sport}")
else:
    st.write("조건에 맞는 운동을 찾지 못했어요 😢")

st.success("운동은 꾸준함이 가장 중요해요! 파이팅! 💪")
