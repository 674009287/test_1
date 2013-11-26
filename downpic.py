import os,urllib2,urllib
path='/home/losa/github_neunn/'
file_name='downpic.jpg'
file_name= os.path.join(path,file_name)
url="http://www.neunn.com/neunn.jpg"
urllib.urlretrieve(url , file_name)
