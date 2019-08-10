from youtube_dl import YoutubeDL
import multiprocessing as mp
#from PyQt4 import QtGui, QtCore
import sys

NAME = 'I_am_folder'                               #set name 

def download_m4a(i_file, dir_name = NAME):
    #print(dir(YoutubeDL))
    opts = {'get-url':True,
            'flat-playlist': True,
            'download': False,
            'format': 'm4a/bestaudio',                  #m4a format
            'outtmpl':f'{dir_name}/%(title)s.%(ext)s',  #directory to save in
            'nooverwrites':True,                        #don't download if same filename exists
            'restrictfilenames':True,                   #no spaces and &&    
            'ignoreerrors':True                        #ignore errors
            }

    a = YoutubeDL(opts).extract_info(i_file)
    print(a)
    '''
    with youtube_dl.YoutubeDL(opts) as ydl:             #call
        .download([i_file])'''



def mp_download():
    playlist = input('playlist: ')
    '''with open('vids.txt') as f:
        mylist = f.readlines()
    mylist = [x[:x.find(';')] for x in mylist]   #stripping from ; til end
    '''
    try:            
        m_proc = mp.Pool()
        m_proc.map(download_m4a, mylist)
    except AttributeError:
        pass           

#cos of multipricessing script sholud run from cmd or just double click
if __name__ == '__main__':
    li = 'https://www.youtube.com/watch?v=Rbm6GXllBiw&list=RDQM3caJcH-zYtk&start_radio=1'
    download_m4a(li)
