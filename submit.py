# coding:utf-8

from selenium import webdriver
import datetime
from calendar import monthrange

# 这里填你的信息
NAME = "xxx"  # 姓名
CLASS = "xxx"  # 班级
MAJOR = "xxxx"  # 专业
DIVISION = "xxxx"  # 学部

chrome_options = webdriver.ChromeOptions()

# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')

# 配置chromedriver.exe 路径
driver_path = "C:\\Users\\Lion\\AppData\\Local\\Programs\\Python\\Python37\\chromedriver.exe"
browser = webdriver.Chrome(options=chrome_options, executable_path=driver_path)
browser.maximize_window()  # 全屏

browser.get('http://forms.ebdan.net/ls/ZLtcdcg7?tdsourcetag=s_pcqq_aiomsg')


# 定义点击按钮 防止没有点击成功 一直点击直到成功
def Input(element, attr=None, IsId=True, IsClick=True):
    while True:
        try:
            # 不是Id就选中css_selector
            if IsId:
                elem = browser.find_element_by_id(element)
            else:
                elem = browser.find_element_by_css_selector(element)
            # 如果是点击事件
            if IsClick:
                elem.click()
            # 否则就是填写事件
            else:
                elem.send_keys(attr)
            break
        except:
            pass


# 提交
def submit(date):
    # 点击日期按钮
    Input("924328816")
    # 选择打卡日期
    Input("td[lay-ymd='2021-" + date, IsId=False)
    # 填写姓名
    Input("9416621315", IsClick=False, attr=NAME)
    # 页面滚动到底部
    browser.execute_script("arguments[0].scrollIntoView();", browser.find_element_by_id("2132429317"))
    # 填写班级
    Input("4599408663", IsClick=False, attr=CLASS)
    # 填写专业
    Input("2132429317", IsClick=False, attr=MAJOR)
    # 填写学部
    Input("5935269394", IsClick=False, attr=DIVISION)
    # 填写提交人
    Input("2117781682", IsClick=False, attr=NAME)
    # 点击提交
    browser.find_element_by_id("203872787").click()
    # 刷新浏览器
    browser.refresh()


if __name__ == '__main__':

    # 打卡范围 默认是本月的1号-最后一天
    """
        如果本月是1月，那么打卡的范围是
        2021-1-1 - 2021-1-31
        如果本月是2月，那么打卡的范围是
        2021-2-1 - 2021-2-28
    """

    # 本月打卡起始日期，默认1号
    startDay = 1
    # 本月打卡终止日期，默认是本月最后一天
    month = datetime.datetime.now().month
    endDay = monthrange(2021, month)[1]

    # 循环打卡
    for i in range(startDay, endDay + 1):
        date = str(month) + "-" + str(i) + "'"
        submit(date)
        print("2021-" + str(month) + "-" + str(i) + " " + "打卡成功")

    # 关闭浏览器
    browser.close()
    # 退出浏览器
    browser.quit()
