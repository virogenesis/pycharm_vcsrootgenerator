### PYCharm VCS Root Updater ###

I had a problem with adding my vcs roots in .env folder for pycharm: http://stackoverflow.com/questions/26998410/registering-vcs-root-in-pycharm-from-within-virtual-environment  
So I wrote a simple script I can execute from within the Project folder where the .env is located that adds to .idea/vcs.xml file all the VCS roots for my editable submodules.  



### Usage ###

* pip install git+https://github.com/virogenesis/pycharm_vcsrootgenerator.git
* Navigate to your project root folder, the one with .idea folder in it.  
* python update_roots.py  

Done.
