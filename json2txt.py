# Extract jokes from json files to txt file


import json
import os.path

def json2txt(json_path, txt_path):
    json_object = json.load(open(json_path, 'r'))


    # Append to existing txt
    if os.path.isfile(txt_path):
        with open(txt_path, 'a') as f:
            for item in json_object:
                f.write('{}\n\n'.format(item['joke'].encode("utf-8")))
        f.close()
    #  Create new  txt
    else:
        with open(txt_path, 'w') as f:
            for item in json_object:
                f.write('{}\n\n'.format(item['joke'].encode("utf-8")))
        f.close()

#json2txt('/home/oliver/Projects/jokes/jokes/items.json', '/home/oliver/Projects/jokes/jokes/raw_jokes.txt')
json2txt('/home/oliver/Projects/jokes/jokes/items_funny2.json', '/home/oliver/Projects/jokes/jokes/raw_jokes.txt')