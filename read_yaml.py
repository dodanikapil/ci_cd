#!/usr/bin/python3
import re
import yaml
#import func

def reading_yaml(func):
    def print_msg(*args, **kwargs):
        print ("I am decorator")
        return func(*args, **kwargs)
    return print_msg

#@reading_yaml
def load_config(yaml_file):
    with open(yaml_file,"r") as yml:
        #config = yaml.safe_load(yml)
        #config = yaml.load_all(yml, Loader = yaml.SafeLoader)
        config = yaml.load_all(yml,Loader=yaml.SafeLoader)
        return config

print (__name__)

if __name__ == "__main__":
    yaml_file = "xrun.yaml"
    data = load_config(yaml_file)

    for f in data:
        print (f)
    if f:
        #print (data)
        #print ("\n"*2,data.get(tool))
        #print (data[0]["dic_check"]["name"][0])
        print (f["tool"], f["xlm_version"], ' '.join(f["build_switches"]))
        #print ("\n"*2+"KD"*5, data[1])
       # print (data["Xcelium_version"])
       # print (data.get("Xcelium_version"))
       # for i in data.get("build_switches"):
       #     print (i)
       # print (data.get("str_check"))
       # print (data.get("str_check2"))
    
