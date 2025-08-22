import streamlit as st

st.set_page_config(page_title="스포츠 추천기", page_icon="🏃", layout="centered")

st.title("🔥 나에게 딱 맞는 스포츠 찾기 🔥")
st.write("성격유형과 운동 목적을 선택하면 어울리는 스포츠를 추천해드립니다!")

# -----------------------
# 입력 파트
# -----------------------
personality = st.radio(
    "👉 당신의 성격유형을 골라주세요:",
    ["활발하고 사교적인 성격",
     "차분하고 인내심 강한 성격",
     "도전적이고 승부욕 강한 성격",
     "창의적이고 자유로운 성격",
     "집중 잘하고 혼자 하는 걸 좋아하는 성격"]
)

purpose = st.selectbox(
    "👉 운동 목적을 선택하세요:",
    ["건강", "다이어트", "경쟁", "재미", "사회성"]
)

fitness = st.slider("👉 본인의 체력 수준은?", 1, 10, 5)

# -----------------------
# 추천 로직
# -----------------------
recommendations = []

if personality == "활발하고 사교적인 성격":
    recommendations = ["⚽ 축구 - 친구들과 함께 즐기며 협동심 강화!",
                       "🏀 농구 - 빠른 템포와 팀워크에 잘 어울려요!"]

elif personality == "차분하고 인내심 강한 성격":
    recommendations = ["🏊 수영 - 꾸준히 하면 성취감 최고!",
                       "🏃 마라톤 - 집중력과 인내심을 살릴 수 있어요!"]

elif personality == "도전적이고 승부욕 강한 성격":
    recommendations = ["🥋 태권도 - 강한 정신력과 승부욕에 어울려요!",
                       "🤼 유도 - 전략과 힘을 동시에 발휘할 수 있어요!"]

elif personality == "창의적이고 자유로운 성격":
    recommendations = ["💃 댄스 - 자유롭게 표현하며 스트레스 해소!",
                       "🛹 스케이트보드 - 창의적인 동작으로 개성 발휘!"]

elif personality == "집중 잘하고 혼자 하는 걸 좋아하는 성격":
    recommendations = ["🏹 양궁 - 집중력 발휘에 최고!",
                       "⛳ 골프 - 혼자만의 플레이에 잘 맞아요!"]

# -----------------------
# 결과 출력
# -----------------------
st.subheader("🎉 추천 결과 🎉")
for rec in recommendations:
    st.write(rec)

st.info(f"당신의 운동 목적은 **{purpose}**, 체력 수준은 **{fitness}/10** 입니다!")

