change = 0


def run(raw):
	global change #임시 방편

	tokens = raw.split()
	cmd, params = tokens[0], tokens[1:]

	if cmd == "잔액":
		return "잔액은 " + str(change) + "원입니다"
	elif cmd == "동전" : 
		coin = params[0]
		change += int(coin) #100원을 int(coin)으로 대체
		return coin + "원을 넣었습니다"
	else:
		return "알 수 없는 명령입니다."

def init():  #매 케이스마다 초기화 시켜주는 함수 만들기
	global change
	change = 0