from math import log10, sqrt
import matplotlib.pyplot as plt
import numpy as np
import os

#Resolutions
res1 = '337x600'
res2 = '1012x1800'
res3 = '1687x3000'

#Methods
methods = ['ANDROID', 'APP-MAC', 'APP-WIN', 'IPHONE', 'WEB-IPAD', 'WEB-MAC', 'WEB-WIN']
QFs = ['QF-50', 'QF-60', 'QF-70', 'QF-80', 'QF-90', 'QF-100']

android_keys = ['android_50', 'android_60', 'android_70', 'android_80', 'android_90', 'android_100', 'android']
android = {}

app_mac_keys = ['app_mac_50', 'app_mac_60', 'app_mac_70', 'app_mac_80', 'app_mac_90', 'app_mac_100', 'app_mac']
app_mac = {}

app_win_keys = ['app_win_50', 'app_win_60', 'app_win_70', 'app_win_80', 'app_win_90', 'app_win_100', 'app_win']
app_win = {}

iphone_keys = ['iphone_50', 'iphone_60', 'iphone_70', 'iphone_80', 'iphone_90', 'iphone_100', 'iphone']
iphone = {}

web_ipad_keys = ['web_ipad_50', 'web_ipad_60', 'web_ipad_70', 'web_ipad_80', 'web_ipad_90', 'web_ipad_100', 'web_ipad']
web_ipad = {}

web_mac_keys = ['web_mac_50', 'web_mac_60', 'web_mac_70', 'web_mac_80', 'web_mac_90', 'web_mac_100', 'web_mac']
web_mac = {}

web_win_keys = ['web_win_50', 'web_win_60', 'web_win_70', 'web_win_80', 'web_win_90', 'web_win_100', 'web_win']
web_win = {}

SHADE = []

#Load images from SHADE
def LoadImages(elem, method, qf):
    arr = []

    for i in range(150):
        image = plt.imread('SHADE/' + method + '/' + qf + '/' + elem[i], 1)
        arr.append(image)

    return arr

#Calculate MSE
def MSE(img1, img2):
    mse = np.mean((img1 - img2) ** 2)
    return mse

#Calculate PSNR
def PSNR(mse):
    max_pixel = 255.0

    if mse != 0:
        p = 20 * log10(max_pixel / sqrt(mse))
        return p
    else:
        return np.Nan

#Compute MSE and PSNR
def Compute_MSE_PSNR(method1, method2, mod):
    if mod == 'MSE':
        mse = []

        for i in range(150):
            m = MSE(method1[i], method2[i])
            mse.insert(i,m)

        return mse
    else:
        psnr = []

        for i in range(150):
            m = MSE(method1[i], method2[i])
            p = PSNR(m)

            psnr.insert(i,p)

        #Removing NaN values from the list
        psnr = [x for x in psnr if str(x) != 'nan']
        return psnr

def main():

    #Loading all the Dataset
    for method in methods:
        i = 0
        for qf in QFs:
            img = []
            if method == 'ANDROID':
                img = LoadImages(os.listdir('SHADE/' + method + '/' + qf), 'ANDROID', qf)
                android[android_keys[i]] = img
            elif method == 'APP-MAC':
                img = LoadImages(os.listdir('SHADE/' + method + '/' + qf), 'APP-MAC', qf)
                app_mac[app_mac_keys[i]] = img
            elif method == 'APP-WIN':
                img = LoadImages(os.listdir('SHADE/' + method + '/' + qf), 'APP-WIN', qf)
                app_win[app_win_keys[i]] = img
            elif method == 'IPHONE':
                img = LoadImages(os.listdir('SHADE/' + method + '/' + qf), 'IPHONE', qf)
                iphone[iphone_keys[i]] = img
            elif method == 'WEB-IPAD':
                img = LoadImages(os.listdir('SHADE/' + method + '/' + qf), 'WEB-IPAD', qf)
                web_ipad[web_ipad_keys[i]] = img
            elif method == 'WEB-MAC':
                img = LoadImages(os.listdir('SHADE/' + method + '/' + qf), 'WEB-MAC', qf)
                web_mac[web_mac_keys[i]] = img
            elif method == 'WEB-WIN':
                img = LoadImages(os.listdir('SHADE/' + method + '/' + qf), 'WEB-WIN', qf)
                web_win[web_win_keys[i]] = img

            i = i + 1
    
    android['android'] = android['android_50'] + android['android_60'] + android['android_70'] + android['android_80'] + android['android_90'] + android['android_100']
    app_mac['app_mac'] = app_mac['app_mac_50'] + app_mac['app_mac_60'] + app_mac['app_mac_70'] + app_mac['app_mac_80'] + app_mac['app_mac_90'] + app_mac['app_mac_100']
    app_win['app_win'] = app_win['app_win_50'] + app_win['app_win_60'] + app_win['app_win_70'] + app_win['app_win_80'] + app_win['app_win_90'] + app_win['app_win_100']
    iphone['iphone'] = iphone['iphone_50'] + iphone['iphone_60'] + iphone['iphone_70'] + iphone['iphone_80'] + iphone['iphone_90'] + iphone['iphone_100']
    web_ipad['web_ipad'] = web_ipad['web_ipad_50'] + web_ipad['web_ipad_60'] + web_ipad['web_ipad_70'] + web_ipad['web_ipad_80'] + web_ipad['web_ipad_90'] + web_ipad['web_ipad_100']
    web_mac['web_mac'] = web_mac['web_mac_50'] + web_mac['web_mac_60'] + web_mac['web_mac_70'] + web_mac['web_mac_80'] + web_mac['web_mac_90'] + web_mac['web_mac_100']
    web_win['web_win'] = web_win['web_win_50'] + web_win['web_win_60'] + web_win['web_win_70'] + web_win['web_win_80'] + web_win['web_win_90'] + web_win['web_win_100']

    SHADE = android['android'] + app_mac['app_mac'] + app_win['app_win'] + iphone['iphone'] + web_ipad['web_ipad'] + web_mac['web_mac'] + web_win['web_win']

    #Computing MSE and PSNR
    combinations = [((app_mac['app_mac'], web_ipad['web_ipad'], ('APP MAC', 'WEB IPAD')), (app_mac['app_mac'], web_mac['web_mac'], ('APP MAC', 'WEB MAC')), (web_ipad['web_ipad'], app_win['app_win'], ('WEB IPAD', 'APP WIN')), (web_mac['web_mac'], app_win['app_win'], ('WEB MAC', 'APP WIN'))), ((web_ipad['web_ipad'], web_win['web_win'], ('WEB IPAD', 'WEB WIN')), (web_mac['web_mac'], web_win['web_win'], ('WEB MAC', 'WEB WIN'))), ((app_mac['app_mac'], web_win['web_win'], ('APP MAC', 'WEB WIN')), (app_win['app_win'], web_win['web_win'], ('APP WIN', 'WEB WIN')))]
    for combination in combinations:
        

if __name__ == '__main__':
    main()