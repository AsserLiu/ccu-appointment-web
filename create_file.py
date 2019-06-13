import time
import datetime
import os

def create_file():
    local = time.localtime()
    if(time.asctime(local).find('Sun') != -1):
        path_chinese_tue = 'list/chinese-TUE.csv'
        path_chinese_thu = 'list/chinese-THU.csv'
        path_family_tue = 'list/family-TUE.csv'
        path_family_thu = 'list/family-THU.csv'

        path_chinese_next_tue = 'list/chinese-next_TUE.csv'
        path_chinese_next_thu = 'list/chinese-next_THU.csv'
        path_family_next_tue = 'list/family-next_TUE.csv'
        path_family_next_thu = 'list/family-next_THU.csv'
        try:
            os.remove(path_chinese_tue)
            os.remove(path_chinese_thu)
            os.remove(path_family_tue)
            os.remove(path_family_thu)
        except OSError as e:
            print(e)
        else:
            print("File is deleted successfully")
        try:
            os.rename(path_chinese_next_tue,path_chinese_tue)
            os.rename(path_chinese_next_thu,path_chinese_thu)
            os.rename(path_family_next_tue,path_family_tue)
            os.rename(path_family_next_thu,path_family_thu)
        except OSError as e:
            print(e)
        else:
            print("File is rename successfully")

        open(path_chinese_next_tue,'w',newline = '\n')
        open(path_chinese_next_thu,'w',newline = '\n')
        open(path_family_next_tue,'w',newline = '\n')
        open(path_family_next_thu,'w',newline = '\n')
