# Data-Science-Tutorials

## CentOS Installation
1. Install Python2.7
2. Install Setuptools, Pip, Virtual Enviroment
3. Install ipython, matplotlib, scipy, pandas, numpy, scikit-learn, nltk

## Windows Installation



### Centos 6.5+ 

    $ which python 
    /usr/local/bin/python

    $ python -V
    Python 2.7.3

    $ ls -ltr /usr/local/bin/pyth*
    lrwxrwxrwx 1 root root      24 Jan 30  2013 /usr/local/bin/python -> /usr/local/bin/python2.7
    -rwxr-xr-x 1 root root 6162289 Sep  3 00:59 /usr/local/bin/python2.7
    -rwxr-xr-x 1 root root    1624 Sep  3 01:00 /usr/local/bin/python2.7-config


So yum will use '/usr/bin/python' which is 2.6

    $ /usr/bin/python -V
    Python 2.6.6

"python" will give you python 2.7.

"python2.7" will give you python 2.7.

"easy_install" and "easy_install-2.7" will easy install for python 2.7. While separate files, they both seem to install into /usr/local/lib/python2.7/site-packages/

    $ ls -ltr /usr/local/bin | grep easy_
    -rwxr-xr-x   1 root root     340 Jan 30  2013 easy_install-2.7
    -rwxr-xr-x   1 root root     332 Jan 30  2013 easy_install


**note the dash before the 2.7**

The easy_install's in /usr/bin are for 2.6

    $ ls -ltr /usr/bin/easy*
    -rwxr-xr-x. 1 root root 331 Nov 11  2010 /usr/bin/easy_install-2.6
    -rwxr-xr-x. 1 root root 323 Nov 11  2010 /usr/bin/easy_install

###I would recommend python 2.7 on all local machines
I suspect  everyone is already ok?. To check:

    [root@apu etc]# python -V
    Python 2.7.3

Instructions for python 2.7 install on windows 7, ubuntu, mac will be on another page.

Because of centos 6.3 on the cluster machines, we need both 2.6 and 2.7 to coexist there.
hopefully only there.

### Centos relies on python 2.6 for yum
if you install python 2.7 in any way other than the following you will destroy the system and make yum inoperable

zlib failure message may be from internal python scripts doing uncompression and they may be referring to python module files, rather than looking at links directly. Not sure.

I believe only the x86_64 zlib is needed. i.e. you don't need 32-bit and 64-bit, but just follow these instructions. They worked on apu.0xdata.loc (192.168.1.160) on 9/28/2012

### to check centos version

    [root@apu etc]# cat /etc/redhat-release
    CentOS release 6.3 (Final)

(also okay for centos 6.4)

###How to install Python 2.7.6 on CentOS 6.3 (6.2 and 6.4 okay too, probably others)

stolen from Daniel Eriksson. Thanks Daniel!

http://toomuchdata.com/2012/06/25/how-to-install-python-2-7-3-on-centos-6-2/

(modified a little)

CentOS 6.2 ships with Python 2.6.6 and depends on that specific version. Be careful not to replace it or bad things will happen. If you need access to a newer version of Python you must compile it yourself and install it side-by-side with the system version.

Here are the steps necessary to install Python 2.7.6. 
Execute all the commands below as root. Either log in as root temporarily or use sudo.

###Install development tools

In order to compile Python you must first install the development tools:

    yum groupinstall "Development tools"

You also need a few extra libs installed before compiling Python or else you will run into problems later when trying to install various packages:

    yum install zlib-devel
    yum install bzip2-devel
    yum install openssl-devel
    yum install ncurses-devel
    yum install sqlite-devel

###Download, compile and install Python

The --no-check-certificate is optional

    cd /opt
    wget --no-check-certificate https://www.python.org/ftp/python/2.7.6/Python-2.7.6.tar.xz
    tar xf Python-2.7.6.tar.xz
    cd Python-2.7.6
    ./configure --prefix=/usr/local
    make && make altinstall

It is important to use altinstall instead of install, otherwise you will end up with two different versions of Python in the filesystem both named python.

(Depending on your version of wget, you may need to add the --no-check-certificate option to the wget command line.)

After running the commands above your newly installed Python 2.7.6 interpreter will be available as /usr/local/bin/python2.7 and the system version of Python 2.6.6 will be available as /usr/bin/python and /usr/bin/python2.6.

Check with:

    root@node-01/opt/Python-2.7.6 ] ls -ltr /usr/bin/python*

    lrwxrwxrwx 1 root root    6 Nov 16  2002 /usr/bin/python2 -> python
    -rwxr-xr-x 1 root root 1418 Jul 10  2013 /usr/bin/python2.6-config
    -rwxr-xr-x 2 root root 4864 Jul 10  2013 /usr/bin/python2.6
    -rwxr-xr-x 2 root root 4864 Jul 10  2013 /usr/bin/python
    lrwxrwxrwx 1 root root   16 Oct 24 15:39 /usr/bin/python-config -> python2.6-config

    root@node-01/opt/Python-2.7.6 ] ls -ltr /usr/local/bin/python*
    -rwxr-xr-x 1 root root 6214533 Mar 19 22:46 /usr/local/bin/python2.7
    -rwxr-xr-x 1 root root    1674 Mar 19 22:46 /usr/local/bin/python2.7-config
 
If things don't look right, you might need to create a symbolic link in /usr/local/bin

    cd /usr/local/bin
    ls -ltr python*

WARNING: don't do this before checking the $PATH for root. if it has /usr/local/bin before /usr/bin, it will see python2.7 first
i.e.

    root@openstack h2o]# echo $PATH
    /usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin

