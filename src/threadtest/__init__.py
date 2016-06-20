#coding:utf-8
'''
os/sys 鍖呭惈鍩烘湰杩涚▼绠＄悊鍑芥暟
subprocess Python鍩烘湰搴撲腑澶氳繘绋嬬浉鍏虫ā鍧�
signal   Python鍩烘湰搴撲腑淇″彿鐩稿叧妯″潡
threading Python鍩烘湰搴撲腑绾跨▼鐩稿叧妯″潡


鍑芥暟
popen   鐢熸垚鏂扮殑杩涚▼
system  鐩存帴鐢熸垚瀛楃涓叉墍浠ｈ〃鐨勮繘绋� (鎵撳紑鍙︿竴涓▼搴�)
abort/exit   缁堟杩涚▼
exec瀹舵棌   鍦ㄧ幇鏈夎繘绋嬫崲杩涗笅鐢熸垚鏂扮殑杩涚▼
'''

import os
# for key in os.environ.keys():
#     print(key ,'\t',os.environ[key])


# print(os.system('dir'))


import subprocess

# pingP = subprocess.Popen(args='ping - n 4 www.sina.com.cn',shell=True)
# pingP.wait()
# print(pingP.stdout)
# print(pingP.pid)
# print(pingP.returncode)

# sts = os.system('cmd')

# p = subprocess.Popen('cmd',shell = True)

try:
    returncode = subprocess.call('cmd',shell = True)
    if returncode < 0:
        print('treminated by signal')
    else:
        print(returncode)
        print('return with code')
except OSError,e:
    print('OSError ')
    



