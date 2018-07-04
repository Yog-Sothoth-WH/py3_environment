import os
os.system('yum -y groupinstall "Development tools"')
os.system('yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel')

os.system('wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tar.xz && mkdir /usr/local/python3')

os.system('tar -xvJf Python-3.6.2.tar.xz')
os.chdir('Python-3.6.2')

os.system('make && make install')

os.system('ln -s /usr/local/python3/bin/python3 /usr/bin/python3')
os.system('ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3')

os.system('pip3 install --upgrade pip && pip install requests')
