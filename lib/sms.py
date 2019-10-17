import random

import requests
from django.http import JsonResponse

from common import errors
from swiper import config
from lib.http import render_json

def gen_vcode(size=4):
    start = 10 ** (size - 1)
    end = 10 ** size - 1
    vcode = random.randint(start, end)
    return str(vcode)


# 发送短信验证码
def send_vcode(phone):
    params = config.YZX_PARAMS.copy()
    params['param'] = gen_vcode()
    params['mobile'] = phone

    response = requests.post(config.YZX_URL, json=params)
    if response.status_code == 200:
        json_resposne = response.json()
        if json_resposne['code'] == '000000':
            return 'ok'
        else:
            return json_resposne['msg']
    else:
        return render_json(data='短信验证码发送失败', code=errors.SMS_FAILED)
