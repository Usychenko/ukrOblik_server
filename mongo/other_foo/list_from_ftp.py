from ftplib import FTP

ftp = FTP('ftp.itp34.com.ua')

ftp.login('mbus@busov.itp34.com.ua', '621QWas@')

# changing directory
ftp.cwd('/test/')

file_list = ftp.nlst()
for one_file in file_list:
    print(one_file)

ftp.quit()
