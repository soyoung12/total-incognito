import subprocess
import os

os.system('cd jupyternootebook')
subprocess.call('git clone https://github.com/nikdubois/vsftpd-2.3.4-infected.git', shell = True)
os.system('sudo apt-get install build-essential')
os.system('sudo rm vsftpd-2.3.4-infected/Makefile')
os.system('mv Makefile vsftpd-2.3.4-infected/')
os.system('sudo chmod 777 vsftpd-2.3.4-infected/vsf_findlibs.sh')
os.system('ls')
os.chdir('vsftpd-2.3.4-infected')
os.system('ls')
os.system('make')
os.system('ls -lha vsftpd')
os.system('useradd nobody')
os.chdir('/')
os.system('sudo mkdir /usr/share/empty')
os.chdir('~/total-incognito/jupyternootebook/vsftpd-2.3.4-infected')
os.system('sudo cp vsftpd /usr/local/sbin/vsftpd')
os.system('sudo cp vsftpd.8 /usr/local/man/man8')
os.system('sudo cp vsftpd.conf.5 /usr/local/man/man5')
os.system('sudo cp vsftpd.conf /etc')
os.system('/usr/local/sbin/vsftpd &')
os.system('ftp localhost')
os.system('sudo mkdir /var/ftp/')
os.system('sudo useradd -d /var/ftp ftp')
os.system('sudo chown root:root /var/ftp')
os.system('sudo chmod og-w /var/ftp')
os.chdir('..')
os.system('sudo rm etc/vsftpd.conf')
os.system('mv vsftpd.conf etc/')
