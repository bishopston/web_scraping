from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome(executable_path=r'C:\selenium\\chromedriver.exe')

url = 'https://www.youtube.com/c/JohnWatsonRooney/videos?view=0&sort=p&flow=grid'

driver.get(url)

videos = driver.find_elements_by_class_name('style-scope ytd-grid-video-renderer')

video_list=[]

for video in videos:
    title = video.find_element_by_xpath('.//*[@id="video-title"]')
    views = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[1]').text
    when = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[2]').text
    vid_item = {
        'title': title,
        'views': views,
        'posted': when,
    }

    video_list.append(vid_item)

df = pd.DataFrame(video_list)
print(df)

# driver.quit() 

