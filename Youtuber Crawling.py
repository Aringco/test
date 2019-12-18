#!/usr/bin/env python
# coding: utf-8

# In[104]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import csv


# In[108]:


driver = webdriver.Chrome('C:/Users/kange/Downloads/chromedriver.exe')
driver.get('https://www.youtube.com/channel/UCXhTIte6TjoItbiUVUnMIlA/videos')


time.sleep(5)
endk = 8
while endk:
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(0.3)
    endk -= 1

page = driver.page_source

soup = BeautifulSoup(page,'lxml')

all_title = soup.find_all('a','yt-simple-endpoint style-scope ytd-grid-video-renderer')
title = [soup.find_all('a','yt-simple-endpoint style-scope ytd-grid-video-renderer')[n].string for n in range(0,len(all_title))]
for i in range(0, len(title)):
    title[i] = str(title[i])
print(title)

all_title = list(soup.find_all('a','yt-simple-endpoint style-scope ytd-grid-video-renderer'))
title_tag = []
viewed = []
for i in range(0, len(all_title)):
    title_tag.append(str(all_title[i]))
for i in range(0, len(title_tag)):
    viewed.append(title_tag[i].split('"')[1].split(' ')[-1])
for i in range(0, len(viewed)):
    viewed[i] = int(viewed[i].rstrip('회').replace(',',''))
print(viewed)

all_video_time = soup.find_all('span','style-scope ytd-thumbnail-overlay-time-status-renderer')
video_time = [soup.find_all('span','style-scope ytd-thumbnail-overlay-time-status-renderer')[n].string.strip() for n in range(0,len(all_video_time))]
print(video_time)
    
all_upload_time = soup.find_all('span', 'style-scope ytd-grid-video-renderer')
upload_time = [soup.find_all('span', 'style-scope ytd-grid-video-renderer')[n].string for n in range(1, len(all_upload_time)+1,2)]
print(upload_time)

channel = soup.find('yt-formatted-string','style-scope ytd-channel-name').string
print(channel)

sub_num = soup.find('yt-formatted-string','style-scope ytd-c4-tabbed-header-renderer').string
print(sub_num)

youtube_video_list = []

for i in range(1,len(all_title)):
    roww = []
    roww.append(title[i])
    roww.append(video_time[i])
    roww.append(viewed[i])
    roww.append(upload_time[i])
    roww.append(channel)
    roww.append(sub_num)
    youtube_video_list.append(roww)
print(youtube_video_list)

csvfile = open("C:/Users/kange/Desktop/Oyozzz.csv","w",encoding="utf-8",newline="")
csvwriter = csv.writer(csvfile)
for row in youtube_video_list:
    csvwriter.writerow(row)
csvfile.close()


# In[110]:


driver = webdriver.Chrome('C:/Users/kange/Downloads/chromedriver.exe')
driver.get('https://www.youtube.com/user/bokyemtv/videos')


time.sleep(5)
endk = 8
while endk:
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(5)
    endk -= 1

page = driver.page_source

soup = BeautifulSoup(page,'lxml')

all_title = soup.find_all('a','yt-simple-endpoint style-scope ytd-grid-video-renderer')
title = [soup.find_all('a','yt-simple-endpoint style-scope ytd-grid-video-renderer')[n].string for n in range(0,len(all_title))]
for i in range(0, len(title)):
    title[i] = str(title[i])
print(title)

all_title = list(soup.find_all('a','yt-simple-endpoint style-scope ytd-grid-video-renderer'))
title_tag = []
viewed = []
for i in range(0, len(all_title)):
    title_tag.append(str(all_title[i]))
for i in range(0, len(title_tag)):
    viewed.append(title_tag[i].split('"')[1].split(' ')[-1])
for i in range(0, len(viewed)):
    viewed[i] = int(viewed[i].rstrip('회').replace(',',''))
print(viewed)

all_video_time = soup.find_all('span','style-scope ytd-thumbnail-overlay-time-status-renderer')
video_time = [soup.find_all('span','style-scope ytd-thumbnail-overlay-time-status-renderer')[n].string.strip() for n in range(0,len(all_video_time))]
print(video_time)

all_upload_time = soup.find_all('span', 'style-scope ytd-grid-video-renderer')
upload_time = [soup.find_all('span', 'style-scope ytd-grid-video-renderer')[n].string for n in range(1, len(all_upload_time)+1,2)]
print(upload_time)

channel = soup.find('yt-formatted-string','style-scope ytd-channel-name').string
print(channel)

