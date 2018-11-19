#encoding:utf-8

from selenium import webdriver
from time import sleep,time
import  unittest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

class SendMsgCase(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        #����������ô��ע��ҳ��
        self.dr.get('https://h5.ele.me/login/#redirect=https%3A%2F%2Fwww.ele.me%2Fhome%2F')
        self.dr.implicitly_wait(10)

    def by_css(self,the_css):
        return  self.dr.find_element_by_css_selector(the_css)

    #�ֻ����������λ
    def mobile_phone_input_box(self):
        return self.by_css('input[type = "tel"]')

    #[��ѻ�ȡ��֤��]��ť
    def send_msg_button(self):
         return self.by_css('.CountButton-3e-kd')

    #��ȡ������֤��ɹ��ı���Ϣ
    def send_msg_successful_text(self):
        expected_result_msg = '���»�ȡ'
        actual_result_mag = self.send_msg_button().text
        print(actual_result_mag)
        self.assertEqual(expected_result_msg, actual_result_mag)

    #������֤��
    def send_msg(self,mobile_phone):
        self.mobile_phone_input_box().send_keys(mobile_phone)
        self.send_msg_button().click()

    #��������
    def test_send_msg_button(self):
        #������֤��
        self.send_msg('15869679590')
        sleep(2)
        #��֤����ȡ��֤�롿��ť������
        self.assertFalse(self.send_msg_button().is_enabled())
        print(self.send_msg_button().is_enabled())
        #�������
        expected_result = '�ѷ���'
        #Ԥ�ڽ��
        actual_result = self.send_msg_button().text
        print(actual_result)
        #��֤ ʵ�ʽ������Ԥ�ڽ��'�ѷ���'
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
                print("��֤��ȴ�ʱ��Ϊ" + str(i + 1) + "s")
            else:
                i=i+1
                sleep(1)
                start_time = int(time())
                #print(start_time)
                if start_time > end_time:
                    raise TimeoutException("��ʱʱ��Ϊ" + str(i + 1) + "s")
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
           print('û�����ֶ�λ��ʽ')

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()