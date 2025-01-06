import random

def generate_lotto_numbers():
    print("✨ 로또 번호 생성기 ✨")
    print("행운의 숫자를 골라드립니다! 잠시만 기다려주세요... 🎲")

    # 로또 번호 생성 (1~45 사이의 숫자 6개, 중복 없음)
    numbers = random.sample(range(1, 46), 6)
    numbers.sort()

    print(f"🎉 오늘의 행운 번호: {numbers} 🎉")
    print("다음 주 대박을 기원합니다! 💰")

# 함수 실행
generate_lotto_numbers()
