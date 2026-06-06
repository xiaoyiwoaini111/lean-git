import requests
import json

#配置区

BASE_URL ="https://www.nowcoder.com/courses"

#替换你登陆后的Token

Heads ={
    "Content-Tyoe": "application/json",
    "Authorization":"Bearer Your_Token_HERE"
}



#测试用例函数

def test_create_pet_success():

    
  BASE_URL=f"{BASE_URL}/pets"

payload ={
  "name" :"旺财",
  "type" :"狗",
  "bread":"金毛",
  "size_desc":"中型犬，性格温顺",
  "is_commen":True,
}