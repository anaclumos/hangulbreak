from Enyg import enygma as e

print()

print(e("안녕하세요! 저[은or는] 조성현이라고 합니다.", True))
print(e("생활코딩 페이스북 그룹[은or는] 코딩[을or를] 처음 시작하는 분들이 서로[을or를] 돕기 위해서 시작된 커뮤니티입니다.", True))
print(e("코딩이라는 범위 안에서 정보와 의견[을or를] 나누는 공간입니다. 활동[을or를] 시작하기 전에 가이드[을or를] 읽어주세요.", True))

items = ["아이폰", "아이패드", "아이팟", "맥"]
for item in items:
	print(e("{}[이or가] 비활성화되었습니다.".format(item), True))

print()