import re
config={}
text=open('rover_config.txt','r')
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
if config('config_test')=='Y':
    for name in config.keys():
        print name + str(config(name))