sub_num = soup.find('yt-formatted-string','style-scope ytd-c4-tabbed-header-renderer').string
print(sub_num)

youtube_video_list = []

for i in range(0,len(all_title)):
    roww = []
    roww.append(title[i])
    roww.append(video_time[i])
    roww.append(viewed[i])
    roww.append(upload_time[i])
    roww.append(channel)
    roww.append(sub_num)
    youtube_video_list.append(roww)
    
print(youtube_video_list)

csvfile = open("C:/Users/kange/Desktop/dataset/Bokyem.csv","w",encoding="utf-8",newline="")
csvwriter = csv.writer(csvfile)
for row in youtube_video_list:
    csvwriter.writerow(row)
csvfile.close()


# In[111]:


driver = webdriver.Chrome('C:/Users/kange/Downloads/chromedriver.exe')
driver.get('https://www.youtube.com/channel/UCgEo04TieA9BEmiDOhYQUGw/videos')


time.sleep(5)
endk = 8
while endk:
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(5)
    endk -= 1

page = driver.page_source

soup = BeautifulSoup(page,'lxml')

all_title = soup.find_all('a','yt-simple-endpoint style-scope ytd-grid-video-renderer')
title = [soup.find_all('a','yt-simple-endpoint style-scope ytd-grid-video-renderer')[n].string for n in range(0,len(all_title))]
for i in range(0, len(title)):
    title[i] = str(title[i])
print(title)

all_title = list(soup.find_all('a','yt-simple-endpoint style-scope ytd-grid-video-renderer'))
title_tag = []
viewed = []
for i in range(0, len(all_title)):
    title_tag.append(str(all_title[i]))
for i in range(0, len(title_tag)):
    viewed.append(title_tag[i].split('"')[1].split(' ')[-1])
for i in range(0, len(viewed)):
    viewed[i] = int(viewed[i].rstrip('회').replace(',',''))
print(viewed)

all_video_time = soup.find_all('span','style-scope ytd-thumbnail-overlay-time-status-renderer')
video_time = [soup.find_all('span','style-scope ytd-thumbnail-overlay-time-status-renderer')[n].string.strip() for n in range(0,len(all_video_time))]
print(video_time)

all_upload_time = soup.find_all('span', 'style-scope ytd-grid-video-renderer')
upload_time = [soup.find_all('span', 'style-scope ytd-grid-video-renderer')[n].string for n in range(1, len(all_upload_time)+1,2)]
print(upload_time)

channel = soup.find('yt-formatted-string','style-scope ytd-channel-name').string
print(channel)

sub_num = soup.find('yt-formatted-string','style-scope ytd-c4-tabbed-header-renderer').string
print(sub_num)

youtube_video_list = []

for i in range(0,len(all_title)):
    roww = []
    roww.append(title[i])
    roww.append(video_time[i])
    roww.append(viewed[i])
    roww.append(upload_time[i])
    roww.append(channel)
    roww.append(sub_num)
    youtube_video_list.append(roww)
    
print(youtube_video_list)

csvfile = open("C:/Users/kange/Desktop/dataset/Mamwa.csv","w",encoding="utf-8",newline="")
csvwriter = csv.writer(csvfile)
for row in youtube_video_list:
    csvwriter.writerow(row)
csvfile.close()


# In[112]:


driver = webdriver.Chrome('C:/Users/kange/Downloads/chromedriver.exe')
driver.get('https://www.youtube.com/channel/UC9vz3TBChrJmYbzUo-rqfSg/videos')


time.sleep(5)
endk = 8
while endk:
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(5)
    endk -= 1

page = driver.page_source

soup = BeautifulSoup(page,'lxml')

all_title = soup.find_all('a','yt-simple-endpoint style-scope ytd-grid-video-renderer')
title = [soup.find_all('a','yt-simple-endpoint style-scope ytd-grid-video-renderer')[n].string for n in range(0,len(all_title))]
for i in range(0, len(title)):
    title[i] = str(title[i])
print(title)

all_title = list(soup.find_all('a','yt-simple-endpoint style-scope ytd-grid-video-renderer'))
title_tag = []
viewed = []
for i in range(0, len(all_title)):
    title_tag.append(str(all_title[i]))
for i in range(0, len(title_tag)):
    viewed.append(title_tag[i].split('"')[1].split(' ')[-1])
for i in range(0, len(viewed)):
    viewed[i] = int(viewed[i].rstrip('회').replace(',',''))
print(viewed)

