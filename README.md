# Simple Web scrapper to fetch 100 images for our ML/DL learning (Fast.ai)

Simple immage puller to fascilitate getting smaller datasets (default 100 images) for our future ML/DL learning (i.e. Fast.ai's 2nd notebook from Fastbook).


## PREREQUISITES:

This code was run in Ubuntu 20.04. For any other OS (like macOS) I'm not sure if commands such as mkdir etc. work, this is only for Linux.

You'll need Chrome and Chromedriver.

NOTE: Download the Chrome and CDriver that are compatible with eachother.

Grab Chromedriver at the following link: https://chromedriver.chromium.org/downloads

Then open the terminal in the folder you downloaded the driver to and run:

```
unzip chromedriver_linux64.zip
chmod +x chromedriver

sudo mv -f chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
```

Then we get Chrome:
```
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt-get update 
sudo apt-get install google-chrome-stable
```
Finally, install Selenium (via terminal):
```
pip3 install selenium
```

## What pull_images.py does:

Every time we run the program it will check if the folder with the search querry exists already (so make sure there is NO folder with your search querry else the program EXITS)...then proceeds to creating a new folder with our keywords and dumps our images into that folder.

## HOW-TO:

Make sure you are in the DIR where pull_images.py is...

To get 100 images of "Grizzly Bear" run in terminal: 

```
python3 pull_images.py -k grizzly+bear
```

-k is for keyword.... and if you want any other search term just type something else, but make sure to use (+) for multiple word search querries..


> example searching for "Deja Vu":
```
python3 pull_images.py -k Deja+Vu
```


Since the default # of images is limited to 100, you can change it to your desired amount by adding the argument -n followed by your desired amount of images (only up to one page worth of the search engine results though):


> In this case, we set it to 300 images
```
python3 pull_images.py -k Deja+Vu -n 300
```


