# Developed by Sunghyun Cho on Feb 25, 2019.

from decomposer import hangulbreaker as 한글분해

글자인쇄최대길이 = 40

def 차원분석(파자):
    길이 = 1 # 초성의 길이
    높이 = 1 # 초성의 높이

    if 파자.가로형중성을_가진다면():
        길이 = 길이 + 1
    elif 파자.이중모음을_가진다면():
        길이 = 길이 + 1
        높이 = 높이 + 1
    else:
        높이 = 높이 + 1
    if 파자.종성이_있다면() and not 파자.이중모음을_가진다면():
        높이 = 높이 + 1
    return [길이, 높이]

def 인쇄(줄1, 줄2, 줄3):
    for 글자 in 줄1:
        print(글자, end="")
    print()
    for 글자 in 줄2:
        print(글자, end="")
    print()
    for 글자 in 줄3:
        print(글자, end="")
    print("\n")

def 문장잘라인쇄(줄1, 줄2, 줄3):
    위치 = 글자인쇄최대길이
    남은길이 = len(줄1)
    if 위치 < 남은길이:
        while (줄1[위치] != "   " or 줄2[위치] != "   " or 줄3[위치] != "   "):
            if 위치 < 남은길이 - 1:
                위치 = 위치 + 1
            else:
                break
        인쇄(줄1[:위치+1], 줄2[:위치+1], 줄3[:위치+1])
        문장잘라인쇄(줄1[위치+1:], 줄2[위치+1:], 줄3[위치+1:])
    else:
        인쇄(줄1, 줄2, 줄3)

깨야할_한글 = list(input("\n\x1b[1;32m" + "깰 한글을 입력하세요: " + "\x1b[0m"))
줄1 = []
줄2 = []
줄3 = []

for 한글 in 깨야할_한글:
    파자 = 한글분해(한글)
    차원 = 차원분석(파자)
    길이 = 차원[0]
    높이 = 차원[1]
    if 길이 == 2:
        줄1.append(파자.초성)
        if not 파자.이중모음을_가진다면():
            줄1.append(파자.중성)
            if(높이 == 2):
                줄2.append("  ")
                줄2.append(파자.종성)
            else:
                for 위치 in range(길이):
                    줄2.append("  ")
            for 위치 in range(길이):
                줄3.append("  ")
        else:
            if 파자.중성 in ["ㅘ", "ㅙ", "ㅚ"]:
                줄2.append("ㅗ")
            elif 파자.중성 in ["ㅝ", "ㅞ", "ㅟ"]:
                줄2.append("ㅜ")
            else:
                줄2.append("ㅡ")
            if 파자.중성 in ("ㅚ", "ㅟ", "ㅢ"):
                줄1.append("ㅣ")
            if 파자.중성 == "ㅘ":
                줄1.append("ㅏ")
            if 파자.중성 == "ㅙ":
                줄1.append("ㅐ")
            if 파자.중성 == "ㅝ":
                줄1.append("ㅓ")
            if 파자.중성 == "ㅞ":
                줄1.append("ㅔ")
            if 파자.종성 != "":
                줄2.append(파자.종성)
            else:
                줄2.append("  ")
            for 위치 in range(길이):
                줄3.append("  ")
    else:
        줄1.append(파자.초성)
        줄2.append(파자.중성)
        if 높이 == 3:
            줄3.append(파자.종성)
        else:
            줄3.append("  ")

if len(줄1) > 글자인쇄최대길이:
    if input("\n\x1b[1;32m" + "문장이 긴 것 같습니다. 자동으로 줄을 바꿀까요?" + "\x1b[0m\n" + "  1 : 예\n그외: 아니오\n결정: ") == "1":
        print("\n\x1b[1;32m" + "결과: " + "\x1b[0m\n")
        문장잘라인쇄(줄1, 줄2, 줄3)
    else:
        print("\n\x1b[1;32m" + "결과: " + "\x1b[0m\n")
        인쇄(줄1, 줄2, 줄3)
else:
    print("\n\x1b[1;32m" + "결과: " + "\x1b[0m\n")
    인쇄(줄1, 줄2, 줄3)