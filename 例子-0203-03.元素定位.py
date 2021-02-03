#coding=utf-8
#1.导入selenium模块中的webdriver驱动程序
from selenium import webdriver
#2.定义打开的浏览器类型
br=webdriver.Chrome()
#3.打开目标网站
br.get("https://www.baidu.com")
#1.通过id进行定位
# br.find_element_by_id("kw").send_keys("小志")
#2.通过class定位
# br.find_element_by_class_name("s_ipt").send_keys("LOL")
#3.通过tag定位
# br.find_element_by_tag_name("input").send_keys("simida")
#4.link_text定位
# br.find_element_by_link_text("hao123").click()
#5.partial_link_text
# br.find_element_by_partial_link_text("闻").click()
#6.xpath定位
# br.find_element_by_xpath("//*[@id='kw']").send_keys("王者新皮肤")
#7.css定位
br.find_element_by_css_selector("#kw").send_keys("么么哒")