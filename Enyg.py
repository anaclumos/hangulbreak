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