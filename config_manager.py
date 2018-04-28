import re
import os.path
directory=os.path.dirname(os.path.abspath(__file__))
filename=os.path.join(directory, "rover_config.txt")
print filename
config={}
try:
    text=open(filename,'r')
    lines=text.readlines()
    text.close()
    for line in lines:
        if line.startswith('#'):
            continue
        name=re.findall('.*?(\S+)\s*?=',line)
        if len(name)!=1:
            continue
        name=name[0]
        value=re.findall('.*=\s?(\S+)',line)
        if len(value)!=1:
            continue
        value=value[0]
        if value.isdigit():
            value=int(value)
        config[name]=value
except IOError:
    #default backup values
    print "rover_config.txt not found, using default values"
    config['config_test']='N'
    config['tile_size']=100
    config['collision_efficiency']=.5
    config['scale']=10
if config['config_test']=='Y':
    for name in config.keys():
        print name +'='+ str(config[name])
