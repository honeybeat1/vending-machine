from vm import VendingMachine 

def test_초기_잔액은_0원():
	m = VendingMachine()
	assert "잔액은 0원입니다" == m.run("잔액")

def test_동전_넣고_잔액_검사():
	m = VendingMachine()
	assert "100원을 넣었습니다" == m.run("동전 100")
	assert "잔액은 100원입니다" == m.run("잔액")

def test_잔액_누적():
 	m = VendingMachine()
 	m.run("동전 100")
 	m.run("동전 100")
 	assert "잔액은 200원입니다" == m.run("잔액")

def test_음료_뽑기():
	m = VendingMachine()
	m.run("동전 500")
	assert "커피가 나왔습니다" + """
---@-----
|  coffee |
|         |
---------  """ == m.run("음료 커피")
	assert "잔액은 350원입니다" == m.run('잔액')

def test_모르는_음료_뽑기():
 	m = VendingMachine()
 	m.run("동전 500")
 	assert "알 수 없는 음료입니다" == m.run("음료 맥주")
 	assert "잔액은 500원입니다" == m.run("잔액")

def test_동전이_부족한_상황에서_음료_뽑기():
    m = VendingMachine()
    m.run("동전 100")
    assert "잔액이 부족합니다" == m.run("음료 커피")
    assert "잔액은 100원입니다" == m.run("잔액")

def test_유효한_동전():
	m = VendingMachine()
	valid_coins = ['10','50','100','500']
	for coin in valid_coins:
		assert coin + "원을 넣었습니다" == m.run('동전 '+ coin)

def test_유효하지_않은_동전():
	m = VendingMachine()
	assert "모르는 동전입니다" == m.run("동전 999")





#run, init  #모르는 함수 나오면 항상 임포트 해주새요 


# def test_coffee():
# 	m = VendingMachine()
# 	assert """
# ---@-----
# |  coffee |
# |         |
# ---------  """ == m.run("커피")

# def test_coffee_lack():
# 	m = VendingMachine()
# 	assert "잔액이 부족합니다." == m.run("커피")

# def test_meow():
# 	init()
# 	assert "알 수 없는 명령입니다." == run("고양이")

