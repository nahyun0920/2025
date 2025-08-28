import streamlit as st
import random

st.set_page_config(page_title="🔥성격별 스포츠 추천🔥", page_icon="⚡", layout="wide")

st.markdown(
    """
    <h1 style='text-align: center; color: #ff5733; font-size:60px;'>✨ 성격 유형별 스포츠 추천 ✨</h1>
    <p style='text-align: center; font-size:22px;'>당신의 성격에 맞는 운동 종목을 찾아보세요! ⚡🏆</p>
    """,
    unsafe_allow_html=True
)

# 성격 유형별 스포츠 추천 데이터
sports_recommendations = {
    "모험을 좋아하는 유형 🌋": [
        "🥋 주짓수", "🥊 복싱", "🥷 태권도", "⛷ 스키", "🏂 스노우보드", "🏄‍♂️ 서핑", "🧗 암벽등반", "🚵 MTB", "🏇 승마"
    ],
    "협동을 중시하는 유형 🤝": [
        "⚽ 축구", "🏀 농구", "🏐 배구", "🏒 아이스하키", "🥅 핸드볼", "🏉 럭비", "🥎 소프트볼"
    ],
    "인내심 강한 유형 🧘": [
        "🏊 수영", "🚴 사이클", "🏃 마라톤", "⛷ 크로스컨트리", "🚣 조정", "🏌️ 골프"
    ],
    "집중력이 뛰어난 유형 🎯": [
        "🏹 양궁", "🤺 펜싱", "🎱 당구", "♟ 체스(두뇌 스포츠)", "🎳 볼링", "🕹 e스포츠"
    ],
    "도전을 즐기는 유형 🔥": [
        "🤼 레슬링", "🥋 유도", "🥊 킥복싱", "🤸 체조", "🏇 승마 점프", "🛹 스케이트보드"
    ],
    "창의적인 유형 🎨": [
        "⛸ 피겨스케이팅", "🤸 리듬체조", "🎤 댄스스포츠", "🎭 치어리딩"
    ],
    "차분한 유형 🌙": [
        "🏹 양궁", "🎾 테니스", "🏓 탁구", "🏸 배드민턴", "⛳ 골프", "🥋 합기도"
    ],
    "리더십이 강한 유형 👑": [
        "⚽ 축구 주장", "🏀 농구 주장", "🏉 럭비", "🏐 배구", "🥅 아이스하키 주장"
    ]
}

# 성격 유형 선택
st.markdown("## 👉 당신의 성격 유형을 선택하세요 😎")
selected_type = st.selectbox("성격유형 선택 🎭", list(sports_recommendations.keys()))

st.markdown(f"### ✨ {selected_type} 에게 어울리는 스포츠는... 🎉")

# 카드 형식으로 추천 종목 표시
cols = st.columns(3)
sports = sports_recommendations[selected_type]

for i, sport in enumerate(sports):
    with cols[i % 3]:
        st.markdown(
            f"""
            <div style="background-color:#ffe6e6; border-radius:20px; padding:20px; margin:10px; text-align:center; 
            box-shadow: 0px 4px 8px rgba(0,0,0,0.2); font-size:25px;">
            {sport}
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("---")
st.markdown(
    "<h3 style='text-align:center; color:#0077b6;'>💪 오늘부터 새로운 스포츠에 도전해보세요! 🏆🔥</h3>",
    unsafe_allow_html=True
)



