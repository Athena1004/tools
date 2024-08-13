import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import csv

account = ''
password = ''

Info = []
  

class Application_login(Frame):
    def __init__(self,master = None):
        super().__init__(master)
        self.master = master
        self.font = ('宋体',12)
        self.pack()
        self.createWidget()

    def createWidget(self):
        #创建标签
        self.lab01 = Label(self,text = '账号: ',font = self.font)
        self.lab02 = Label(self,text = '密码: ',font = self.font)

        self.lab01.grid(row = 0 , column = 0,sticky=NSEW)
        self.lab02.grid(row = 1 , column = 0,sticky=NSEW)

        #创建单行文本框
        self.account = StringVar()
        self.account.set('请输入：管理员/用户')
        self.entry01 = Entry(self,textvariable=self.account,width=50,exportselection=False,font = self.font)
        self.entry01.grid(row=0,column=1,sticky=NSEW)

        self.password = StringVar()
        self.password.set('若是管理员,请输入密码(用户可以直接点击登录)')
        self.entry02 = Entry(self,textvariable=self.password,width=50,exportselection=False,font = self.font)
        self.entry02.grid(row=1,column=1,sticky=NSEW)

        #创建功能按钮
        self.btn01 = Button(self,text = '登录',command = self.confirm,bg = 'silver' )
        self.btn01.grid(row=2,column=0,columnspan=2,sticky=NSEW)

    def confirm(self):      
        global account
        global password
        print('用户输入的账户是： ',self.account.get())
        if self.account.get() == '管理员':
            if self.password.get() == '' or self.password.get() == '若是管理员,请输入密码(用户可以直接点击登录)':
                messagebox.showwarning('警告','您是管理员，还未输入密码')
            elif self.password.get() == '123456':
                account = self.account.get()
                password = self.password.get()
                messagebox.showinfo('提示','恭喜您以管理员身份登录成功')
                self.login_destroy()
            else:
                messagebox.showwarning('警告','您以管理员身份登录,密码错误')

        elif self.account.get() == '用户':
            account = self.account.get()
            messagebox.showinfo('提示','恭喜您以用户身份登录')
            self.login_destroy()

        elif self.account.get() == '请输入：管理员/用户' or self.account.get() == '':
            messagebox.showwarning('Board管理系统登录','你还未选择账户是管理员还是用户')
        else:
            messagebox.showwarning('Board管理系统登录','你选择的账户不符合规定')

    def login_destroy(self):
        login_gui.destroy()


