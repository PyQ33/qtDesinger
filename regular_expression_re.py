#!/usr/bin/env python
# coding: utf-8

# # 메타문자
# 
# 메타 문자	설명 
# 
# *   "[ ]"	문자 클래스
# * "."	\n을 제외한 모든 문자와 매치 (점 하나는 글자 하나를 의미) 
# *	"*" 0회 이상 반복 (업어도 상관 없음)  
# * "+"1 회 이상 반복 (무조건 한번 이상 등장해야 함) 
# * l	or 조건식을 의미 
# * ^	문자열의 시작 의미 
# * $	문자열의 끝을 의미 
# * ?	0회 이상 1회 이하 
# * \	이스케이프, 또는 메타 문자를 일반 문자로 인식하게 한다 \n\n
# *( )	그룹핑, 추출할 패턴을 지정한다. \n\n

# In[1]:


# from google.colab import drive
# drive.mount('/content/drive')


# In[2]:


#!pip install -U finance-datareader


# In[3]:

global df
import pandas as pd
from pandas.tseries.offsets import BDay, Day

today = pd.datetime.today()
what_date1 = today-BDay(1)
what_date2 = today

what_date1 = format(what_date1,'%Y%m%d')
what_date2 = format(what_date2,'%Y%m%d')
print(f'{what_date1}: {what_date2}')
print(type(what_date1))


# In[4]:




import os
os.getcwd() 
import sys
sys.path
# sys.path.append(os.getcwd() )


# In[5]:


#!pip install -U finance-datareader
import FinanceDataReader as fdr
try:
  print(f'-----------is Exist KRX_list')
  all_tickers= pd.read_csv(f'tickersKRX_list.csv', encoding='utf-8-sig')
except Exception as e:
  print(f'{e} ----------Lets crawl KRX')
  all_tickers = fdr.StockListing('KRX')
  all_tickers.to_csv(f'tickersKRX_list.csv', encoding='utf-8-sig')

# In[7]:
import time

#import time
#time.sleep(1)
#df_etf_kr = fdr.EtfListing(country= 'KR') # 'KR' 생략가능
# df_etf_kr.to_csv('etflisting_kr.csv',encoding = 'utf-8')
# df_etf_kr.head()

# all_tickers.to_csv(f'/content/drive/My Drive/Colab Notebooks/tickers_info_{what_date2}.csv',encoding='utf-8')
# df_etf_kr.to_csv(f'/content/drive/My Drive/Colab Notebooks/etfs_info_{what_date2}.csv',encoding='utf-8')
# all_tickers = pd.read_csv(f'/content/drive/My Drive/Colab Notebooks/캡스톤_공모주상장첫날가격예측/tickers_info.csv', encoding='utf-8')
try:
  # if i have ETF csv list
  df_etf_kr = pd.read_csv(f'etflisting_kr.csv', encoding='utf-8')

except Exception as e:
  print(e)
  df_etf_kr = fdr.EtfListing(country= 'KR') # 'KR' 생략가능
  df_etf_kr.to_csv('etflisting_kr.csv',encoding = 'utf-8')
  time.sleep(1)

# In[8]:


import re


# # Find text INPUT
# ###### 한줄에 하나씩 
# ######+-숫자 drop 가능
# if Error -> text 이후 셀 의 리스트 확인하기
# # 
# # KRX or KiwoomAPI 로 근원물 선물 Ticker 도 추가하자

# In[39]:

# import regular_expression_QTable
#
# try:
#   text = regular_expression_QTable.MyWindow.TextEdit
#
# except Exception as e:
#   print(e)
text = """
현대차2우
현대차3우
현대차우

  """


def input_text(text):
  text = str(text)
  return text

# # Run --searchTICKER

# In[40]:



import re
#text = input(str())
import pandas as pd
df = pd.DataFrame()


def text2df(text):
  df = pd.DataFrame()
  인컴 = []
  프리미엄 = []
  for unit in re.findall('\w+', input_text(text)):
    if unit == "인컴":

      인컴 = []
    elif unit == "프리미엄":

      프리미엄 = []
    elif unit == '시그널':
      시그널 = []
    
    elif unit == "보":
      None
    elif unit == '0':
      None
    elif unit == '1':
      None
    elif unit == '2':
      None
    elif unit == '3':
      None
    elif unit == 'HIGH_D':
      None
    elif unit == '인컴펀드':
      None
    elif unit == '프리미엄펀드':
      None
    elif unit == '3시':
      None
    elif unit == '우선주인컴':
      None
    elif unit == '우선주프리미엄':
      None
    elif unit == '2시':
      None
    elif unit == '편출':
      None
    else:
      인컴.append(unit)
      프리미엄.append(unit)
  print(인컴)


  df['인컴']= pd.Series(인컴)
  #df['프리미엄']= pd.Series(프리미엄)
  df['general']= pd.Series(인컴).str.replace('우',"").replace('2B','')

  codes = []
  import numpy as np
  for unit in list(df.인컴.values):
    if unit == "Cj제일제당우" or unit == "CJ제일제당우":
      unit = "CJ제일제당 우"
    elif unit == "KODEX200" or  unit == "kodex200":
      unit = "KODEX 200"  # if KODEX str.contains -> KODEX&" "& *
    elif unit == "KT":
      unit = "케이티"  # if KODEX str.contains -> KODEX&" "& *
    elif unit == "sk이노우" or  unit == "SK이노우" or unit == "에스케이노우" or unit == "에스케이이노베이션우":
      unit = "SK이노베이션우"  # if KODEX str.contains -> KODEX&" "& *


    else:
      None
    print(unit)
    try:
      # ------------------as 보통주
      codes_unit = all_tickers.Symbol[all_tickers.Name == unit]
      print(f'{codes_unit}------- Find')
      codes.append(str(codes_unit.array[0]).zfill(6))
    
    except Exception as e:
      print(e)
      #codes_unit = df_etf_kr.Symbol[df_etf_kr['Name'].str.contains(unit)]
      try:
        # --------------as 우선주
        codes_unit = all_tickers.Symbol[all_tickers.Name.str.contains(unit)]
        codes.append(str(codes_unit.array[0]).zfill(6))
      except Exception as e:
        # --------------as ETF
        codes_unit = df_etf_kr.Symbol[df_etf_kr['Name'] == unit]
        codes.append(str(codes_unit.array[0]).zfill(6))
    print(f'{unit} : {codes_unit.array[0]}')
  #codes
  df['ticker'] = pd.Series(codes)
  return df

  # # Searched

# In[11]:


print(text2df(text))


# # 아래는 확인용 view

# In[12]:

#
# all_tickers.Symbol[all_tickers.Name.str.contains(unit)]


# In[13]:


#
# df_etf_kr.Name[df_etf_kr['Name'] ==(unit)]
# #all_tickers[all_tickers.Name.str.contains("대림산업")]
# codes_unit

