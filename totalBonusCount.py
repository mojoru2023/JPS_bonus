
#! -*- coding:utf-8 -*-

import json
import datetime
import operator
import re
import time

import pymysql
import requests
from lxml import etree
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
#
# from selenium.webdriver import PhantomJS




def use_requests(url):
    driver.get(url)
    # time.sleep(3)
    html = driver.page_source
    return html





def writeintoTSV_file(filename, data):
    with open(filename, 'a', encoding="utf-8") as f_output:
        tsv_output = csv.writer(f_output, delimiter='\t')
        tsv_output.writerow(data)

from selenium import webdriver
import csv
driver = webdriver.Chrome()
def readjsonfile(filename):
    with open(filename, 'r', encoding='utf-8') as fw:
        s = json.load(fw)
        return s

#
def exec_dot(string_args):
    if "," in string_args:
        ret = "".join(string_args.split(","))
    else:
        ret = string_args
    return ret


def get_bonus(url):
    driver.get(url)
    # time.sleep(3)
    html = driver.page_source
    pattern = re.compile('<th>一株配当（円）<a href=".*?" target="_blank"><i class="m-iconQ">（解説）</i></a></th>'+'(.*?)<h3 class="m-headlineSmall_text">中間業績</h3>'
                        ,re.S)
    items = re.findall(pattern,html)
    pattern2 = re.compile('<td class="a-taR a-wordBreakAll">(.*?)</td>',re.S)
    items2 = re.findall(pattern2,items[0])

    print(items2[4])
    ret = exec_dot(items2[4])

    return ret

if __name__ == '__main__':
    ret = exec_dot("1,711.00")


    f_list = []


    resultjson = readjsonfile("nikki225_nikkei_info.json")
    for item in resultjson:
        code = item["code"]
        if code != "8355":

            industry_info = item["industry_info"]

            nikkei_url = "https://finance.yahoo.co.jp/quote/{0}.T".format(code)
            html = use_requests(nikkei_url)
            selector = etree.HTML(html)
            oneDict = {}
            name = selector.xpath('//*[@id="root"]/main/div/div/div[1]/div[2]/section[1]/div[2]/header/div[1]/h1/text()')
            following_shares = selector.xpath('//*[@id="referenc"]/div/ul/li[2]/dl/dd/span[1]/span/span[1]/text()')
            f_shares = int("".join("".join(following_shares[0].split(","))))

            OneStockBonus = get_bonus("https://www.nikkei.com/nkd/company/kessan/?scode={0}&ba=1".format(code))
            f_OneStockBonus = float(OneStockBonus)
            totalBonusCount = str(round(f_shares*f_OneStockBonus/(100000000),2)) + " 憶"
            intTotalBonusCOunt = f_shares*f_OneStockBonus/(100000000)
            bonusRate = selector.xpath('//*[@id="referenc"]/div/ul/li[3]/dl/dd/span[1]/span/span[1]/text()')
            f_bonusRate = bonusRate[0] + "%"
            oneDict["code"] =code
            oneDict["name"] =name[0]
            oneDict["industry_info"] =industry_info
            oneDict["totalBonusCount"] =totalBonusCount
            oneDict["f_bonusRate"] =f_bonusRate
            oneDict["intTotalBonusCOunt"] =intTotalBonusCOunt
            print(oneDict)
            time.sleep(1)
            f_list.append(oneDict)

    for item in f_list:
        writeintoTSV_file("d.tsv",[item["code"],item["name"],item["industry_info"],item["totalBonusCount"],item["f_bonusRate"]])



# https://faq.nomura.co.jp/app/answers/detail/a_id/390/~/%E9%85%8D%E5%BD%93%E9%87%91%E3%81%AB%E5%AF%BE%E3%81%99%E3%82%8B%E7%A8%8E%E9%87%91%E3%82%92%E6%95%99%E3%81%88%E3%81%A6%E3%81%8F%E3%81%A0%E3%81%95%E3%81%84%E3%80%82
# https://www.oag-tax.co.jp/asset-campus-oag/stock-dividend-tax-924

# 日股中哪些公司，哪些行业在大撒币