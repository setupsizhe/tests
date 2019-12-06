# coding:utf-8
import os
import requests
import sys
import yaml
import common.get_token as a



# from common.readexcel import ExcelUti

def send_requests(s, testdata):


    '''封装requests请求'''
    method = testdata["method"]
    url = testdata["url"]
    # url后面的params参数
    Flag=testdata['Flag']
    print(Flag)
    try:
        params = testdata["params"]
    except:
        params = None
    # 请求头部headers
    try:
        if Flag==1:
            headers = a.get_token()
        else:
            headers=None

        # print("请求头部：%s" % headers)
    except:
        headers = None
    # post请求body类型


    test_nub = testdata['ID']
    print("*******正在执行用例：-----  %s  ----**********" % test_nub)
    print("请求方式：%s, 请求url:%s" % (method, url))
    print("请求params：%s" % params)


    try:
        bodydata = testdata["body"]
    except:
        bodydata = {}

    # 判断传data数据还是json
    if type == "data":
        body = bodydata
    elif type == "json":
        body = json.dumps(bodydata)
    else:
        body = bodydata
    if method == "post": print("请求body类型为：post" )

    verify = False
    res = {}   # 接受返回数据

    try:
        r = s.request(method=method,
                      url=url,
                      params=params,
                      headers=headers,
                      verify=verify
                       )
        print("页面返回信息：%s" % r.content.decode("utf-8"))
        res['id'] = testdata['ID']
        res['rowNum'] = testdata['rowNum']


        res["statuscode"] = str(r.status_code)  # 状态码转成str
        res["text"] = r.content.decode("utf-8")
        res["times"] = str(r.elapsed.total_seconds())
        # 接口请求时间转str
        if res["statuscode"] != "200":
            res["error"] = res["text"]
            print(res["text"])
        else:
            res["error"] = ""
        res["msg"] = ""
        if testdata["checkpoint"] in res["text"]:
            res["result"] = "pass"
            print("用例测试结果:   %s---->%s" % (test_nub, res["result"])+'\n\n')
        else:
            res["result"] = "fail"
        return res
    except Exception as msg:
        res["msg"] = str(msg)
        return res


if __name__ == "__main__":
    cur_path=os.path.dirname(os.path.realpath(__file__))
    yaml_path=os.path.join(cur_path,'D://unit//jiekou//config//canshu')
    datas = open(yaml_path,'r',encoding='UTF-8')
    testdatas = yaml.load(datas, Loader=yaml.FullLoader)
    data =testdatas
    s = requests.session()
    res = send_requests(s, data[1])
    # print(data)
    # print(data[0]['params'])



