from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
print("라이브러리 임포트 완료".rjust(20, '-'))

# 드라이버 준비
driver = webdriver.Chrome()
url = "https://www.google.com"
driver.get(url)
# driver.maximize_window()

# 드라이버 제어 변수 설정
action = ActionChains(driver)

#로그인 버튼 클릭 (#은 id)
driver.find_element_by_css_selector("#gb_70").click()

#아이디 입력
action.send_keys("test@gmail.com").perform()
action.reset_actions()
action = ActionChains(driver)

#다음버튼 클릭 (.은 클래스)
driver.find_element_by_css_selector(".CwaK9").click()

time.sleep(3.0)
#비밀번호 입력 (클래스 명에 빈 공간이 있으면 빈 공간 제거 후 .으로 대체)
driver.find_element_by_css_selector(".whsOnd.zHQkBf").send_keys("password")

#다음버튼 클릭
driver.find_element_by_css_selector(".CwaK9").click()
time.sleep(2)

# 메일 접근
driver.get("https://mail.google.com/mail/u/0/?ogbl#inbox")

#메일쓰기 접근
time.sleep(2)
driver.find_element_by_css_selector(".T-I.J-J5-Ji.T-I-KE.L3").click()
time.sleep(2)

send_button = driver.find_element_by_css_selector(".gU.Up")

#메일 쓰기
action.send_keys("kisang6710@gmail.com").pause(2).key_down(Keys.TAB).pause(1).key_down(Keys.TAB)\
    .send_keys("메일 자동화 테스트").pause(2).key_down(Keys.TAB).pause(1)\
    .send_keys("메일 자동화 테스트합니다").pause(2).key_down(Keys.TAB).pause(1)\
    .move_to_element(send_button).click()\
    .perform()









