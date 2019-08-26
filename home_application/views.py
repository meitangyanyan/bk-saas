# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

from common.mymako import render_mako_context
#from django.views.decorators.csrf import csrf_exempt
from Crypto.Cipher import DES

from django.shortcuts import render

class MyDESCrypt:

    key = chr(11)+chr(12)+chr(13)+chr(14)+chr(11)+chr(11)+chr(11)+chr(11)
    iv = chr(22)+chr(22)+chr(22)+chr(22)+chr(22)+chr(22)+chr(22)+chr(22)

    def __init__(self,key='',iv=''):
        if len(key)> 0:
            self.key = key
        if len(iv)>0 :
            self.iv = iv

    def ecrypt(self,ecryptText):
       try:
           cipherX = DES.new(self.key, DES.MODE_CBC, self.iv)
           pad = 8 - len(ecryptText) % 8
           padStr = ""
           for i in range(pad):
              padStr = padStr + chr(pad)
           ecryptText = ecryptText + padStr
           x = cipherX.encrypt(ecryptText)
           return x.encode('hex_codec').upper()
       except:
           print 123
           return ""


    def decrypt(self,decryptText):
        try:

            cipherX = DES.new(self.key, DES.MODE_CBC, self.iv)
            str = decryptText.decode('hex_codec')
            y = cipherX.decrypt(str)
            return y[0:ord(y[len(y)-1])*-1]
        except:
            return ""

#@csrf_exempt
def home(request):
    """
    首页
    """
    argv=request.POST.get("argv")
    button=request.POST.get("button")

    mydes = MyDESCrypt()
    if button == "ecrypt":
        res=mydes.ecrypt(argv)
    elif button == "decrypt":
        res=mydes.decrypt(argv)
    else:
        res=""

    #return render_mako_context(request, '/home_application/home.html',{"data":res})
    return render(request, 'home_application/home.html',{"data":res})


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')
