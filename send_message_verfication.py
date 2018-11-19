#encoding:utf-8

from selenium import webdriver
from time import sleep,time
import  unittest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

class SendMsgCase(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        #导航到饿了么的注册页面
        self.dr.get('https://h5.ele.me/login/#redirect=https%3A%2F%2Fwww.ele.me%2Fhome%2F')
        self.dr.implicitly_wait(10)

    def by_css(self,the_css):
        return  self.dr.find_element_by_css_selector(the_css)

    #手机号码输入框定位
    def mobile_phone_input_box(self):
        return self.by_css('input[type = "tel"]')

    #[免费获取验证码]按钮
    def send_msg_button(self):
         return self.by_css('.CountButton-3e-kd')

    #获取发送验证码成功文本信息
    def send_msg_successful_text(self):
        expected_result_msg = '重新获取'
        actual_result_mag = self.send_msg_button().text
        print(actual_result_mag)
        self.assertEqual(expected_result_msg, actual_result_mag)

    #发送验证码
    def send_msg(self,mobile_phone):
        self.mobile_phone_input_box().send_keys(mobile_phone)
        self.send_msg_button().click()

    #测试用例
    def test_send_msg_button(self):
        #发送验证码
        self.send_msg('15869679590')
        sleep(2)
        #验证【获取验证码】按钮被禁用
        self.assertFalse(self.send_msg_button().is_enabled())
        print(self.send_msg_button().is_enabled())
        #期望结果
        expected_result = '已发送'
        #预期结果
        actual_result = self.send_msg_button().text
        print(actual_result)
        #验证 实际结果包含预期结果'已发送'
        self.assertTrue(expected_result in actual_result)

        self.verify_msg_time('css','.CountButton-3e-kd',30)
        self.send_msg_successful_text()

    
    def verify_msg_time(self,type ,loca, total_time):
        start_time = int(time())
        end_time = int(time()) + total_time
        #print(end_time)
        i = 1
        while True:
            if self.find_elements(type,loca).is_enabled() ==True:
                print("验证码等待时间为" + str(i + 1) + "s")
            else:
                i=i+1
                sleep(1)
                start_time = int(time())
                #print(start_time)
                if start_time > end_time:
                    raise TimeoutException("超时时间为" + str(i + 1) + "s")
                    break
                continue

    def find_elements(self,type,loca):
        if   type == 'id':
            return self.dr.find_element(by=By.ID, value=loca)
        elif type == 'css':
            return self.dr.find_element(by=By.CSS_SELECTOR, value=loca)
        elif type == 'xpath':
            return self.dr.find_element(by=By.XPATH, value=loca)
        else:
           print('没有这种定位方式')

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()