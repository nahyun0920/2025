import streamlit as st

st.set_page_config(page_title="성격 기반 스포츠 추천", page_icon="🏅", layout="centered")

st.title("🏅 성격 유형 & 체력 수준 기반 스포츠 추천 웹")
st.write("성격과 체력에 맞는 스포츠 종목을 추천해드릴게요!")

# 성격유형 선택
personality = st.radio(
    "당신의 성격 유형을 선택하세요:",
    ["활발하고 사교적인 성격", "차분하고 인내심 강한 성격", 
     "도전적이고 승부욕 강한 성격", "창의적이고 자유로운 성격", 
     "집중 잘하고 혼자 하는 걸 좋아하는 성격"]
)

# 운동 목적 선택
goal = st.selectbox(
    "운동 목적은 무엇인가요?",
    ["건강 유지", "다이어트", "경쟁/승부", "재미", "사회성 향상"]
)

# 체력 수준 슬라이더
fitness = st.slider("당신의 현재 체력 수준을 선택하세요:", 1, 5, 3)

st.markdown("---")

# 추천 로직
recommendations = []

if personality == "활발하고 사교적인 성격":
    if fitness <= 2:
        recommendations = ["🏓 배드민턴", "🏐 발리볼"]
    elif fitness <= 4:
        recommendations = ["⚽ 축구", "🏀 농구"]
    else:
        recommendations = ["🏉 럭비", "🤾 핸드볼"]

elif personality == "차분하고 인내심 강한 성격":
    if fitness <= 2:
        recommendations = ["🧘 요가", "🚶 가벼운 걷기"]
    elif fitness <= 4:
        recommendations = ["🏊 수영", "🚴 자전거"]
    else:
        recommendations = ["🏃 마라톤", "🏋️ 웨이트 트레이닝"]

elif personality == "도전적이고 승부욕 강한 성격":
    if fitness <= 2:
        recommendations = ["🤼 주짓수", "🥋 태권도"]
    elif fitness <= 4:
        recommendations = ["🥊 복싱", "🤺 펜싱"]
    else:
        recommendations = ["🏋️ 크로스핏", "🥇 철인 3종 경기"]

elif personality == "창의적이고 자유로운 성격":
    if fitness <= 2:
        recommendations = ["🕺 댄스", "🤸‍♀️ 필라테스"]
    elif fitness <= 4:
        recommendations = ["🛹 스케이트보드", "🎿 스키"]
    else:
        recommendations = ["🏄 서핑", "🚵 산악자전거"]

elif personality == "집중 잘하고 혼자 하는 걸 좋아하는 성격":
    if fitness <= 2:
        recommendations = ["🎯 다트", "🎳 볼링"]
    elif fitness <= 4:
        recommendations = ["🏹 양궁", "⛳ 골프"]
    else:
        recommendations = ["🏓 탁구", "🥌 컬링"]

# 결과 출력
st.subheader("🎉 추천 결과 🎉")
for sport in recommendations:
    st.write(sport)

# 이미지 예시 (로컬 or URL 가능)
# ✅ 인터넷 연결 안되면, 같은 폴더에 sport.jpg 저장해두고 불러오기
try:
    st.image("https://cdn.pixabay.com/photo/2017/04/06/22/13/sport-2200733_1280.png", use_container_width=True)
except:
    st.image("sport.jpg", use_container_width=True)

