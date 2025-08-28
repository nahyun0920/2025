import streamlit as st

# ---------------- 페이지 기본 설정 ---------------- #
st.set_page_config(page_title="스포츠 추천 웹", page_icon="🏅", layout="wide")

st.title("🌟 나에게 맞는 스포츠 찾기 🎽")
st.markdown("### 성격유형 + 체력수준에 따라 딱 맞는 스포츠를 추천해드립니다! 💪🔥")

# ---------------- 데이터 정의 ---------------- #
sports_data = {
    "도전적인 유형 🏋️": {
        "초급": ["복싱 🥊", "클라이밍 🧗", "태권도 🥋", "주짓수 🤼"],
        "중급": ["철인 3종 경기 🏊🚴🏃", "레슬링 🤼", "킥복싱 🦵", "역도 🏋️"],
        "고급": ["MMA 🥊🤼", "크로스핏 💥", "유도 🥋", "스파르탄 레이스 🏃‍♂️🔥"]
    },
    "사교적인 유형 🤝": {
        "초급": ["농구 🏀", "배구 🏐", "축구 ⚽", "줄넘기 🤸"],
        "중급": ["족구 ⚽", "소프트볼 ⚾", "피구 🤾", "하키 🏒"],
        "고급": ["럭비 🏉", "아이스하키 🏒", "워터폴로 🤽", "라크로스 🥍"]
    },
    "차분한 유형 🌱": {
        "초급": ["요가 🧘", "필라테스 🧘‍♀️", "걷기 🚶", "하이킹 🥾"],
        "중급": ["수영 🏊", "사이클 🚴", "러닝 🏃", "스케이팅 ⛸️"],
        "고급": ["마라톤 🏃‍♂️", "트라이애슬론 🏊🚴🏃", "스키 ⛷️", "스노보드 🏂"]
    },
    "모험을 즐기는 유형 🌍": {
        "초급": ["서핑 🏄", "스케이트보드 🛹", "승마 🐎", "패들보드 🏄‍♀️"],
        "중급": ["스쿠버다이빙 🤿", "패러글라이딩 🪂", "카약 🚣", "산악자전거 🚵"],
        "고급": ["스카이다이빙 🪂🔥", "빙벽등반 🧗‍♂️❄️", "카누 🚣‍♂️", "카이트서핑 🪁🏄"]
    },
    "전략적인 유형 ♟️": {
        "초급": ["양궁 🏹", "탁구 🏓", "볼링 🎳", "펜싱 🤺"],
        "중급": ["테니스 🎾", "배드민턴 🏸", "골프 ⛳", "스쿼시 🥏"],
        "고급": ["체스 복싱 ♟️🥊", "에페 펜싱 🤺🔥", "세팍타크로 🏐", "폴로 🐎"]
    }
}

# ---------------- 사용자 입력 ---------------- #
st.sidebar.header("⚡ 나의 성향 선택하기")
personality = st.sidebar.selectbox("👉 성격 유형을 골라주세요", list(sports_data.keys()))

st.sidebar.header("🏃 체력 수준 선택하기")
fitness_level = st.sidebar.radio("👉 현재 나의 체력 수준은?", ["초급", "중급", "고급"])

# ---------------- 추천 결과 출력 ---------------- #
st.markdown("## 🎯 맞춤 스포츠 추천 결과")

if personality and fitness_level:
    recommendations = sports_data[personality][fitness_level]

    st.success(f"💡 **{personality}** + **{fitness_level} 체력 수준** 에 딱 맞는 종목은 다음과 같아요!")
    
    cols = st.columns(2)
    for i, sport in enumerate(recommendations):
        with cols[i % 2]:
            st.markdown(f"""
            <div style="background-color:#f0f8ff; padding:15px; border-radius:15px; 
                        text-align:center; font-size:20px; margin:10px;
                        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
                {sport}
            </div>
            """, unsafe_allow_html=True)

# ---------------- 추가 효과 ---------------- #
st.balloons()
st.markdown("✨ 운동으로 더 건강하고 멋진 자신을 만들어봐요! ✨")



