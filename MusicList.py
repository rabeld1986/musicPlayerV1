'''
Created on Sep 9, 2020

@author: rabel
'''
import os

from pygame import mixer,time

from threading import Thread

from random import randint



class music_list(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        self.track_list = dict()
        
    def add_song(self,file: str,path: str):
        ###results from searching our selected path
        self.results = []
        
        #provided file name
        self.file = file + ".mp3"
        
        #provided path
        self.path = path
        #key creation for our hash table
        self.key = self.get_name().replace(" ", "")
        
        for root, dir, files in os.walk(self.path):
            if self.file in files:
                self.results.append(os.path.join(root, self.file))
                

            else:
                return False
        #inserting element into our hash table
        if self.key not in self.track_list:
            self.track_list[self.key] = []
        
        self.track_list[self.key].append(self.path+"\\"+self.file)

    def get_key(self):
        return self.get_name().replace(" ", "")
    def printL(self):
        print(self.track_list[self.get_key()][0])
    def run(self):
        self.p = False
        if self.track_list != None :
            mixer.init()
            mixer.music.load(self.track_list[self.get_key()][0])
            mixer.music.set_volume(0.7)
            mixer.music.play()
            
            while mixer.music.get_busy():
                time.Clock().tick(10)
                secondsToSleep = randint(1, 5)

                time.delay(secondsToSleep)
                self.p = True
                
                global stop_thread
                
                if stop_thread == True:
                    break
    
                
    def volume_up(self,up: float):
        
        mixer.music.set_volume(up)
    
    def volume_down(self,down: float):
        mixer.init()
        mixer.music.set_volume(down)  
    
    def stop(self):
            mixer.music.pause()
              
    def get_name(self):
        for i in range(len(self.file)):
            if self.file[i] == "-":
                self.song_name = self.file[0:i-1]
        return self.song_name
    def get_artist(self):
        start = 0
        endP = 0
        for i in range(len(self.file)):
            if self.file[i] == "-":
                start = i+1
            elif self.file[i] == ".":
                endP = i
            self.artist = self.file[start:endP]
        return self.artist



