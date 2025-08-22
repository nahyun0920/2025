import streamlit as st
import random

st.set_page_config(page_title="스포츠 추천기", page_icon="🏃", layout="centered")

st.title("🔥 나에게 딱 맞는 스포츠 찾기 🔥")
st.write("성격유형과 체력 수준을 선택하면 어울리는 스포츠를 추천해드립니다!")

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

fitness = st.slider("👉 본인의 체력 수준은?", 1, 10, 5)

# -----------------------
# 추천 로직
# -----------------------
recommendations = []
show_jiujitsu = False   # 주짓수 추천 여부 체크

if personality == "활발하고 사교적인 성격":
    if fitness <= 4:
        recommendations = ["🏓 탁구 - 가볍게 즐기기 좋아요!", "🚶 가벼운 걷기 - 친구랑 수다 떨며 딱!"]
    elif fitness <= 7:
        recommendations = ["🏀 농구 - 빠른 템포와 팀워크에 어울려요!", "🏸 배드민턴 - 가볍게도, 치열하게도 가능!"]
    else:
        recommendations = ["⚽ 축구 - 에너지 넘치는 당신에게 완벽!", "🏐 배구 - 활발함과 체력이 딱 맞아요!"]

elif personality == "차분하고 인내심 강한 성격":
    if fitness <= 4:
        recommendations = ["🧘 요가 - 호흡과 집중에 좋아요", "🚶‍♂️ 산책 - 꾸준함이 무기!"]
    elif fitness <= 7:
        recommendations = ["🏊 수영 - 차분하게 체력 기르기 최고!", "🚴 자전거 - 중간 난이도 지구력 운동"]
    else:
        recommendations = ["🏃 마라톤 - 인내심과 체력을 동시에!", "⛰️ 등산 - 자연 속에서 꾸준한 도전"]

elif personality == "도전적이고 승부욕 강한 성격":
    if fitness <= 4:
        recommendations = ["🏓 탁구 - 가볍게 시작하면서 승부욕 발휘!", "🥊 라이트 복싱 - 재미 위주로"]
    elif fitness <= 7:
        recommendations = ["🥋 태권도 - 승부욕을 발휘하기 좋은 운동!", "🤼 유도 - 기술과 힘을 동시에!"]
    else:
        recommendations = ["🥋 주짓수 - 전략과 힘, 인내심을 모두 발휘!", "🏋️ 크로스핏 - 강한 정신력과 체력 발휘!"]
        show_jiujitsu = True

elif personality == "창의적이고 자유로운 성격":
    if fitness <= 4:
        recommendations = ["🧘 필라테스 - 유연성과 창의성 발휘!", "💃 가벼운 댄스 - 즐겁게 몸 풀기"]
    elif fitness <= 7:
        recommendations = ["🛹 스케이트보드 - 자유롭게 기술 도전!", "🤸‍♀️ 리듬체조 - 표현력 살리기"]
    else:
        recommendations = ["🎭 댄스 배틀 - 창의력 폭발!", "⛷️ 스노보드 - 고난도 기술에 도전!"]

elif personality == "집중 잘하고 혼자 하는 걸 좋아하는 성격":
    if fitness <= 4:
        recommendations = ["🎯 다트 - 집중력과 손 눈 협응!", "♟️ 체스+체력운동 (간단한 조깅 병행)"]
    elif fitness <= 7:
        recommendations = ["🏹 양궁 - 집중력 발휘에 최고!", "🏓 탁구(개인연습) - 혼자도 가능!"]
    else:
        recommendations = ["🥋 주짓수 - 집중력+기술+체력 완벽 조합!", "⛳ 골프 - 집중과 체력 모두 활용!"]
        show_jiujitsu = True

# -----------------------
# 결과 출력
# -----------------------
st.subheader("🎉 추천 결과 🎉")
for rec in recommendations:
    st.write(rec)

# 주짓수 추천되면 기술 GIF 보여주기
if show_jiujitsu:
    st.markdown("### 🥋 주짓수 기술 예시")

    jiujitsu_gifs = [
        ("https://jiujitsulegacy.com/wp-content/uploads/2021/02/armbar.gif", "암바 (Armbar)"),
        ("https://media.tenor.com/5UfrpsbR9P4AAAAC/bjj-sweep.gif", "스윕 (Sweep)"),
        ("https://media.tenor.com/oxIkvhk1HqQAAAAC/triangle-choke-bjj.gif", "삼각조르기 (Triangle Choke)"),
    ]

    gif_url, caption = random.choice(jiujitsu_gifs)
    st.image(gif_url, caption=caption, use_column_width=True)

st.info(f"체력 수준: **{fitness}/10** 에 맞춘 추천입니다!")

