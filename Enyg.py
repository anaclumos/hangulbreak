# ENYGma (Eun-Neun-Yi-Ga)
# Developed by Sunghyun Cho on March 9th, 2019.

from decomposer import hangulbreaker as hb

def pronounceInKorean(word):
	# modify accordingly for your use
	return word

def enygma(string, highlight):
	wordList = string.split()
	newString = ""
	for word in wordList:
		word = pronounceInKorean(word)
		if word.find("[을or를]") != -1:
			jong = hb(word[word.find("[을or를]")-1]).종성이_있다면()
			josa = "을" if jong else "를"
			if highlight:
				word = word.replace("[을or를]", "\x1b[1;32m" + josa + "\x1b[0m")
			else:
				word = word.replace("[을or를]", josa)
		if word.find("[은or는]") != -1:
			jong = hb(word[word.find("[은or는]")-1]).종성이_있다면()
			josa = "은" if jong else "는"
			if highlight:
				word = word.replace("[은or는]", "\x1b[1;32m" + josa + "\x1b[0m")
			else:
				word = word.replace("[은or는]", josa)
		if word.find("[이or가]") != -1:
			jong = hb(word[word.find("[이or가]")-1]).종성이_있다면()
			josa = "이" if jong else "가"
			if highlight:
				word = word.replace("[이or가]", "\x1b[1;32m" + josa + "\x1b[0m")
			else:
				word = word.replace("[이or가]", josa)
		newString = newString + " " + word
	return newString[1:]

print()
print(enygma(
	"안녕하세요! 저[은or는] 조성현이라고 합니다."
	, highlight = True))
print()
print(enygma(
	"생활코딩 페이스북 그룹[은or는] 코딩[을or를] 처음 시작하는 분들이 서로[을or를] 돕기 위해서 시작된 커뮤니티입니다."
	, highlight = True))
print()
print(enygma(
	"코딩이라는 범위 안에서 정보와 의견[을or를] 나누는 공간입니다. 활동[을or를] 시작하기 전에 가이드[을or를] 읽어주세요."
	, highlight = True))
print()
items = ["아이폰", "아이패드", "아이팟", "맥"]
for item in items:
	print(enygma(
		"{}[이or가] 비활성화되었습니다.".format(item)
		, highlight = True))
print()