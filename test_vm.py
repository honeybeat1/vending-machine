from vm import VendingMachine #run, init  #모르는 함수 나오면 항상 임포트 해주새요 


def test_initial_change_should_be_zero():
	m = VendingMachine()
	assert "잔액은 0원입니다" == m.run("잔액")

def test_insert_coin_and_check():
	m = VendingMachine()
	assert "100원을 넣었습니다" == m.run("동전 100")
	assert "잔액은 100원입니다" == m.run("잔액")

def test_accumulation_of_change():
 	m = VendingMachine()
 	m.run("동전 100")
 	m.run("동전 100")
 	assert "잔액은 200원입니다" == m.run("잔액")

# def test_meow():
# 	init()
# 	assert "알 수 없는 명령입니다." == run("고양이")