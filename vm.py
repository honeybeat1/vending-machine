#change = 0
#precommand = ""

class VendingMachine:
	def __init__(self): #init = 메소드
		self._change = 0 #change = 변수
	
	def run(self,raw): #run은 메소드가 되었다 
		tokens = raw.split()
		cmd, params = tokens[0], tokens[1:]
		if cmd == "잔액":
			return "잔액은 " + str(self._change) + "원입니다"
		elif cmd == "동전" : 
			coin = params[0]
			self._change += int(coin) #100원을 int(coin)으로 대체
			return coin + "원을 넣었습니다"
		else:
			return "알 수 없는 명령입니다"





# def run(raw):
# 	global change #임시 방편
# 	global precommand

# 	tokens = raw.split()
# 	cmd, params = tokens[0], tokens[1:]

# 	if cmd == "잔액":
# 		if precommand == "고양이":
# 			return "야옹"
# 		else:
# 			return "잔액은 " + str(change) + "원입니다"
# 	elif cmd == "동전" : 
# 		coin = params[0]
# 		change += int(coin) #100원을 int(coin)으로 대체
# 		return coin + "원을 넣었습니다"
# 	else:
# 		precommand = raw
# 		return "고양이를 넣었습니다"

# def init():  #매 케이스마다 초기화 시켜주는 함수 만들기
# 	global change
# 	change = 0