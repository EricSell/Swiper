import re

from django.http import JsonResponse

# Create your views here.

# 获取短信验证码
from common import errors
from lib.sms import send_vcode
from lib.http import render_json


def get_vcode(request):
    # 接收手机号码
    phone = request.POST.get('phone')
    if phone is None:
        return render_json(data='手机号码为空', code=errors.PHONE_EMPTY)
    if not re.match(r'1[356789]\d{9}', phone):
        return render_json(data='非法手机号', code=errors.PHONE_ILLEGAL)

    # 发送短信验证码
    send_vcode(phone)

    return render_json()

#
# # 通过验证码登录,注册
# def(request):
#     pass
#
#
# # 获取个人资料
# def(request):
#     pass
#
#
# # 通过验证码登录,注册
# def(request):
#     pass
#
#
# # 通过验证码登录,注册
# def(request):
#     pass
