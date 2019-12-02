# coding:utf-8
import unittest
import ddt
import requests
import os

from jiekou.common import request
import yaml
import sys
cur_path=os.path.dirname(os.path.realpath(__file__))
yaml_path=os.path.join(cur_path,'D://unit//jiekou//config//canshu')
print(cur_path)
datas=open(yaml_path,'r',encoding='UTF-8')
testdata=yaml.load(datas,Loader=yaml.FullLoader)
# print(testdata)



@ddt.ddt
class Test_api(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()

    @ddt.data(*testdata)
    def test_api(self, data):

        res = request.send_requests(self.s, data)
        check = data["checkpoint"]
        # print("检查点->：%s"%check)
        res_text = res["text"]
        # print("返回实际结果->：%s"%res_text)
        # for i in res:
        #     print(res['times'])
        self.assertTrue(check in res_text)


if __name__ == "__main__":
    unittest.main()

