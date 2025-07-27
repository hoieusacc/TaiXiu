import random as r
from colorama import Fore
import time
import os

def menu():
    print(Fore.YELLOW+'1.Chơi')
    print(Fore.YELLOW+'2.Đăng xuất')
    print(Fore.YELLOW+'3.Xem số dư')
    print(Fore.YELLOW+'4.Nạp tiền vào tài khoản')

islogin = False
isreg = False
svusn = ''
svpass = ''

while True:
    print(Fore.LIGHTGREEN_EX+'**********************************')
    print(Fore.YELLOW+'Vui lòng đăng nhập')
    print(Fore.YELLOW+'1.Đăng nhập')
    print(Fore.YELLOW+'2.Đăng ký')
    print(Fore.YELLOW+'3.Thoát chương trình')
    dangnhap = input(Fore.BLUE+'Chọn lựa chọn của bạn:')
    if dangnhap == '1':
        print(Fore.LIGHTGREEN_EX+'************Đăng nhập******************')
        username = input(Fore.BLUE+'Tên đăng nhập:')
        password = input(Fore.BLUE+'Mật khẩu: ')
        if username == svusn and password == svpass:
            print(Fore.GREEN+'Đăng nhập thành công')
            islogin = True
        else:
            print(Fore.RED+'Sai tên đăng nhập hoặc mật khẩu')
    elif dangnhap == '2':
        if isreg:
            print(Fore.RED+'Bạn đã đăng ký rồi')
        else:
            print(Fore.LIGHTGREEN_EX+'**************Đăng ký***************')
            regusn = input(Fore.BLUE+'Nhập tên đăng nhập:')
            regpass = input(Fore.BLUE+'Nhập tên đăng nhập:')
            svusn = regusn
            svpass = regpass
            print(Fore.GREEN+'Đăng ký thành công')
            isreg = True
    elif dangnhap == '3':
        print(Fore.GREEN+'Cảm ơn bạn đã sử dụng')
        break
    else:
        print(Fore.RED+'Sai lựa chọn vui lòng chọn lại')
    if islogin:
        balance = 0
        while 1>0:
            print(Fore.GREEN+'*****************Game tài xỉu******************')
            print(Fore.YELLOW+'Hướng dẫn cách chơi: x.Chọn xỉu, t.Chọn tài')
            menu()
            choice = input(Fore.BLUE+'Nhập lựa chọn:')
            if choice == '1':
                cuoc = int(input(Fore.BLUE+'Nhập mức cược:'))
                chon = input(Fore.BLUE+'Cược tài hoặc xỉu:')
                kq = ''
                ketqua = ''
                if chon == 't' or chon == 'x':
                    if cuoc <= balance:
                        a = r.randrange(1, 7)
                        b = r.randrange(1, 7)
                        c= r.randrange(1, 7)
                        tong = a + b + c
                        time.sleep(1)
                        print(a, end=' ')
                        time.sleep(1)
                        print(b, end=' ')
                        time.sleep(1)
                        print(c)
                        time.sleep(1)
                        if tong < 4 and chon == 'x':
                            chon = 'nh'
                            ketqua = 'Nổ hũ'
                        elif tong >= 4 and tong <=10:
                            kq = 'x'
                            ketqua = 'Xỉu'
                        elif tong > 10 and tong <= 17:
                            kq = 't'
                            ketqua = 'Tài'
                        if chon == kq:
                            balance = balance + 2*cuoc

                            print(Fore.GREEN+'Kết quả ',ketqua)
                            print(Fore.GREEN+'Bạn được cộng', 2*cuoc,'vào tài khoản')
                            print(Fore.YELLOW+'Số dư của bạn là:',balance)
                        elif chon == 'nh':
                            balance = balance + 20*cuoc
                            print(a, b, c)
                            print(Fore.GREEN+'Kết quả ',ketqua)
                            print(Fore.GREEN+'Bạn được cộng', 20*cuoc ,'vào tài khoản')
                            print(Fore.YELLOW+'Số dư của bạn là',balance)
                        else:
                            balance = balance - cuoc
                            print(a, b, c)
                            print(Fore.LIGHTRED_EX+'Bạn bị trừ',cuoc)
                            print(Fore.LIGHTRED_EX+'Số dư của bạn là:',balance)
                    else:
                        print(Fore.RED+'Bạn không đủ số dư, số dư của bạn hiện tại là',balance,'bạn cần nạp thêm',cuoc-balance)
                else:
                    print(Fore.RED+'Sai lựa chọn')
            elif choice == '2':
                print(Fore.GREEN+'Tạm biệt bạn')
                break
            elif choice == '3':
                print(Fore.GREEN+'Số dư của bạn là:',balance)
            elif choice == '4':
                amount = int(input(Fore.BLUE+'Nhập số tiền muốn nạp:'))
                balance = balance + amount
                print(Fore.GREEN+'Bạn vừa nạp',amount,'vào tài khoản số dư hiện tại',balance)
            else:
                print(Fore.RED+'Sai lựa chọn vui lòng chọn lại')
    else:
        print(Fore.RED+'Vui lòng đăng nhập')
os.system('cls')