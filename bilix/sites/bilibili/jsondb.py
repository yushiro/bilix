import json
import os

def check_and_save_key(key,value):
    # 检查文件是否存在，如果不存在则创建一个空的 JSON 文件
    if not os.path.isfile("data123.json"):
        with open("data123.json", "w", encoding='utf-8') as json_file:
            json.dump({}, json_file)
    with open("data123.json", "r+", encoding='utf-8') as json_file:
        data = json.load(json_file)
        if key in data:
            # print(f"键存在{key}")
            return data[key]["isDownloaded"]
        else:
            # print(f"键不存在，将其保存到 JSON 文件中{value}")
            data[key] = value
            json_file.seek(0)
            json.dump(data, json_file, ensure_ascii=False)
            return False


def update_key(key, value):
    # 检查文件是否存在，如果不存在则创建一个空的 JSON 文件
    if not os.path.isfile("data123.json"):
        with open("data123.json", "w", encoding='utf-8') as json_file:
            json.dump({}, json_file)
    with open("data123.json", "r+", encoding='utf-8') as json_file:
        data = json.load(json_file)
        if key in data:
            # print(f"键存在，更新其值{value}")
            data[key] = value
            json_file.seek(0)
            json.dump(data, json_file, ensure_ascii=False)

def get_key(key):
    # # 检查文件是否存在，如果不存在则创建一个空的 JSON 文件
    # if not os.path.isfile("data123.json"):
    #     with open("data123.json", "w", encoding='utf-8') as json_file:
    #         json.dump({}, json_file)
    with open("data123.json", "r", encoding='utf-8') as json_file:
        data = json.load(json_file)
        # print(f"键存在，获取其值{key}=>{data}")
        if key in data:
            return data[key]
        else:
            return None