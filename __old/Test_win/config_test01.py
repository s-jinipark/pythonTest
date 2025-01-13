import configparser
import json

parser = configparser.ConfigParser()
parser.read("sample_config.txt")

option_values = parser.get("config", "a_list")
option_value_list = json.loads(option_values)

print(option_value_list)

#https://www.kite.com/python/answers/how-to-parse-a-configuration-file-into-a-list-in-python


lst = json.loads(parser.get("Bar","files_to_check"))
print(lst)

#https://stackoverflow.com/questions/335695/lists-in-configparser