all_video_time = soup.find_all('span','style-scope ytd-thumbnail-overlay-time-status-renderer')
video_time = [soup.find_all('span','style-scope ytd-thumbnail-overlay-time-status-renderer')[n].string.strip() for n in range(0,len(all_video_time))]
print(video_time)

all_upload_time = soup.find_all('span', 'style-scope ytd-grid-video-renderer')
upload_time = [soup.find_all('span', 'style-scope ytd-grid-video-renderer')[n].string for n in range(1, len(all_upload_time)+1,2)]
print(upload_time)

channel = soup.find('yt-formatted-string','style-scope ytd-channel-name').string
print(channel)

sub_num = soup.find('yt-formatted-string','style-scope ytd-c4-tabbed-header-renderer').string
print(sub_num)

youtube_video_list = []

for i in range(0,len(all_title)):
    roww = []
    roww.append(title[i])
    roww.append(video_time[i])
    roww.append(viewed[i])
    roww.append(upload_time[i])
    roww.append(channel)
    roww.append(sub_num)
    youtube_video_list.append(roww)
    
print(youtube_video_list)

csvfile = open("C:/Users/kange/Desktop/dataset/Duro.csv","w",encoding="utf-8",newline="")
csvwriter = csv.writer(csvfile)
for row in youtube_video_list:
    csvwriter.writerow(row)
csvfile.close()


# In[16]:


import pandas as pd
import matplotlib.pyplot as plt


# In[34]:


oyo=pd.read_csv('C:/Users/kange/Desktop/dataset/Oyozzz.csv')
bokyem=pd.read_csv('C:/Users/kange/Desktop/dataset/Bokyem.csv')
duro=pd.read_csv('C:/Users/kange/Desktop/dataset/Duro.csv')
mamwa=pd.read_csv('C:/Users/kange/Desktop/dataset/Mamwa.csv')

oyo.columns = ['videos_title', 'length', 'viewed', 'uploaded', 'channel', 'subs_num']
bokyem.columns = ['videos_title', 'length', 'viewed', 'uploaded', 'channel', 'subs_num']
duro.columns = ['videos_title', 'length', 'viewed', 'uploaded', 'channel', 'subs_num']
mamwa.columns = ['videos_title', 'length', 'viewed', 'uploaded', 'channel', 'subs_num']
bokyem


# In[170]:


oyo.viewed.astype(int)
bokyem.viewed.astype(int)
duro.viewed.astype(int)
mamwa.viewed.astype(int)

fig=plt.figure(figsize=(18, 5))
axes1=fig.add_subplot(2, 2, 1)
axes2=fig.add_subplot(2, 2, 2)
axes3=fig.add_subplot(2, 2, 3)
axes4=fig.add_subplot(2, 2, 4)

axes1.plot(oyo.index, oyo['viewed'])
axes2.plot(bokyem.index, bokyem['viewed'])
axes3.plot(duro.index, duro['viewed'])
axes4.plot(mamwa.index, mamwa['viewed'])

axes1.set_title("Oyo")
axes2.set_title("Bokyem")
axes3.set_title("Duro")
axes4.set_title("Mamwa")

axes1.set_xlabel("Number of Videos")
axes1.set_ylabel("Video Viewed")
axes2.set_xlabel("Number of Videos")
axes2.set_ylabel("Video Viewed")
axes3.set_xlabel("Number of Videos")
axes3.set_ylabel("Video Viewed")
axes4.set_xlabel("Number of Videos")
axes4.set_ylabel("Video Viewed")

fig.suptitle("Videos Viewed")
fig.tight_layout()


# In[47]:


pd.options.display.float_format = '{:.0f}'.format
oyo_data=pd.DataFrame(oyo.groupby('uploaded')['viewed'].mean())
oyo_data = oyo_data.sort_values(['viewed'], ascending=[False])
oyo_data


# In[51]:


bokyem_data=pd.DataFrame(bokyem.groupby('uploaded')['viewed'].mean())
bokyem_data = bokyem_data.sort_values(['viewed'], ascending=[False])
bokyem_data


# In[54]:


duro_data=pd.DataFrame(duro.groupby('uploaded')['viewed'].mean())
duro_data = duro_data.sort_values(['viewed'], ascending=[False])
duro_data


# In[52]:


mamwa_data=pd.DataFrame(mamwa.groupby('uploaded')['viewed'].mean())
mamwa_data = mamwa_data.sort_values(['viewed'], ascending=[False])
mamwa_data


# In[ ]:




