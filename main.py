import sys
import xlrd as xl
from skimage import io
import requests
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.wjx.cn/login.aspx")

elem_user = driver.find_element_by_id("UserName")
elem_user.send_keys("18800155112")
elem_pwd = driver.find_element_by_id("Password")
elem_pwd.send_keys("277772316227")
# 点击登录按钮
driver.find_element_by_id("LoginButton").click()

if __name__ == "__main__":
    xls_file = xl.open_workbook("./cwh.xls")
    print(len(xls_file.sheets()))
    xls_sheet = xls_file.sheets()[0]

    # exit()
    for i in range(1, xls_sheet.nrows):
        data = xls_sheet.row_values(i)
        file_name = str(data[6]) + "_" + str(data[7]) + "_" + str(data[8])
        for j in range(10, 14):
            if str(data[j])[0] == 'h':
                print(data[j])
                driver.get(data[j])
                time.sleep(3)
        print(file_name)
        time.sleep(10)
    rows = xls_sheet.row_values(0)
    print(rows)

    driver.close()