If you add this link, do a "which python" for the user and for root. If root is pointing to /usr/local/bin/python, remove the link you just added, and figure out something else.

    ln -s /usr/local/bin/python2.7 /usr/local/bin/python

final check:


    sudo sh
    root@node-01~ ] which python
    /usr/bin/python
    root@node-01/home/0xdiag ] python
    Python 2.6.6 (r266:84292, Jul 10 2013, 22:48:45) 
    [GCC 4.4.7 20120313 (Red Hat 4.4.7-3)] on linux2
    root@node-01~ ] exit
 
    sudo - user
    user@lg1:~ ] which python
    /usr/local/bin/python
    user@lg1:~ ] python
    Python 2.7.6 (default, Mar 19 2014, 22:45:29) 
    [GCC 4.4.7 20120313 (Red Hat 4.4.7-4)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.


###Installing and configuring distribute (setuptools)

After installing Python 2.7.6 you also need to install distribute (setuptools) so you can easily install new packages in the right location.

 
    wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py
    sudo /usr/local/bin/python2.7 ez_setup.py
    sudo /usr/local/bin/easy_install-2.7 pip
 

The commands above will generate the script /usr/local/bin/easy_install-2.7. Use this script to install packages for your new Python version. You should be able to use "easy_install" if "which easy_install" points to the correct 2.7 versions

I'm jumping between two different machine installs here, sorry about that, pay attention to /usr/local/bin vs /usr/bin
 
    0xdiag@lg1$ which pip
    /usr/local/bin/pip

    $ which easy_install
    /usr/local/bin/easy_install

    $ ls -ltr /usr/local/bin/easy_install*
    -rwxr-xr-x 1 root root 340 Jan 30  2013 /usr/local/bin/easy_install-2.7
    -rwxr-xr-x 1 root root 332 Jan 30  2013 /usr/local/bin/easy_install

    sudo /usr/local/bin/easy_install-2.7 requests
    sudo /usr/local/bin/easy_install-2.7 psutil
    sudo /usr/local/bin/easy_install-2.7 paramiko

    (for normal user, easy_install should work too, if your PATH gets /usr/local/bin first)


I had to rename pip and easy_install in /user/local/bin and create links. The existing ones were 2.6 variants. Check first though if pip and easy_install act right after install. On this system they did:

    [root@openstack kevin]# cd /usr/local/bin
    [root@openstack bin]# ls -ltr pip*
    -rwxr-xr-x 1 root root 213 Oct 20 22:55 pip2.7
    -rwxr-xr-x 1 root root 213 Oct 20 22:55 pip2
    -rwxr-xr-x 1 root root 296 Oct 20 22:58 pip3.4
    -rwxr-xr-x 1 root root 290 Oct 20 22:58 pip
    -rwxr-xr-x 1 root root 292 Oct 20 22:58 pip3

I think if root uses pip or easy_install it will install into python 2.7, not 2.6 
maybe that doesn't matter
 
On this system, it's because /usr/local/bin comes before /usr/bin

    [root@openstack bin]# which pip
    /usr/local/bin/pip
    [root@openstack bin]# which easy_install
    /usr/local/bin/easy_install

    [root@openstack bin]# pip --version
    pip 1.5.6 from /usr/local/lib/python2.7/site-packages (python 2.7)
    [root@openstack bin]# easy_install --version
    setuptools 7.0
    [root@openstack bin]# pip2.7 --version
    pip 1.5.6 from /usr/local/lib/python2.7/site-packages (python 2.7)
    [root@openstack bin]# 


Fixing the $PATH would make that correct, since the 2.6 gets resolved correctly with /usr/bin

    [root@openstack bin]# /usr/bin/pip --version
    pip 1.3.1 from /usr/lib/python2.6/site-packages (python 2.6)
 
    root@openstack bin]# /usr/bin/easy_install --version
    distribute 0.6.10


In any case, if this doesn't cause a problem due to $PATH in root or users, you can do this:

    cd /usr/local/bin
    mv pip pip2.6
    mv easy_install easy_install-2.6
    ln -s pip2.7 pip
    ln -s easy_install-2.7 easy_install

result in /usr/local/bin

    -rwxr-xr-x 1 root root 6214533 Mar 19 22:46 python2.7
    -rwxr-xr-x 1 root root    1674 Mar 19 22:46 python2.7-config
    lrwxrwxrwx 1 root root      24 Mar 19 22:51 python -> /usr/local/bin/python2.7
    -rwxr-xr-x 1 root root     323 Mar 19 23:18 easy_install-2.6
    -rwxr-xr-x 1 root root     331 Mar 19 23:18 easy_install-2.7
    -rwxr-xr-x 1 root root     296 Mar 19 23:22 pip2.7
    -rwxr-xr-x 1 root root     290 Mar 19 23:22 pip2.6
    -rwxr-xr-x 1 root root     292 Mar 19 23:22 pip2
    lrwxrwxrwx 1 root root      16 Mar 19 23:29 easy_install -> easy_install-2.7
 
result in /usr/bin

     ls -ltr /usr/bin/pip
    -rwxr-xr-x 1 root root 281 Oct 24 15:38 /usr/bin/pip
 
     ls -ltr /usr/bin/easy_install
    -rwxr-xr-x 1 root root 323 Nov 11  2010 /usr/bin/easy_install


### Ipython Notebook
```
yum install virtualenv

virtualenv test-ipython

cd ./test-ipython

source bin/activate

pip install pyzmq tornado notebook

ipython notebook
```
Head to your server running on 127.0.0.1:8888
