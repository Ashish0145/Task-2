from pytube import YouTube

while (True):
    ip = input("Press 1 if you have Video Link or Press 2 if you have video ID : ")
    if (ip == "1"):
        link = input("Please Enter Video Link : ")
        ys = YouTube(link)
        break
    elif (ip == "2"):
        VIDEO_ID = input("Please Enter Video ID : ")
        ys = YouTube("www.youtube.com/watch?v=" + VIDEO_ID)
        break


print("Title: ",ys.title)

VIDEO = ys.streams.get_highest_resolution()


#Starting download
print("Downloading...")
VIDEO.download()
print("Download completed!!")