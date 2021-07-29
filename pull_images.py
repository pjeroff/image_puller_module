import os
import time
import argparse

from selenium import webdriver

import urllib.request


# Making an input method for user to choose their search terms / keywords

ap = argparse.ArgumentParser()
ap.add_argument("-k", "--keywords", required = True, help = "Input your search keyword(s)...for multiple words use (+) instead of space...i.e. grizzly+bear")
ap.add_argument("-n", "--number", required = False, help = "Specify a number of pictures you'd like to get, default is set to 100")
args = vars(ap.parse_args())

search_query = args["keywords"]
#search_query = "grizzly+bear"

# Setting default limit of images to download, in this case.. it's 100 images, else we take the users desired number
limit = 100
if args["number"] is not None:
    limit = int(args["number"])

#Selenium code to scroll to bottom of the page
link = "https://www.google.com/search?q={}&tbm=isch".format(search_query)

driver = webdriver.Chrome('chromedriver')
driver.get(link)

SCROLL_PAUSE_TIME = 2


# Making a new folder to put our images in before jumping into scroller
# If folder exists already, ask user to delete/rename/remove it first

path2folder = os.getcwd()
secondPath = path2folder+"/"+args["keywords"]

if os.path.exists(secondPath) == False:
    print("Creating directory")
    os.mkdir(args["keywords"])
    os.chdir(args["keywords"])

else:
    print("Folder already exists! Please remove any folders already named {} and run the program again!".format(args["keywords"]))
    driver.quit()
    exit()


#check if we fcked up
print("Attempting to get {} images of our search terms".format(limit))


# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
    #break #insert press load more
        try:
            element = driver.find_elements_by_class_name('mye4qd') #returns list
            element[0].click()
        except:
            break
    last_height = new_height

print("Reached the end of page")


def null_count(l):
    #given a list l, find the number of null
    null_count = 0

    for element in l:
        if element == None:
            null_count += 1

    return null_count


#return a list clickable objects for each individual image
image_links = driver.find_elements_by_class_name('rg_i.Q4LuWd')
total = len(image_links)
total


#use the list of object to search for 'data-src' and 'src' anchors
data_src_links = [image_links[i].get_attribute('data-src') for i in range(total)]
src_links = [image_links[i].get_attribute('src') for i in range(total)]


data_src_null_count = null_count(data_src_links)
data_src_null_count


src_null_count = null_count(src_links)
src_null_count

#Since the "data_src" anchor has less missing, we will use "src" anchor's list to fill in "data_src"

for i,element in enumerate(data_src_links):
    if element == None:
        data_src_links[i] = src_links[i]


#check null count again
"Nulls: {}, Length: {}".format(null_count(data_src_links), len(data_src_links))



# Actual Scraping
image_nmbr_index = 0
#limit = 100

for i,link in enumerate(data_src_links):

    name = args["keywords"]+'{}.jpg'.format(i)

    urllib.request.urlretrieve(link, name)
    image_nmbr_index += 1
    if image_nmbr_index == limit:
        break
    time.sleep(1)


driver.quit()
