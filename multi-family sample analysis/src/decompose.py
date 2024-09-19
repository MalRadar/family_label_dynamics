import os
import subprocess
import time


def decompile(apk, folder):
    '''
    Decompile apk with ApkTool
    '''
    CMD = ['apktool', 'd', '-o', folder, apk]
    print(CMD)
    subprocess.call(CMD)


def sample_decompose(apkpath):
    # apkpath = './malradar-family-euphony/anubisspy/anubisspy-453c829c2b7f504e28b554927f4bc1f2.apk'
    folder = apkpath[:-4]
    decompile(apkpath, folder)


def sample_makefile():
    folder = './malradar-family-euphony/anubisspy/anubisspy-453c829c2b7f504e28b554927f4bc1f2'
    res = folder + '/res'
    for d in os.listdir(res):
        touch_cmd = ['touch', os.path.join(res, d, 'a.txt')]
        subprocess.call(touch_cmd)
        print(touch_cmd)
        time.sleep(1)
        rm_cmd = ['rm', '-rf', os.path.join(res, d, 'a.txt')]
        subprocess.call(rm_cmd)
        print(rm_cmd)

