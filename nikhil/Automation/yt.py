from pytube import YouTube

link = input("Enter the video link to download")
yt = YouTube(f"{link}")
print("Title:",  yt.title)
yd = yt.streams.get_highest_resolution()
download_path = input("Please Enter the path to save the File")
yd.download(f"{download_path}")