# -*- coding: utf-8 -*-
"""
Created on 2020

@author: Maryam Kiani Nezhad
"""

# -*- coding: utf-8 -*-
"""
@author: Maryam
"""
import json
#The program needs to load the file and manage the discography providing the following features:
#search by artist–search by title–search by publication year–search by total tracks

class Discography():## object oriented in python
    
#####################################################   search by artist ##########################################
    """ print all the information about the discs  for the given <artist_name> """  
    
    def search_artist(self,artist_name,disco_name):
        j=len(disco_name['album_list'])
        found=False             ## Initialization
        while j!=0:             ## All the artists found must be printed
            if disco_name['album_list'][j-1]['artist']==artist_name:
                found=True
                return disco_name['album_list'][j-1]
                j=j-1
            else: 
                j=j-1
            if j==0 and found==False:
                found=False
                return "Does not exist!!"
######################################################   read file json ###########################################
        
    def read_file_json(self):
        filename = "discography.JSON"  ## File name received input information
        json_data=open(filename).read()
        
        data=json.loads(json_data)
    
        
        return data

######################################################   search by title ###########################################
    """ print all the information about the discs for the given <title>  """  
    
    def search_title(self,title_name,disco_name):
        j=len(disco_name['album_list'])
        found=False             ## Initialization
        while j!=0:             ## All the artists found must be printed
            if disco_name['album_list'][j-1]['title']==title_name:
                found=True
                print(disco_name['album_list'][j-1])
                j=j-1
            else: 
                j=j-1
            if j==0 and found==False:
                found=False
                return "Does not exist!!"
                
            
####################################################   search by year ##############################################
    """ print all the information about the discs for the given <year>  """

    def search_year(self,year,disco_name):
        j=len(disco_name['album_list'])
        found=False             ## Initialization
        while j!=0:             ## All the artists found must be printed
            if disco_name['album_list'][j-1]['publication_year']==year:
                found=True
                print(disco_name['album_list'][j-1])
                j=j-1
            else: 
                j=j-1
            try:
                j==0 and found==False
            except:
                print ("Does not exist!!")
        
###################################################   search by total_tracks #######################################
    """print all the information about the discs having the given <total_tracks>  """
    
    def search_total_tracks(self,total_tracks,disco_name):
        j=len(disco_name['album_list'])
        found=False            ## Initialization
        while j!=0:            ## All the artists found must be printed
            if disco_name['album_list'][j-1]['total_tracks']==total_tracks:
                found=True
                print(disco_name['album_list'][j-1])
                j=j-1
            else: 
                j=j-1
            if j==0 and found==False:
                print("Does not exist")
                break
        
 #############################################   print All ########################################################        
        
    def print_all(self,disco_name):
        print('album_list :','\n')
        i=len(disco_name['album_list'])
        j=0
        while i!=0:
            print('artist',[j],':',disco_name['album_list'][j]['artist'])
            print('     title:',':',disco_name['album_list'][j]['title'])
            print('     publication_year',':',disco_name['album_list'][j]['publication_year'])    
            print('     total_tracks',':',disco_name['album_list'][j]['total_tracks'],'\n')    

            j=j+1
            i=i-1 
        print("######################################")    
        print('discography_owner :', "Maryam Kiani Nezhad")
######################################################## design ####################################################
    """  Primary design function for user selection  """
    
    def design(self):
        print("1.Search_by_artist",'\n')
        print("2.Search_by_title",'\n')
        print("3.Search_by_publication_year",'\n')
        print("4.Search_by_total_tracks",'\n')
        print("5.Print_all",'\n')
        
######################################################### main #####################################################
    
if __name__ =='__main__':
    """ Create a class object Discography """
    dis=Discography()
    disco=dis.read_file_json()##read json file 
#    disco = eval(disco)
    while True:
        dis.design()## Function of basic design
        operation=input("Enter The Nubmer of operation : ")
        list_operation=operation.split(' ') 
        if list_operation[0]=='1':################### search by artist ##########################################
            artist=input("Enter The artist name : ")
            print(dis.search_artist(artist,disco))
            decide=input("The main menu?[y]N : ")
            if decide=='n' or decide=='N':
              print("Goodbye!!")
              break  
        elif list_operation[0]=='2':################### Search by title ##########################################
            title=input("Enter The title : ")
            dis.search_title(title,disco)
            decide=input("The main menu?[y]N : ")
            if decide=='n' or decide=='N':
              print("Goodbye!!")
              break  
        elif list_operation[0]=='3':################### Search_by_publication_year ###############################
            year=input("Enter The year : ")
            year=int(year)
            dis.search_year(year,disco)
            decide=input("The main menu?[y]N : ")
            if decide=='n' or decide=='N':
              print("Goodbye!!")
              break  
        elif list_operation[0]=='4':################### Search_by_total_tracks ###################################
            tracks=input("Enter The total tracks : ")
            tracks=int(tracks)
            dis.search_total_tracks(tracks,disco)
            decide=input("The main menu?[y]N : ")
            if decide=='n' or decide=='N':
              print("Goodbye!!")
              break  
       
        elif list_operation[0]=='5':################### Print_all #################################################
            dis.print_all(disco)
            decide=input("The main menu?[y]N : ")
            if decide=='n' or decide=='N':
              print("Goodbye!!")
              break 
      

