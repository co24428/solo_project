import insta_img
import urllib.request

myimg = insta_img.get_img_url()
num = 0
for img in myimg:
    urllib.request.urlretrieve(img,'save_insta_'+str(num)+'.png')
    num += 1
print('저장성공')