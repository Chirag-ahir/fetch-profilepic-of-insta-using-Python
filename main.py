-----------pip install instaloader----------
import instaloader()
data=instaloader.Instaloader()
name=input("enter your profilename:")
data.download_profile(name,profile_pic_only=True)
