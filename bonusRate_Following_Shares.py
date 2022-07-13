

#! -*- coding:utf-8 -*-

import json
import datetime
import re
import time

import pymysql
import requests
from lxml import etree
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

from selenium.webdriver import PhantomJS




def use_requests(url):
    response = requests.get(url)
    return response.text









def insertDB(content,tablename):


    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='Trust',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:

        f_6 = "%s," *225
        cursor.executemany('insert into {1} (j4151,j4502,j4503,j4506,j4507,j4519,j4523,j4568,j4578,j6479,j6501,j6503,j6504,j6506,j6645,j6674,j6701,j6702,j6703,j6724,j6752,j6753,j6758,j6762,j6770,j6841,j6857,j6861,j6902,j6952,j6954,j6971,j6976,j6981,j7735,j7751,j7752,j8035,j7201,j7202,j7203,j7205,j7211,j7261,j7267,j7269,j7270,j7272,j4543,j4902,j7731,j7733,j7762,j9432,j9433,j9434,j9613,j9984,j7186,j8304,j8306,j8308,j8309,j8316,j8331,j8354,j8355,j8411,j8253,j8591,j8697,j8601,j8604,j8628,j8630,j8725,j8750,j8766,j8795,j1332,j1333,j2002,j2269,j2282,j2501,j2502,j2503,j2531,j2801,j2802,j2871,j2914,j3086,j3099,j3382,j8233,j8252,j8267,j9983,j2413,j2432,j3659,j4324,j4689,j4704,j4751,j4755,j6098,j6178,j7974,j9602,j9735,j9766,j1605,j3101,j3103,j3401,j3402,j3861,j3863,j3405,j3407,j4004,j4005,j4021,j4042,j4043,j4061,j4063,j4183,j4188,j4208,j4452,j4631,j4901,j4911,j6988,j5019,j5020,j5101,j5108,j5201,j5202,j5214,j5232,j5233,j5301,j5332,j5333,j5401,j5406,j5411,j5541,j3436,j5703,j5706,j5707,j5711,j5713,j5714,j5801,j5802,j5803,j2768,j8001,j8002,j8015,j8031,j8053,j8058,j1721,j1801,j1802,j1803,j1808,j1812,j1925,j1928,j1963,j5631,j6103,j6113,j6301,j6302,j6305,j6326,j6361,j6367,j6471,j6472,j6473,j7004,j7011,j7013,j7003,j7012,j7832,j7911,j7912,j7951,j3289,j8801,j8802,j8804,j8830,j9001,j9005,j9007,j9008,j9009,j9020,j9021,j9022,j9064,j9147,j9101,j9104,j9107,j9202,j9301,j9501,j9502,j9503,j9531,j9532) values ({0})'.format(f_6[:-1],tablename), content)
        connection.commit()
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass



def readjsonfile(filename):
    with open(filename, 'r', encoding='utf-8') as fw:
        s = json.load(fw)
        return s

#
if __name__ == '__main__':
    following_shares_ = []
    bonusRate_ = []
    resultjson = readjsonfile("nikki225_nikkei_info.json")
    for item in resultjson:
        code = item["code"]
        nikkei_url = "https://finance.yahoo.co.jp/quote/{0}.T".format(code)
        html = use_requests(nikkei_url)
        selector = etree.HTML(html)
        following_shares = selector.xpath('//*[@id="referenc"]/div/ul/li[2]/dl/dd/span[1]/span/span[1]/text()')
        following_shares_.append("".join(following_shares[0].split(",")))
        bonusRate = selector.xpath('//*[@id="referenc"]/div/ul/li[3]/dl/dd/span[1]/span/span[1]/text()')
        bonusRate_.append(bonusRate[0])
        print(following_shares)
        time.sleep(0.1)

    insertDB([tuple(bonusRate_)],"nikki225_bonus_")
    insertDB([tuple(following_shares_)],"nikki225_followingShares")


