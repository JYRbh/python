#!/usr/bin/python
#-*-coding:utf-8-*-

import threading, time
#print "my name is fanxunshan!"

#主体思想： 对象——>进行抽象——>类——>实例化——>对象——>线程化——>赋予了独立的处理能力——>自动化

profession = {
    "1":{"name":u"战士","attackInit":40,"defenseInit":40},
    "2":{"name":u"法师","attackInit":50,"defenseInit":30},
              }

class people():
    equip_head = 0
    equip_hand = 0
    equip_leg = 0
    HP = 100
    def __init__(self,username,password):
        pass

flowPrinting = False

class role():
    equip_head = 0
    equip_hand = 0
    equip_leg = 0
    HP = 100
    LV = 1
    
    #appearance默认有4种样貌1,2,3,4
    def __init__(self,username,password,professionNum,name=u"无名大侠"):
        self.username = username
        self.password = password
        self.name = name
        self.professionNum = professionNum
        self.professionName = profession[str(professionNum)]["name"]
        self.attack = profession[str(professionNum)]["attackInit"]
        self.defense = profession[str(professionNum)]["defenseInit"]

        #command中1代表攻击;2代表持续攻击至死
        self.command = ""
        #target代表目标
        self.target = None
        
        self.thread_commandHandler = threading.Thread(target=self.CommandHandler, args=())
        self.thread_commandHandler.start()

    def OnAttack(self, obj):
        #global flowPrinting
        #if (flowPrinting==False):
        #    flowPrinting = True
        #    print("Start to attack "+obj.name)
        #    flowPrinting = False
        print("Start to attack "+obj.name)
           
        if obj.HP <= 0:
            obj.SayDeath()
        else:
            obj.HP = obj.HP - (self.attack - obj.defense)
            if obj.HP <= 0:
                obj.SayDeath()
        obj.ShowAttributes()

    def ShowAttributes(self):
        global flowPrinting
        if (flowPrinting==False):
            flowPrinting = True
            print(u"该用户的信息如下:")
            print(u"用户名称:"+self.name)
            print(u"角色名称:"+self.professionName)
            print(u"角色攻击力:"+str(self.attack))
            print(u"角色防御力:"+str(self.defense))
            print(u"角色等级:"+str(self.LV))
            print(u"角色血量:"+str(self.HP))
            flowPrinting = False

    def SayHello(self):
        print("my name is "+self.username)

    def SayDeath(self):
        print("my name is "+self.username+", I'm death!")

    def execCommand(self, command, target):
        self.command = command
        self.target = target

    def CommandInit(self):
        self.command = 0
        self.target = None
    
    def CommandHandler(self):
        while True:
            if (self.command==""):
                pass
            elif (self.command==1):
                print ("Recv command "+str(self.command))
                self.OnAttack(self.target)
                self.CommandInit()
            elif (self.command==2):
                print ("Recv command "+str(self.command))
                while (self.target.HP > 0):
                    self.OnAttack(self.target)
                    time.sleep(0.2)
                self.CommandInit()
            else:
                pass
            time.sleep(0.01)
    
if __name__ == "__main__":
    ###########基本对象的实现##########
    '''
    #print "my name is fanxunshan!"
    fan = role("fanxunshan","123456","1",u"范训山")
    shan = role("vankey","123456","2",u"路人甲")
    fan.ShowAttributes()

    for i in range(11):
        print("================")
        fan.OnAttack(shan)
        shan.ShowAttributes()
    '''
    ###########有自我处理能力的对象##########
    fan = role("fanxunshan","123456","1",u"范")
    shan = role("vankey","123456","2",u"山")

    #场景1：A攻击B
    #fan.execCommand(1,shan)

    #场景2：A持续攻击B
    #fan.execCommand(2,shan)

    #场景3：A、B互相攻击
    fan.execCommand(2,shan)
    time.sleep(0.2)
    shan.execCommand(2,fan)








    
