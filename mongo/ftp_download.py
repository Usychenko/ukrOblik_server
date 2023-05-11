import ftplib
from convert import csv_to_json

def ftp_download(path_for_save, path_to_dir, url, user, pwd):
    #path = 'test2/'
    #filename = 'MPC140_2023_04_25_13.csv'
    count = 0
    ftp = ftplib.FTP(url)
    ftp.login(user,pwd)
    ftp.cwd(path_to_dir)
    arr_of_file = ftp.nlst()
    for file_name in arr_of_file:
        #print(file_name)
        path_to_file = path_for_save + file_name
        if file_name != '.' and file_name != '..':
            if('.log' not in file_name):
                f = open(path_to_file, 'wb')
                ftp.retrbinary("RETR " + file_name, f.write)
                f.close()
                arr_of_file[count] = path_to_file
            ftp.delete(file_name)
                     #   print(path_to_file)
        count += 1
    ftp.quit()
    print ('############')
    #for i in arr_of_file:
    #    print(i)
    return arr_of_file

def all_csv_to_json(dir_for_save, arr_of_file):
    for csv_file in arr_of_file:
        #json_name('../some_json/' + )
        if csv_file != '.' and csv_file != '..':
            json_name = csv_file.replace('.csv', '.json')
            json_name = json_name.replace('/some_file/', '/some_json/')
#            print(json_name)
            csv_to_json(csv_file, json_name)
    return arr_of_file

#ftp_download('/test2/','ftp.itp34.com.ua','mbus@busov.itp34.com.ua','621QWas@')
