# coding=utf-8
import unittest
import time
from BeautifulReport import BeautifulReport
import os
from tomorrow3 import threads
curpath = os.path.dirname(os.path.realpath(__file__))
report_path = os.path.join(curpath, "report")
if not os.path.exists(report_path):
    os.mkdir(report_path)
case_path = os.path.join(curpath, "case")

def add_case(casepath=case_path, rule="test*.py"):
    '''加载所有的测试用例'''
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(casepath,
                                                  pattern=rule)

    return discover
@threads(3)
def run_case(test_suit):
    result = BeautifulReport(test_suit)
    result.report(filename='report.html', description='接口测试报告', log_path='report')

if __name__ == "__main__":
    # 用例集合
    cases = add_case()
    for i in cases:
        run_case(i)
        print(i)

