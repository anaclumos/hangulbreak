# Developed by Sunghyun Cho on Feb 25, 2019.

class 한글분해():

	초성들 = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
	중성들 = ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"]
	종성들 = ["", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]

	def __init__(self, 입력):
		self.원본 = 입력
		if not ord('가') <= ord(입력) <= ord('힣'):
			self.종성 = "   "
			self.중성 = "   "
			self.초성 = " " + 입력 + " "
		else:
			self.임시 = ord(입력) - 0xAC00
			self.종성번호 = int(self.임시 % 28)
			self.중성번호 = int(((self.임시 - self.종성번호) / 28 ) % 21)
			self.초성번호 = int((((self.임시 - self.종성번호) / 28 ) - self.중성번호 ) / 21)
			self.종성 = self.종성들[self.종성번호]
			self.중성 = self.중성들[self.중성번호]
			self.초성 = self.초성들[self.초성번호]

	def 종성이_있다면(self):
		if self.종성 != "":
			return True
		else:
			return False

	def 가로형중성을_가진다면(self):
		if self.중성 in ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅣ"]:
			return True
		else:
			return False

	def 인쇄(self):
		print(self.원본, "을 분해함. 초성:", self.초성, "중성:", self.중성, "종성:", self.종성)

def 차원분석(파자):
	길이 = 1 # 초성의 길이
	높이 = 1 # 초성의 높이

	if 파자.가로형중성을_가진다면():
		길이 = 길이 + 1
	else:
		높이 = 높이 + 1
	if 파자.종성이_있다면():
		높이 = 높이 + 1
	return [길이, 높이]

깨야할_한글 = list(input("\x1b[1;32m" + "깰 한글을 입력하세요: " + "\x1b[0m"))
줄1 = []
줄2 = []
줄3 = []

for 한글 in 깨야할_한글:
	파자 = 한글분해(한글)
	차원 = 차원분석(파자)
	길이 = 차원[0]
	높이 = 차원[1]
	if 길이 == 2:
		줄1.append(파자.초성 + 파자.중성)
		if(높이 == 2):
			줄2.append("  " + 파자.종성)
		else:
			줄2.append("    ")
		줄3.append("    ")
	else:
		줄1.append(파자.초성)
		줄2.append(파자.중성)
		if 높이 == 3:
			줄3.append(파자.종성)
		else:
			줄3.append("  ")

print("\n\x1b[1;32m" + "결과: " + "\x1b[0m\n")
for 글자 in 줄1:
	print(글자, end="")
print()
for 글자 in 줄2:
	print(글자, end="")
print()
for 글자 in 줄3:
	print(글자, end="")
print()