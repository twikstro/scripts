scripts
=======

itermcolor.py  
- Set iTerm2 tab color by ssh server role/category
- customize your roles inside the script  
  
use like this in .ssh/config:  
Host myhost  
    HostName myhost  
    PermitLocalCommand yes  
    LocalCommand python ~/path/to/itermcolor.py role 
