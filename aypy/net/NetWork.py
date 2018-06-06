# -*- encoding:utf-8 -*-
"""
  网络统一接口模块
"""

import logging
import requests
import time
import ast

from requests.packages.urllib3.exceptions import ReadTimeoutError


def get(url, params=None, headers=None, retry=3, **kwargs):
    """
    :param url: 请求base url
    :param params: url params参数
    :param headers: http head头信息
    :param retry: 重试次数，默认retry=3
    :param kwargs: 透传给requests.get，可设置ua等，超时等参数
    """
    req_count = 0
    while req_count < retry:
        # 重试retry次
        try:
            resp = requests.get(url=url, params=params, headers=headers, **kwargs)
            if resp.status_code == 200 or resp.status_code == 206:
                # 如果200，206返回，否则继续走重试
                return resp
        except ReadTimeoutError:
            # 超时直接重试就行，不打日志
            pass
        except Exception as e:
            logging.exception(e)
        req_count += 1
        time.sleep(0.5)
        continue
    return None


def post(url, params=None, headers=None, retry=3, **kwargs):
    """
    :param url: 请求base url
    :param params: url params参数
    :param headers: http head头信息
    :param retry: 重试次数，默认retry=3
    :param kwargs: 透传给requests.get，可设置ua等，超时等参数
    """
    req_count = 0
    while req_count < retry:
        try:
            resp = requests.post(url=url, params=params, headers=headers, **kwargs)
            return resp
        except Exception as e:
            logging.exception(e)
            req_count += 1
            time.sleep(0.5)
            continue
    return None