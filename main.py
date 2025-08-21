import streamlit as st

# 🎯 MBTI별 추천 직업 데이터
career_dict = {
    "INTJ": ["🧪 과학자", "🧠 전략 기획가", "⚙️ 엔지니어"],
    "INTP": ["🔬 연구원", "💻 프로그래머", "💡 발명가"],
    "ENTJ": ["👔 CEO", "⚖️ 변호사", "🏛️ 정치인"],
    "ENTP": ["🚀 창업가", "📢 마케터", "🧭 컨설턴트"],
    "INFJ": ["🤝 상담가", "📚 교사", "✍️ 작가"],
    "INFP": ["🧘 심리학자", "🎨 예술가", "🎼 작사가"],
    "ENFJ": ["👑 리더", "🎓 교수", "🌍 외교관"],
    "ENFP": ["🎭 배우", "📰 기자", "📣 홍보 전문가"],
    "ISTJ": ["⚖️ 판사", "📊 회계사", "👮 경찰"],
    "ISFJ": ["💉 간호사", "🍎 교사", "🤲 사회복지사"],
    "ESTJ": ["🪖 군인", "📈 경영자", "🏢 공무원"],
    "ESFJ": ["💬 상담사", "🏥 간호사", "🎉 이벤트 기획자"],
    "ISTP": ["🔧 기술자", "✈️ 파일럿", "🏋️ 스포츠 코치"],
    "ISFP": ["🎨 디자이너", "📸 사진작가", "🎶 음악가"],
    "ESTP": ["💼 기업가", "⚽ 운동선수", "🤝 세일즈 전문가"],
    "ESFP": ["🎤 배우", "📺 MC", "🌟 예능인"]
}

# 🌟 페이지 꾸미기
st.set_page_config(page_title="MBTI 진로 추천", page_icon="✨", layout="centered")

st.markdown(
    """
    <h1 style='text-align: center; color: #FF6F61;'>
        🌈 MBTI 기반 진로 추천 사이트 ✨
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown("#### 당신의 MBTI를 선택하면 🧭 어울리는 직업을 추천해드려요! 🎓")

# 🌀 사용자 MBTI 선택
mbti = st.selectbox("👉 MBTI를 선택하세요", list(career_dict.keys()))

if st.button("💡 나의 직업 추천 받기! 🚀"):
    st.success(f"✨ 당신의 MBTI는 **{mbti}** 🌟")
    st.markdown("#### 어울리는 직업 리스트 🎯")
    for job in career_dict[mbti]:
        st.markdown(f"- {job}")
    st.balloons()  # 🎈 효과
    st.snow()      # ❄️ 효과