# create table nikki225_bonus_ (id int not null primary key auto_increment, j4151 text,j4502 text,j4503 text,j4506 text,j4507 text,j4519 text,j4523 text,j4568 text,j4578 text,j6479 text,j6501 text,j6503 text,j6504 text,j6506 text,j6645 text,j6674 text,j6701 text,j6702 text,j6703 text,j6724 text,j6752 text,j6753 text,j6758 text,j6762 text,j6770 text,j6841 text,j6857 text,j6861 text,j6902 text,j6952 text,j6954 text,j6971 text,j6976 text,j6981 text,j7735 text,j7751 text,j7752 text,j8035 text,j7201 text,j7202 text,j7203 text,j7205 text,j7211 text,j7261 text,j7267 text,j7269 text,j7270 text,j7272 text,j4543 text,j4902 text,j7731 text,j7733 text,j7762 text,j9432 text,j9433 text,j9434 text,j9613 text,j9984 text,j7186 text,j8304 text,j8306 text,j8308 text,j8309 text,j8316 text,j8331 text,j8354 text,j8355 text,j8411 text,j8253 text,j8591 text,j8697 text,j8601 text,j8604 text,j8628 text,j8630 text,j8725 text,j8750 text,j8766 text,j8795 text,j1332 text,j1333 text,j2002 text,j2269 text,j2282 text,j2501 text,j2502 text,j2503 text,j2531 text,j2801 text,j2802 text,j2871 text,j2914 text,j3086 text,j3099 text,j3382 text,j8233 text,j8252 text,j8267 text,j9983 text,j2413 text,j2432 text,j3659 text,j4324 text,j4689 text,j4704 text,j4751 text,j4755 text,j6098 text,j6178 text,j7974 text,j9602 text,j9735 text,j9766 text,j1605 text,j3101 text,j3103 text,j3401 text,j3402 text,j3861 text,j3863 text,j3405 text,j3407 text,j4004 text,j4005 text,j4021 text,j4042 text,j4043 text,j4061 text,j4063 text,j4183 text,j4188 text,j4208 text,j4452 text,j4631 text,j4901 text,j4911 text,j6988 text,j5019 text,j5020 text,j5101 text,j5108 text,j5201 text,j5202 text,j5214 text,j5232 text,j5233 text,j5301 text,j5332 text,j5333 text,j5401 text,j5406 text,j5411 text,j5541 text,j3436 text,j5703 text,j5706 text,j5707 text,j5711 text,j5713 text,j5714 text,j5801 text,j5802 text,j5803 text,j2768 text,j8001 text,j8002 text,j8015 text,j8031 text,j8053 text,j8058 text,j1721 text,j1801 text,j1802 text,j1803 text,j1808 text,j1812 text,j1925 text,j1928 text,j1963 text,j5631 text,j6103 text,j6113 text,j6301 text,j6302 text,j6305 text,j6326 text,j6361 text,j6367 text,j6471 text,j6472 text,j6473 text,j7004 text,j7011 text,j7013 text,j7003 text,j7012 text,j7832 text,j7911 text,j7912 text,j7951 text,j3289 text,j8801 text,j8802 text,j8804 text,j8830 text,j9001 text,j9005 text,j9007 text,j9008 text,j9009 text,j9020 text,j9021 text,j9022 text,j9064 text,j9147 text,j9101 text,j9104 text,j9107 text,j9202 text,j9301 text,j9501 text,j9502 text,j9503 text,j9531 text,j9532 text,LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP) engine=InnoDB  charset=utf8;
#
#
#
# create table nikki225_followingShares (id int not null primary key auto_increment, j4151 text,j4502 text,j4503 text,j4506 text,j4507 text,j4519 text,j4523 text,j4568 text,j4578 text,j6479 text,j6501 text,j6503 text,j6504 text,j6506 text,j6645 text,j6674 text,j6701 text,j6702 text,j6703 text,j6724 text,j6752 text,j6753 text,j6758 text,j6762 text,j6770 text,j6841 text,j6857 text,j6861 text,j6902 text,j6952 text,j6954 text,j6971 text,j6976 text,j6981 text,j7735 text,j7751 text,j7752 text,j8035 text,j7201 text,j7202 text,j7203 text,j7205 text,j7211 text,j7261 text,j7267 text,j7269 text,j7270 text,j7272 text,j4543 text,j4902 text,j7731 text,j7733 text,j7762 text,j9432 text,j9433 text,j9434 text,j9613 text,j9984 text,j7186 text,j8304 text,j8306 text,j8308 text,j8309 text,j8316 text,j8331 text,j8354 text,j8355 text,j8411 text,j8253 text,j8591 text,j8697 text,j8601 text,j8604 text,j8628 text,j8630 text,j8725 text,j8750 text,j8766 text,j8795 text,j1332 text,j1333 text,j2002 text,j2269 text,j2282 text,j2501 text,j2502 text,j2503 text,j2531 text,j2801 text,j2802 text,j2871 text,j2914 text,j3086 text,j3099 text,j3382 text,j8233 text,j8252 text,j8267 text,j9983 text,j2413 text,j2432 text,j3659 text,j4324 text,j4689 text,j4704 text,j4751 text,j4755 text,j6098 text,j6178 text,j7974 text,j9602 text,j9735 text,j9766 text,j1605 text,j3101 text,j3103 text,j3401 text,j3402 text,j3861 text,j3863 text,j3405 text,j3407 text,j4004 text,j4005 text,j4021 text,j4042 text,j4043 text,j4061 text,j4063 text,j4183 text,j4188 text,j4208 text,j4452 text,j4631 text,j4901 text,j4911 text,j6988 text,j5019 text,j5020 text,j5101 text,j5108 text,j5201 text,j5202 text,j5214 text,j5232 text,j5233 text,j5301 text,j5332 text,j5333 text,j5401 text,j5406 text,j5411 text,j5541 text,j3436 text,j5703 text,j5706 text,j5707 text,j5711 text,j5713 text,j5714 text,j5801 text,j5802 text,j5803 text,j2768 text,j8001 text,j8002 text,j8015 text,j8031 text,j8053 text,j8058 text,j1721 text,j1801 text,j1802 text,j1803 text,j1808 text,j1812 text,j1925 text,j1928 text,j1963 text,j5631 text,j6103 text,j6113 text,j6301 text,j6302 text,j6305 text,j6326 text,j6361 text,j6367 text,j6471 text,j6472 text,j6473 text,j7004 text,j7011 text,j7013 text,j7003 text,j7012 text,j7832 text,j7911 text,j7912 text,j7951 text,j3289 text,j8801 text,j8802 text,j8804 text,j8830 text,j9001 text,j9005 text,j9007 text,j9008 text,j9009 text,j9020 text,j9021 text,j9022 text,j9064 text,j9147 text,j9101 text,j9104 text,j9107 text,j9202 text,j9301 text,j9501 text,j9502 text,j9503 text,j9531 text,j9532 text,LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP) engine=InnoDB  charset=utf8;