class Application(Frame):
    def __init__(self,master = None):
        super().__init__(master)
        self.master = master
        self.font = ("宋体", 12)
        self.student_list = []
        self.grid(row=0,column=0,columnspan=6)
        self.createWidget()
        

    def createWidget(self):
        self.btn01 = Button(self,text = '添 加 板 子 信 息', bg = 'silver', font = ('Arial', 12), command = self.Add_window, width = 20)
        self.btn02 = Button(self,text = '删 除 板 子 信 息', bg = 'silver', font = ('Arial', 12), command = self.Del_window, width = 20)
        self.btn03 = Button(self,text = '修 改 板 子 信 息', bg = 'silver', font = ('Arial', 12), command = self.Mod_window, width = 20)
        self.btn04 = Button(self,text = '查 询 板 子 信 息', bg = 'silver', font = ('Arial', 12), command = self.Ser_window, width = 20)
        self.btn05 = Button(self,text = '显 示 板 子 信 息', bg = 'silver', font = ('Arial', 12), command = self.Show_window, width = 20)
        self.btn06 = Button(self,text = '退 出 板 子 管 理 系 统', bg = 'silver', font = ('Arial', 12), command = self.Exit_window, width = 20)

        self.btn01.grid(row=0,column=0,sticky=NSEW,pady = 15)
        self.btn02.grid(row=1,column=0,sticky=NSEW,pady = 15)
        self.btn03.grid(row=2,column=0,sticky=NSEW,pady = 15)
        self.btn04.grid(row=3,column=0,sticky=NSEW,pady = 15)
        self.btn05.grid(row=4,column=0,sticky=NSEW,pady = 15)
        self.btn06.grid(row=5,column=0,sticky=NSEW,pady = 15)

        self.result = StringVar()
        self.result.set('">>>欢迎使用HPEC Board信息管理系统<<<\n   Edition:  V1.1   \n   @Author: athena\nComplete Time:  2024/06/14"')

        # image = Image.open("main.jpg")  # 替换为你自己的图像文件路径
        # image = image.resize((400,400))  #规定图片大小
        # self.tk_image = ImageTk.PhotoImage(image)
        #self.Show_result = Label(self, bg="white", fg="black", image=self.tk_image,font=self.font, bd='0', anchor='nw', textvariable=self.result,width=100)
        self.Show_result = Label(self, bg="white", fg="black", font=self.font, bd='0', anchor='nw', textvariable=self.result,width=100)
        self.Show_result.grid(row=0,column=1,rowspan=6,sticky=NSEW)
        

    def Add_window(self):
        print('打开窗口: 添加Board信息')
        self.add_window = tkinter.Toplevel()
        self.add_window.title('添加Board信息')
        self.add_window.geometry('400x350+520+300')

        #板子ID
        self.ID =StringVar()
        self.lab_ID = Label(self.add_window,text = 'ID（6位）：',font = self.font)
        self.entry_ID = Entry(self.add_window,textvariable=self.ID,width=30)
        self.lab_ID.grid(row=0,column=0,sticky=E,pady = 15)
        self.entry_ID.grid(row=0,column=1,columnspan=5,sticky=EW)

        #板子型号名字
        self.name =StringVar()
        self.lab_name = Label(self.add_window,text = '板子型号名字 ：',font = self.font)
        self.entry_name = Entry(self.add_window,textvariable=self.name,width=30)
        self.lab_name.grid(row=1,column=0,sticky=E,pady = 15)
        self.entry_name.grid(row=1,column=1,columnspan=5,sticky=EW)

        #使用者
        self.user =StringVar()
        self.lab_user = Label(self.add_window,text = '使用者 ：',font = self.font)
        self.entry_user = Entry(self.add_window,textvariable=self.user,width=30)
        self.lab_user.grid(row=2,column=0,sticky=E,pady = 15)
        self.entry_user.grid(row=2,column=1,columnspan=5,sticky=EW)

        #使用者电话
        self.phone =StringVar()
        self.lab_phone = Label(self.add_window,text = '电话 ：',font = self.font)
        self.entry_phone = Entry(self.add_window,textvariable=self.phone,width=30)
        self.lab_phone.grid(row=5,column=0,sticky=E,pady = 15)
        self.entry_phone.grid(row=5,column=1,columnspan=5,sticky=EW)

        #购于时间
        self._buy_time =StringVar()
        self.lab__buy_time = Label(self.add_window,text = '购于时间：',font = self.font)
        self.entry__buy_time = Entry(self.add_window,textvariable=self._buy_time,width=30)
        self.lab__buy_time.grid(row=4,column=0,sticky=E,pady = 15)
        self.entry__buy_time.grid(row=4,column=1,columnspan=5,sticky=EW)
        #确认按钮
        self.add_confirm = Button(self.add_window,text = '确认', bg = 'silver',font = self.font,command = lambda: self.student_add(self.ID.get(),self.name.get(),self.user.get(),self._buy_time.get(),self.phone.get()))
        self.add_confirm.grid(row=7,column=2,sticky=NSEW)

        #取消按钮
        self.add_concel = Button(self.add_window,text = '取消', bg = 'silver',font = self.font,command = lambda :self.concel(self.add_window))
        self.add_concel.grid(row=7,column=4,sticky=NSEW)

        self.add_window.mainloop()

    def Del_window(self):
        print('打开窗口: 删除Board信息')
        # 窗口创建
        self.del_window = tkinter.Toplevel()
        self.del_window.title('删除Board信息')
        self.del_window.geometry('450x110+550+400')

        #提示标签
        self.lab_del_tip = Label(self.del_window,text = '>>>请先通过"查询Board信息"查询待删除Board的ID<<<',bg = 'white',font=self.font)
        self.lab_del_tip.grid(row=0,column=0,columnspan=5,sticky=NSEW)

        #删除板子ID
        self.del_ID =StringVar()
        self.lab_del_ID = Label(self.del_window,text = 'ID ：',font = self.font)
        self.entry_del_ID = Entry(self.del_window,textvariable=self.del_ID,width=30)
        self.lab_del_ID.grid(row=1,column=0,sticky=E,pady = 15)
        self.entry_del_ID.grid(row=1,column=1,columnspan=4,sticky=EW)

        #确认按钮
        self.del_confirm = Button(self.del_window,text = '确认', bg = 'silver',font = self.font,command = lambda :self.student_del(self.del_ID.get()))
        self.del_confirm.grid(row=2,column=1)

        #取消按钮
        self.del_concel = Button(self.del_window,text = '取消', bg = 'silver',font = self.font,command = lambda :self.concel(self.del_window))
        self.del_concel.grid(row=2,column=2)

        self.del_window.mainloop()

    def Mod_window(self):
        # 窗口创建
        print('打开窗口:修改Board信息')
        self.mod_window = tkinter.Toplevel()
        self.mod_window.title('修改Board信息')
        self.mod_window.geometry('470x110+550+400')

        #提示标签
        self.lab_mod_tip = Label(self.mod_window,text = '>>>请先通过"查询Board信息"查询待修改信息Board的ID<<<',bg = 'white',font=self.font)
        self.lab_mod_tip.grid(row=0,column=0,columnspan=5,sticky=NSEW)

        #查询ID
        self.mod_ID =StringVar()
        self.lab_mod_ID = Label(self.mod_window,text = 'ID ：',font = self.font)
        self.entry_mod_ID = Entry(self.mod_window,textvariable=self.mod_ID,width=30)
        self.lab_mod_ID.grid(row=1,column=0,sticky=E,pady = 15)
        self.entry_mod_ID.grid(row=1,column=1,columnspan=4,sticky=EW)


        #确认按钮
        self.mod_confirm = Button(self.mod_window,text = '确认', bg = 'silver',font = self.font,command = lambda :self.student_mod(self.mod_ID.get()))
        self.mod_confirm.grid(row=2,column=1)

        #取消按钮
        self.mod_concel = Button(self.mod_window,text = '取消', bg = 'silver',font = self.font,command = lambda :self.concel(self.mod_window))
        self.mod_concel.grid(row=2,column=2)


        self.mod_window.mainloop()

    def Ser_window(self):
        # 窗口创建
        print('打开窗口: 查询Board信息')
        self.ser_window = tkinter.Toplevel()
        self.ser_window.title('查询Board信息')
        self.ser_window.geometry('400x400+600+250')
        #提示标签
        self.lab_mod_tip = Label(self.ser_window,text = '>>>输入ID/board name,点击确认后开始查询<<<\n<<当ID和board name同时存在时,仅使用ID查找>>',bg = 'white',font=self.font)
        self.lab_mod_tip.grid(row=6,column=0,columnspan=7,sticky=NSEW)

        #ID
        self.ser_ID =StringVar()
        self.lab_ser_ID = Label(self.ser_window,text = 'ID（6位）：',font = self.font)
        self.entry_ser_ID = Entry(self.ser_window,textvariable=self.ser_ID,width=30)
        self.lab_ser_ID.grid(row=0,column=0,sticky=E,pady = 15)
        self.entry_ser_ID.grid(row=0,column=1,columnspan=5,sticky=EW)

        #板子型号名字
        self.ser_board_name =StringVar()
        self.lab_ser_board_name = Label(self.ser_window,text = '   板子型号名字 ：',font = self.font)
        self.entry_ser_board_name = Entry(self.ser_window,textvariable=self.ser_board_name,width=30)
        self.lab_ser_board_name.grid(row=2,column=0,sticky=E,pady = 15)
        self.entry_ser_board_name.grid(row=2,column=1,columnspan=5,sticky=EW)

        #使用者
        self.ser_user_name =StringVar()
        self.lab_ser_user_name = Label(self.ser_window,text = '   使用者 ：',font = self.font)
        self.entry_ser_user_name = Entry(self.ser_window,textvariable=self.ser_user_name,width=30)
        self.lab_ser_user_name.grid(row=1,column=0,sticky=E,pady = 15)
        self.entry_ser_user_name.grid(row=1,column=1,columnspan=5,sticky=EW)

        #购于时间
        self.ser_buy_time =StringVar()
        self.lab_ser_buy_time = Label(self.ser_window,text = '购于时间：',font = self.font)
        self.entry_ser_buy_time = Entry(self.ser_window,textvariable=self.ser_buy_time,width=30)
        self.lab_ser_buy_time.grid(row=4,column=0,sticky=E,pady = 15)
        self.entry_ser_buy_time.grid(row=4,column=1,columnspan=5,sticky=EW)

        #使用者电话
        self.ser_phone =StringVar()
        self.lab_ser_phone = Label(self.ser_window,text = '  电话 ：',font = self.font)
        self.entry_ser_phone = Entry(self.ser_window,textvariable=self.ser_phone,width=30)
        self.lab_ser_phone.grid(row=5,column=0,sticky=E,pady = 15)
        self.entry_ser_phone.grid(row=5,column=1,columnspan=5,sticky=EW)

        #确认按钮
        self.ser_confirm = Button(self.ser_window,text = '确认', bg = 'silver',font = self.font,command = lambda :self.student_ser(self.ser_ID.get(),self.ser_user_name.get()))
        self.ser_confirm.grid(row=7,column=2,sticky=NSEW)

        #取消按钮
        self.ser_concel = Button(self.ser_window,text = '取消', bg = 'silver',font = self.font,command = lambda :self.concel(self.ser_window))
        self.ser_concel.grid(row=7,column=4,sticky=NSEW)

        self.ser_window.mainloop()

    def Show_window(self):      #用于实现信息的展示
        global Info
        if len(Info) == 0:
            messagebox.showinfo('提示','暂无Board信息')
            self.result.set('>>>>暂无Board信息<<<<')
            return
        if account == '管理员':
            student_content = ("{:<15}".format("ID") +
                        "{:<15}".format("Board Name") +
                        "{:<15}".format("User") +
                        "{:<15}".format("User Phone") +
                        "{:<15}".format("Buy Time") +
                        "\n")

            for i in Info:
                student_content += ("{:<15}".format(i['ID']) +
                        "{:<15}".format(i['Board Name']) +
                        "{:<15}".format(i['User']) +
                        "{:<15}".format(i['User Phone']) +
                        "{:<15}".format(i['Buy Time']) +
                        "\n")
            self.result.set(student_content)
            messagebox.showinfo('提示','显示Board信息成功')
        elif account == '用户':
            messagebox.showinfo('提示','由于您是用户,仅展示一部分Board信息')
            student_content = ("{:<15}".format("ID") +
                               "{:<15}".format("Board Name") +
                               "{:<15}".format("Buy Time") +
                               "\n")

            for i in Info:
                student_content += ("{:<15}".format(i['ID']) +
                                    "{:<15}".format(i['Board Name']) +
                                    "{:<15}".format(i['Buy Time']) +
                                    "{:<15}".format(i['User']) +
                                    "{:<15}".format("User Phone") +
                                    "\n")
            self.result.set(student_content)
            messagebox.showinfo('提示', '显示Board信息成功')

    def Exit_window(self):      #用于实现退出窗口
        answer = messagebox.askyesno('退出HPEC Board管理系统','您确定退出HPECBoard管理系统吗？')
        print('是否退出HPEC Board管理系统：',answer)
        if answer == True:                    #传回的是bool值，不是字符串,所以不用加引号
            messagebox.showinfo('HPEC Board管理系统','欢迎下次使用')
            root.destroy()
        elif answer == False:
            return


    def concel(self,window):#用于关闭窗口
        print('关闭窗口')
        window.destroy()

    def student_add(self,ID,name,user,_buy_time,phone):  #用于添加Board信息
        global Info

        if not self.is_ID(ID):
            self.Tip_Add_ID()
            return

        if not self.is_buy_time(_buy_time):
            self.Tip_Add_buy_time()
            return

        if not self.is_Telephone(phone):
            self.Tip_Add_Telephone()
            return

        for i in Info:
            if i['ID'] == ID:
                self.Tip_Add_ID_Repeat()
                return

        if account == '管理员':
            Info_dict = {'ID': ID, 'Board Name': name, 'User': user
                , 'Buy Time': _buy_time, 'User Phone': phone}
            print('添加的Board信息是:', Info_dict)
            Info.append(Info_dict)
            with open('BoardData.csv','w',encoding='utf-8')as f:
                for item in Info:
                     f.write(str(item)+'\n')
                self.Tip_Add()
                self.add_window.destroy()
                self.Show_window()
        else:
            messagebox.showwarning('警告','您不是管理员,无法添加Board信息')


    def student_del(self,get_ID):  #用于删除Board信息
        global Info
        ID = get_ID
        flag = 0
        if not self.is_ID(ID):
            self.Tip_Add_ID()
            return

        if account == '管理员':
            for i in Info:
                if i['ID'] == ID:
                    Info.remove(i)
                    flag = 1
                    break
            if flag == 1:
                for i in Info:
                    with open('BoardData.csv','w',encoding='utf-8')as f:
                        f.write(str(i)+'\n')
                self.Tip_Del()
                self.Show_window()
            else:
                self.Tip_Del_ID_None()
        else:
            messagebox.showwarning('警告','您不是管理员,无法删除Board信息')


    def student_mod(self,get_ID):  #用于更改Board信息
        global Info
        ID = get_ID
        if not self.is_ID(ID):
            self.Tip_Add_ID()
            return

        if account == '管理员':
            for i in Info:
                if i['ID'] == ID:
                    self.student_del(ID)
                    messagebox.showinfo('提示','要修改的信息已删除,请输入修改后的信息')
                    self.Add_window()
                    break
                else:
                    self.Tip_Del_ID_None()

        else:
            messagebox.showwarning('警告','您不是管理员,无法修改Board信息')


    def student_ser(self,get_ID,get_Name):  #用于查询Board信息
        global Info
        ID = get_ID
        Name = get_Name
        flag = 0
        if ID != '':                
            if not self.is_ID(ID): 
                self.Tip_Add_ID()
                return
            if account == '管理员':
                for i in Info:
                    if i['ID'] == ID:
                        self.ser_ID.set(i['ID'])
                        self.ser_user_name.set(i['User'])
                        self.ser_board_name.set(i['Board Name'])
                        self.ser_buy_time.set(i['Buy Time'])
                        self.ser_phone.set(i['User Phone'])
                        flag = 1
                        break
                if flag == 1:
                    self.Tip_Search()
                else:
                    self.Tip_Search_None()

            elif account == '用户':
                messagebox.showinfo('提示', '由于您是用户，仅展示一部分内容')
                for i in Info:
                    if i['ID'] == ID:
                        self.ser_ID.set(i['ID'])
                        self.ser_user_name.set(i['User'])
                        self.ser_board_name.set(i['Board Name'])
                        self.ser_buy_time.set(i['Buy Time'])
                        flag = 1
                        break
                if flag == 1:
                    self.Tip_Search()
                else:
                    self.Tip_Search_None()

        elif ID == '' and Name != '':       #当没有学号，仅存在名字时
            if account == '管理员':
                for i in Info:
                    if i['Name'] == Name:
                        self.ser_ID.set(i['ID'])
                        self.ser_user_name.set(i['User'])
                        self.ser_board_name.set(i['Board Name'])
                        self.ser_buy_time.set(i['Buy Time'])
                        self.ser_phone.set(i['User Phone'])
                        flag = 1
                if flag == 1:
                    self.Tip_Search()
                else:
                    self.Tip_Search_None()

            elif account == '用户':
                messagebox.showinfo('提示', '由于您是用户，仅展示一部分内容')
                for i in Info:
                    if i['Name'] == Name:
                        self.ser_ID.set(i['ID'])
                        self.ser_user_name.set(i['User'])
                        self.ser_board_name.set(i['Board Name'])
                        self.ser_buy_time.set(i['Buy Time'])
                        flag = 1
                        break
                if flag == 1:
                    self.Tip_Search()
                else:
                    self.Tip_Search_None()


    def is_ID(self,ID):
        return len(ID) == 6 and ID.isdigit()

    def is_buy_time(self,_buy_time):
        return _buy_time.isdigit() and int(_buy_time) > 0

    # 定于一个方法，用于检查电话是否规范
    def is_Telephone(self,phone):
        return len(phone) == 11 and phone.isdigit()

    def Tip_Add(self):
        messagebox.showinfo("提示信息", "添加成功")

    def Tip_Search(self):
        messagebox.showinfo("提示信息", "查询成功")

    def Tip_Del(self):
        messagebox.showinfo("提示信息", "删除成功")

    def Tip_Mod(self):
        messagebox.showinfo("提示信息", "修改成功")

    def Tip_Add_ID_Repeat(self):
        messagebox.showinfo("提示信息", "此ID已经存在，请勿重复添加！")

    def Tip_Del_ID_None(self):
        messagebox.showinfo("提示信息", "此ID不存在，请重新输入！")

    def Tip_Search_None(self):
        messagebox.showinfo("提示信息", "未查询到有关Board信息！")

    def Tip_Add_ID(self):
        messagebox.showinfo("提示信息", "ID格式有误，请重新输入！")

    def Tip_Add_buy_time(self):
        messagebox.showinfo("提示信息", "时间格式有误，请重新输入！")

    def Tip_Add_Telephone(self):
        messagebox.showinfo("提示信息", "电话格式有误，请重新输入！(11位电话号码)")



if __name__ == '__main__':
    try:
        with open('BoardData.csv','r+',encoding='utf-8')as f:  
            list = f.readlines()
            for item in list:
                Info.append(eval(item))     #将字符串利用eval转换为字典，储存进列表中
    except:
        with open('BoardData.csv','w+',encoding='utf-8')as f:   
            pass  

    login_gui = Tk()
    login_gui.title('<<HPEC Board管理系统登录界面>>')
    login_gui.geometry('500x100+500+200')
    
    app_login = Application_login(master = login_gui)
    login_gui.mainloop()

    if account == '管理员' or account == '用户':
        root = Tk()
        root.title('<<<HPEC Board管理系统>>>')
        root.geometry('1050x375+500+200')
        app = Application(master = root)
        root.mainloop()

