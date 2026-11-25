#====================== DEF ==================
#Phần đầu menu
def menu():
    #========TIÊU ĐỀ=========
    print(f"{" "*25}{"*"*50}")
    print(f"{" "*25}{"*"*11}CHƯƠNG TRÌNH HỌC THÔNG MINH{"*"*12}")
    print(f"{" "*25}{"*"*50}")
    #======Menu============
    print("-"*100)   
    print(f"|{" "*98}|")
    print(f"|{"="*47}MENU{"="*47}|")
    print(f"|{" "*98}|")
    print("-"*100)  
    print()
    #==========NỘI DUNG MENU======
    print("-"*100)
    print(f"|{" "*98}|")
    print(f"|  VUI LÒNG LỰA CHỌN:{" "*78}|")
    print(f"|  1.Xem lịch{" "*86}|")
    print(f"|  2.Tính lương{" "*84}|")
    print(f"|  3.Xem lương{" "*85}|")
    print(f"|  4.Xem thông tin nhân viên{" "*71}|")
    print(f"|  5.Tính điểm trung bình{" "*74}|")
    print(f"|  6.Tính chỉ số BMI của cơ thể {" "*67}|")
    print(f"|  7.Máy tính đơn giản{" "*77}|")
    print(f"|  8.Trò chơi đoán số{" "*78}|")
    print(f"|  9.Trò chơi kéo búa bao{" "*74}|")
    print(f"|  10.Thoát chương trình{" "*75}|")
    for i in range(3):     
        print(f"|{" "*98}|")
    print("-"*100) 
    print()
#Xem lịch
def xem_lich(thang):
    if thang in [1,3,5,7,8,10,12]:
        ngay=31
    elif thang in [4,6,9,11]:
        ngay=30
    elif thang==2:
        nam=int(input("Tháng 2 của năm bao nhiêu: "))
        if nam%4==0 and nam%100!=0:
            ngay=29
        else:
            ngay=28
    return ngay
# Tính LƯƠNG
def tinh_luong(gio,luong):
    if gio<=40:
        tong_luong=gio*luong
    else:
        tong_luong=(luong*40)+((luong*(gio-40))*1.5)
    return tong_luong
# XEM LƯƠNG
def xem_luong(ds_luong,ten,luong):
        ds_luong.append([ten,float(luong)])
        ds_luong.sort(key=lambda x:x[1])#xếp theo index thứ 1 tương ứng với xắp xếp theo lương nếu x[0] là sắp xếp theo tên
#XEM THÔNG TIN NHÂN VIÊN
def xem_thonhtin_NV(ten):
    ho_ten_lot=' '.join(ten[0:len(ten)-1])
    ten_NV=ten[-1]
    ho_ten=' '.join(ten)
    return ho_ten_lot,ten_NV,ho_ten
# TÍNH ĐIỂM TRUNG BÌNH
def tinh_diem_TB(tong_he_so,diem_he_so):
    tong_he_so=sum(tong_he_so)
    diem_he_so=sum(diem_he_so)
    diem_trung_binh=diem_he_so/tong_he_so
    return tong_he_so,diem_he_so,diem_trung_binh
# TÍNH BMI
def tinh_BMI(can_nang,chieu_cao):
    BMI= can_nang/((chieu_cao/100)*(chieu_cao/100))
    return BMI
# MÁY TÍNH ĐƠN GIẢN
  # TÍNH TỔNG
def tinh_tong(danh_sach):
    tong=0
    for i in danh_sach:
        tong+=i
    return tong
def tinh_hieu(danh_sach):
    hieu=danh_sach[0]
    for i in danh_sach[1:]:    
        hieu-=i
    return hieu
def tinh_tich(danh_sach):
    tich=1
    for i in danh_sach:
        tich*=i
    return tich
def tinh_thuong(danh_sach):
    thuong=danh_sach[0]
    for i in danh_sach[1:]:    
        thuong/=i
    return thuong
# TRÒ CHƠI ĐOÁN SỐ
def tro_choi_doan_so(chon_so):
    import random
    so_bi_mat= random.randint(1,101)
    for i in range(7):
        if chon_so==so_bi_mat:
            print(f"Chúc mừng bạn đã đoán đúng số đó chính là {so_bi_mat}")
            break
        elif chon_so<so_bi_mat:
            print("Số bạn chọn nhỏ hơn số bí mật")
            chon_so=(int(input("Nhập số bạn đoán: ")))
        elif chon_so>so_bi_mat:
            print("Số bạn chọn lớn hơn số bí mật.")
            chon_so=(int(input("Nhập số bạn đoán: ")))
    if so_bi_mat!=chon_so:
        print(f"Bạn đã không đoán trúng hãy thử lại nhé! Số bí mật của ta là: {so_bi_mat}")
    else:
        pass