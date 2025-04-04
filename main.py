import os
import sys
import datetime
import arrow
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from kurly import clusters

# 🎯 한국 공휴일 목록 (YYYY-MM-DD 형식)
HOLIDAYS = {
    "2025-01-01",  # 신정
    "2025-03-01",  # 삼일절
    "2025-05-05",  # 어린이날
    "2025-05-06",  # 대체공휴일
    "2025-10-06",  # 추석
    "2025-10-07",  # 추석연휴
    "2025-10-08",  # 대체공휴일
    "2025-10-09",  # 한글날
    "2025-12-25",  # 크리스마스
}

# 📆 오늘 날짜 가져오기
today = datetime.date.today().strftime("%Y-%m-%d")

# 🚫 오늘이 공휴일이면 실행하지 않고 종료
if today in HOLIDAYS:
    print(f"📢 오늘({today})은 공휴일이므로 실행하지 않습니다.")
    sys.exit(0)

# 환경 변수에서 Slack 토큰 로드
load_dotenv()
SLACK_TOKEN = os.environ.get("SLACK_TOKEN")

def send_slack_message(message, channel):
    try:
        client = WebClient(token=SLACK_TOKEN)
        client.chat_postMessage(channel=channel, text=message)
    except SlackApiError as e:
        print(f"⚠️ Error sending message to {channel} : {e}")

def main():
    for cluster in clusters:
        # 메시지 제목 설정
        header = f":loudspeaker: *『인사총무팀 공지』* <!channel>\n\n"

        notice_msg = (
            f"안녕하세요? 평택 클러스터 구성원 여러분! 인사총무팀 입니다. :blush:\n"
            f"\n"
            f"*보다 원활한 평택 클러스터 업무 환경*을 위해 아래와 같이 협조 부탁드리겠습니다.\n\n"
            f"\n"
            f":pushpin: *<https://static.wixstatic.com/media/50072f_ad740cc63d41408ba0c0f674065f80d2~mv2.png|개인가방/귀중품 현장 반입 금지>*\n\n"
            f"\n"
            f"\n"
            f":체크1: *개인 가방은 각 현장 업무 공간에 가지고 들어갈 수 없습니다.* :man-gesturing-no::woman-gesturing-no:\n\n"
            f"\n"
            f":체크1: *현장 및 업무 투입 전 반드시!! 6층 사물함에 보관해 주시기 바랍니다.* :man-gesturing-ok::ok_woman:\n\n"
            f"\n"
            f"각 배정받은 사물함 번호를 모르실 경우 아래 인원에게 문의 부탁드립니다.\n\n"
            f"\n"
            f"\n"
            f":slack: *문의사항*\n"
            f"인사총무팀_총무/시설 담당자 : <@U04RT8X7D9N> <@U07QC9WQ8JX> <@U05NXEAL43E>\n\n"
            f"\n"
            f"감사합니다.\n"
            f"\n"
        )
 
# 메시지 본문
        body = header + notice_msg

        # 슬랙 채널에 전송
        send_slack_message(body, cluster.channel)

if __name__ == "__main__":
    main()
