from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel,\
    QPushButton, QLineEdit, QMenuBar, QStatusBar
from PyQt5.QtCore import *
import requests
import json
import 出牌
from 登录界面 import Ui_Form
from 用户界面 import Ui_Dialog
from 初始界面 import Ui_Dialog6
from 排行榜 import Ui_Dialog2
from 历史战绩 import Ui_Dialog3
from 注册界面 import Ui_Dialog4
from 对战界面 import Ui_Dialog5
from 历史战绩详情 import Ui_Dialog7
global token,id
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()#初始界面窗体
    widget4=QtWidgets.QWidget()#对战界面窗体
    widget0 = QMainWindow()
    f = QMainWindow()
    ui5=Ui_Dialog4()#注册界面类
    ui5.setupUi(widget4)
    ui = Ui_Dialog6()#初始界面类
    ui.setupUi(widget)
    def csjm_enter_dljm():#初始界面进登录界面
        widget0.show()
        widget.hide()
    ui.pushButton.clicked.connect(lambda: csjm_enter_dljm())
    def csjm_enter_zcjm():#初始界面进注册界面
        widget4.show()
        widget.hide()
    ui.pushButton_2.clicked.connect(lambda:csjm_enter_zcjm())
    def zcjm_enter_yhjm():#注册界面进用户界面
        url='http://api.revth.com/auth/register2'
        form_data={
            "username":ui5.lineEdit.text(),
            "password":ui5.lineEdit_2.text(),
            "student_number":ui5.lineEdit_3.text(),
            "student_password":ui5.lineEdit_4.text()
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(url=url, headers=headers, data=json.dumps(form_data), verify=False)
        print(response.text)
        res = response.json()
        if res['status']== 0:
           widget1.show()
           widget4.hide()
    ui5.pushButton.clicked.connect(lambda:zcjm_enter_yhjm())
    def zcjm_back_dljm():#注册界面回登录界面
        widget.show()
        widget4.hide()
    ui5.pushButton_2.clicked.connect(lambda:zcjm_back_dljm())
    ui2 = Ui_Form()#登录界面类
    ui2.setupUi(widget0)#登录界面窗体
    widget1 = QtWidgets.QWidget()
    c = QMainWindow()
    ui1 = Ui_Dialog()#用户界面类
    ui1.setupUi(widget1)#用户界面窗体
    def dljm_enter_yhjm():#登录界面进用户界面
        global n,k
        url = 'http://api.revth.com/auth/login'
        form_data = {
            "username": ui2.lineEdit.text(),
            "password": ui2.lineEdit_2.text()
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(url=url, headers=headers, data=json.dumps(form_data), verify=False)
        print(response.text)
        x = response.json()
        m = x['status']
        if (m == 0):
            n=x['data']['token']
            k=x['data']['user_id']
            print(n)
            print(k)
            widget1.show()
            widget4.hide()
    ui2.pushButton.clicked.connect(lambda: dljm_enter_yhjm())
    def dljm_back_csjm():#登录界面回初始界面
            widget.show()
            widget0.hide()
    ui2.pushButton_2.clicked.connect(lambda:dljm_back_csjm())

    widget2=QtWidgets.QWidget()#排行榜窗体
    widget3=QtWidgets.QWidget()#历史纪录窗体
    widget5=QtWidgets.QWidget()#对战界面窗体
    widget7=QtWidgets.QWidget()#战绩详情窗体
    ui3=Ui_Dialog2()#排行榜类
    ui4=Ui_Dialog3()#历史纪录类
    ui6=Ui_Dialog5()#对战界面类
    ui8=Ui_Dialog7()#战绩详情类
    ui4.setupUi(widget3)
    ui3.setupUi(widget2)
    ui6.setupUi(widget5)
    ui8.setupUi(widget7)
    def yhjm_enter_phb():#用户界面进排行榜
        widget2.show()
        widget1.hide()
        url= 'http://api.revth.com/rank'
        res = requests.get(url)
        info = res.json()
        print('排行榜:')
        count = 1
        for i in info:
            print('排名:', count, i['player_id'], i['score'], i['name'])
            count += 1

    def phb_back_yhjm():#排行榜回用户界面
        widget1.show()
        widget2.hide()
    ui3.pushButton.clicked.connect(lambda:phb_back_yhjm())
    ui1.pushButton.clicked.connect(lambda:yhjm_enter_phb())
    def yhjm_enter_lszj():#用户界面进历史纪录
        widget3.show()
        widget1.hide()
        url = "http://api.revth.com/history?"
        headers = {'x-auth-token': n}

        response = requests.get(url=url, headers=headers, verify=False)
        info=response.json()
        print(info)

    def lszj_back_yhjm():#历史纪录回用户界面
        widget1.show()
        widget3.hide()
    def lszj_enter_zjxq():#历史战绩进战绩详情
        widget7.show()
        widget3.hide()
        url='http://api.revth.com:50000/history/51'
        headers={'x-auth-token': n}
        response = requests.get(url=url, headers=headers, verify=False)
        info = response.json()
        print(info)
    def zjxq_back_lszj():#战绩详情返回历史战绩
        widget3.show()
        widget7.hide()
    ui8.pushButton_2.clicked.connect(lambda:zjxq_back_lszj())
    ui4.pushButton.clicked.connect(lambda:lszj_enter_zjxq())
    ui4.pushButton_2.clicked.connect(lambda:lszj_back_yhjm())
    ui1.pushButton_2.clicked.connect(lambda:yhjm_enter_lszj())
    def yhjm_enter_dzjm():#用户界面进对战界面
        widget5.show()
        widget1.hide()
    ui1.pushButton_3.clicked.connect(lambda:yhjm_enter_dzjm())
    def yhjm_back_dljm():#用户界面回登录界面（注销）
        widget0.show()
        widget1.hide()
    ui1.pushButton_4.clicked.connect(lambda:yhjm_back_dljm())

    ui6.pushButton_2.clicked.connect(lambda:dzjm_fp())
    def dzjm_fp():#对战界面发牌功能
        global cards
        url = 'http://api.revth.com/game/open'
        headers = {'x-auth-token': n}
        res = requests.post(url, headers=headers)
        info = res.json()
        print('开启战局')
        id = info['data']['id']
        print(id)
        cards = info['data']['card']
        print('当前手牌:', cards)

    ui6.pushButton.clicked.connect(lambda:dzjm_cp())
    def dzjm_cp():#对战界面出牌功能
        url= 'http://api.revth.com/game/submit'
        headers = {'x-auth-token': n,
                   "Content-Type": "application/json"
                   }
        data = {
            "id": id,
            "card":出牌.cp(cards)
        }
        print(出牌.cp(cards))
        response = requests.post(url=url, headers=headers, data=json.dumps(data), verify=False)
        print(response.text)

    def dzjm_back_yhjm():#对战界面返回用户界面
        widget1.show()
        widget5.hide()
    ui6.pushButton_3.clicked.connect(lambda:dzjm_back_yhjm())
    widget.show()
    sys.exit(app.exec_())
