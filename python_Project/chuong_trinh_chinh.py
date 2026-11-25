import thuat_toan
# =========PHẦN LỰA CHỌN CHƯƠNG TRÌNH======
while True:
    thuat_toan.menu()
    while True:
        print()
        chon=input("Mời bạn chọn số tương ứng với các chức năng trên: ")
        if chon.isdigit() and 0<int(chon)<11:
            chon=int(chon)
            break
    print()
    #CODE XEM LỊCH
    if chon==1:
        print()
        while True:
            print(f"{" "*25}{"*"*50}")
            print(f"{" "*25}{"*"*21}XEM LỊCH{"*"*21}")
            print(f"{" "*25}{"*"*50}")
            print("_"*100)
            while True:
                thang=(input("Nhập tháng bạn muốn kiểm tra: "))
                if thang.isdigit() and 0<int(thang)<13:
                    thang=int(thang)
                    break
            print(f"Tháng {thang} của bạn có {thuat_toan.xem_lich(thang)}")
            chon = input("Nhấn Enter để tiếp tục | Space + Enter để thoát: ")
            if chon == " ":
                print("Đã thoát chương trình")
                break
        print()
    #CODE TÍNH LƯƠNG
    elif chon==2:
        print()
        while True:
            print(f"{" "*25}{"*"*50}")
            print(f"{" "*25}{"*"*20}TÍNH LƯƠNG{"*"*20}")
            print(f"{" "*25}{"*"*50}")
            print("_"*100)
            print()
            while True:
                try:
                    gio=int(input("Nhập số giờ bạn đã làm việc: "))
                    luong=float(input("Nhập số lương 1 giờ của bạn: "))
                    if gio>0 and luong>=0 and luong!="" and gio!="":
                        break
                except ValueError:
                    print("VUI LÒNG NHẬP SỐ !")
            print(f"Tổng số tiền lương của bạn với số giờ {gio} và lương mỗi giờ {luong} là: {thuat_toan.tinh_luong(gio,luong):.1f}VNĐ")
            chon = input("Nhấn Enter để tiếp tục | Space + Enter để thoát: ")
            if chon == " ":
                print("Đã thoát chương trình")
                break
        print()
    #CODE XEM LƯƠNG
    elif chon==3:
        print()
        while True: 
            print(f"{" "*25}{"*"*50}")
            print(f"{" "*25}{"*"*21}XEM LƯƠNG{"*"*20}")
            print(f"{" "*25}{"*"*50}")
            print("_"*100) 
            print() 
            ds_luong=[]
            while True:
                so_luong=(input("Nhập số lượng nhân viên cần nhập: "))
                if so_luong.isdigit() and (int)(so_luong)>0:
                    so_luong=int(so_luong)
                    break
            for i in range(so_luong):
                while True:
                    ten=input(f"Nhập tên nhân viên thứ {i+1}: ").title()
                    if ten!="":
                        break
                while True:   
                    try:
                        luong=float(input(f"Nhập lương của nhân viên {ten}: "))
                        break
                    except ValueError:
                        print("CHỈ NHẬP SỐ NGUYÊN VUI LÒNG NHẬP LẠI!")
                thuat_toan.xem_luong(ds_luong,ten,luong)
            print("Danh sách lương theo thứ tự tăng dần")
            for j in range(so_luong):
                print(*ds_luong[j],sep=" :",end=" VNĐ")
                print()
            chon = input("Nhấn Enter để tiếp tục | Space + Enter để thoát: ")
            if chon == " ":
                print("Đã thoát chương trình")
                break
            print()
    #CODE XEM THÔNG TIN NHÂN VIÊN
    elif chon==4:
        print()
        while True:
            print(f"{" "*25}{"*"*50}")
            print(f"{" "*25}{"*"*14}XEM THÔNG TIN NHÂN VIÊN{"*"*13}")
            print(f"{" "*25}{"*"*50}")
            print("_"*100)
            print()
            #strip(): xóa khoảng trắng 2 đầu
            #title(): viết hoa chữ cái đầu
            #split():tách chuỗi thành các phần tử list
            ten=input("Nhập tên nhân viên: ").strip().title().split()
            #' '.join: dùng để nối các phần tử của list thành chuỗi cách nhau bằng khoảng trắng
            ho_ten_lot, ten_NV, ho_ten = thuat_toan.xem_thonhtin_NV(ten)
            print(f"Họ và tên lót của nhân viên là: {ho_ten_lot}")
            print(f"Tên của nhân viên là: {ten_NV}")
            print(f"Họ và tên đầy đủ của nhân viên là: {ho_ten}")
            chon = input("Nhấn Enter để tiếp tục | Space + Enter để thoát: ")
            if chon == " ":
                print("Đã thoát chương trình")
                break
            print()
    #CODE TÍNH ĐIỂM TRUNG BÌNH
    elif chon==5:
        print()
        while True:
            print(f"{" "*25}{"*"*50}")
            print(f"{" "*25}{"*"*15}TÍNH ĐIỂM TRUNG BÌNH{"*"*15}")
            print(f"{" "*25}{"*"*50}")
            print("_"*100)
            print()
            while True:
                try:
                    so_mon=int(input("Nhập số môn cần tính trung bình: "))
                    if so_mon>0:
                        break
                except :
                    print("Vui lòng nhập số nguyên!")
            tong_he_so=[]
            diem_he_so=[]
            for i in range(so_mon):
                while True:
                    try:
                        diem=float(input(f"Nhập điểm môn  thứ {i+1}: "))
                        if -1<diem<11 :
                            break
                    except ValueError:
                        print("Không dược nhập chữ vui lòng nhập lại!")
                while True:
                    try:
                        he_so=float(input(f"Nhập hệ số của môn thứ {i+1}: "))
                        if 0<he_so<4:
                            break
                    except ValueError:
                        print("Không dược nhập chữ vui lòng nhập lại!")
                tong_he_so.append(he_so)
                diem_he_so.append(diem*he_so)
            tong_he_so,diem_he_so,diem_trung_binh=thuat_toan.tinh_diem_TB(tong_he_so,diem_he_so)
            print(tong_he_so)
            print(f"Tổng hệ số là: {tong_he_so}")
            print(f"Tổng số môn là: {so_mon}")
            print(f"Điểm trung bình là: {diem_trung_binh:.2f}")
            chon = input("Nhấn Enter để tiếp tục | Space + Enter để thoát: ")
            if chon == " ":
                print("Đã thoát chương trình")
                break
        print()
    #CODE TÍNH BMI
    elif chon==6:
        print()
        while True:
            print(f"{" "*25}{"*"*50}")
            print(f"{" "*25}{"*"*18}TÍNH CHỈ SỐ BMI{"*"*17}")
            print(f"{" "*25}{"*"*50}")
            print("_"*100)
            print()
            while True:
                chieu_cao=(input("Nhập chiều cao của bạn: "))
                can_nang=(input("Nhập cân nặng của bạn: "))
                if chieu_cao.isdigit() and 0<float(chieu_cao) and can_nang.isdigit() and float(can_nang)>0:
                    chieu_cao=float(chieu_cao)
                    can_nang=float(can_nang)
                    break
            BMI=thuat_toan.tinh_BMI(can_nang,chieu_cao)
            if BMI<18.5:
                print(f"Chỉ số BMI của bạn là: {BMI:.2f} bạn hơi gầy nên ăn uống nhiều hơn")
            elif 18.5 <= BMI <= 22.9:
                print(f"Chỉ số BMI của bạn là: {BMI:.2f} bạn có sức khỏe khỏe mạnh")
            else:
                print(f"Chỉ số BMI của bạn là: {BMI:.2f} bạn hơi thừa cân")
            chon = input("Nhấn Enter để tiếp tục | Space + Enter để thoát: ")
            if chon == " ":
                print("Đã thoát chương trình")
                break
            print()
    #CODE MÁY TÍNH ĐƠN GIẢN
    elif chon==7:
        print()
        while True:
            print(f"{" "*25}{"*"*50}")
            print(f"{" "*25}{"*"*16}MÁY TÍNH ĐƠN GIẢN{"*"*17}")
            print(f"{" "*25}{"*"*50}")
            print("_"*100)
            print("1.PHÉP CỘNG")
            print("2.PHÉP TRỪ")
            print("3.PHÉP NHÂN")
            print("4.PHÉP CHIA")
            print()
            while True:    
                try:
                    lua_chon=int(input("Chọn các số tương ứng với chức năng trên: "))
                    if 0<lua_chon<5:
                        break
                except ValueError:
                    print("Phải nhập số xin nhập lại!")
            danh_sach=[]
            if lua_chon==1:
                while True:
                    try:
                        so_luong=int(input("Nhập số lượng số bạn muốn tính tổng: "))
                        if 0<so_luong:
                            break
                    except ValueError:
                        print("Phải nhập số xin nhập lại!")
                tong=0
                for i in range(so_luong):
                    try:
                        so=float(input(f"Nhập số thứ {i+1}: "))
                    except ValueError:
                        print("Phải nhập số xin nhập lại!")
                    danh_sach.append(so)
                tong=thuat_toan.tinh_tong(danh_sach)
                print(f"Danh sách các số bạn đã nhập: {danh_sach}")
                print(f"Tổng của các số trong danh sách là: {tong:.2f}")
            elif lua_chon==2:
                while True:
                    try:
                        so_luong=int(input("Nhập số lượng số bạn muốn tính hiệu: "))
                        if 0<so_luong:
                            break
                    except ValueError:
                        print("Phải nhập số xin nhập lại!")
                for i in range(so_luong):
                    try:
                        so=float(input(f"Nhập số thứ {i+1}: "))
                    except ValueError:
                        print("Phải nhập số xin nhập lại!")
                    danh_sach.append(so)
                hieu=thuat_toan.tinh_hieu(danh_sach)
                print(f"Danh sách các số bạn đã nhập: {danh_sach}")
                print(f"Hiệu của các số trong danh sách là: {hieu:.2f}")
            elif lua_chon==3:
                while True:
                    try:
                        so_luong=int(input("Nhập số lượng số bạn muốn tính tích: "))
                        if 0<so_luong:
                            break
                    except ValueError:
                        print("Phải nhập số xin nhập lại!")
                for i in range(so_luong):
                    try:
                        so=float(input(f"Nhập số thứ {i+1}: "))
                    except ValueError:
                        print("Phải nhập số xin nhập lại!")
                    danh_sach.append(so)
                tich=thuat_toan.tinh_tich(danh_sach)
                print(f"Danh sách các số bạn đã nhập: {danh_sach}")
                print(f"Tích của các số trong danh sách là: {tich:.2f}")
            elif lua_chon==4:
                while True:
                    try:
                        so_luong=int(input("Nhập số lượng số bạn muốn tính thương: "))
                        if 0<so_luong:
                            break
                    except ValueError:
                        print("Phải nhập số xin nhập lại!")
                for i in range(so_luong):
                    while True:
                        try:
                            so=float(input(f"Nhập số thứ {i+1}: "))
                            if so!=0:
                                break
                        except ValueError:
                            print("Vui lòng nhập số!")
                    danh_sach.append(so)
                thuong=thuat_toan.tinh_thuong(danh_sach)
                print(f"Danh sách các số bạn đã nhập: {danh_sach}")
                print(f"Hiệu của các số trong danh sách là: {thuong:.2f}")    
            chon = input("Nhấn Enter để tiếp tục | Space + Enter để thoát: ")
            if chon == " ":
                print("Đã thoát chương trình")
                break
        #"try" và 'except ValueError":bắt lỗi khi người dùng nhập KHÔNG phải số
        print()
    #CODE TRÒ CHƠI ĐOÁN SỐ
    elif chon==8:
        print()
        while True:
            print(f"{" "*25}{"*"*50}")
            print(f"{" "*25}{"*"*17}TRÒ CHƠI ĐOÁN SỐ{"*"*17}")
            print(f"{" "*25}{"*"*50}")
            print("_"*100)
            print("Chào mừng bạn đến với trò chơi đoán số")
            #Lệnh bên dưới dùng để gọi hàm random 
            print("Tôi đã chọn số bí mật từ 1 đến 100 để bạn đoán nhé. Bạn sẻ có 7 lần đoán nhé.")
            while True:
                chon_so=input("Chọn số nguyên bạn muốn: ")
                if chon_so.isdigit() and 0<int(chon_so)<101:
                    chon_so=int(chon_so)
                    break
            thuat_toan.tro_choi_doan_so(chon_so)
            chon = input("Nhấn Enter để tiếp tục | Space + Enter để thoát: ")
            if chon == " ":
                print("Đã thoát chương trình")
                break
        print()
    #CODE TRÒ CHƠI KÉO BÚA BAO
    elif chon==9:
        print()
        while True:
            print(f"{" "*25}{"*"*50}")
            print(f"{" "*25}{"*"*15}TRÒ CHƠI KÉO BÚA BAO{"*"*15}")
            print(f"{" "*25}{"*"*50}")
            print("_"*100)   
            import random
            keo_bua_bao=["KÉO","BÚA","BAO"]
            #random.choice(): dùng để chọn ngẫu nhiên phần tử trong list
            bi_mat=random.choice(keo_bua_bao)
            ban=0
            toi=0
            for i in range(5):
                while True:
                    chon=input("Bạn hãy chọn kéo búa bao: ").upper()
                    if chon.isalpha() and chon in keo_bua_bao:
                        break
                    print("Hãy chọn KÉO BÚA hoặc BAO")    
                if bi_mat==chon:
                    print(f"Tôi chọn: {bi_mat} | Bạn chọn: {chon} chúng ta hòa nhau")
                elif bi_mat=="KÉO" and chon=="BAO":
                    print(f"Tôi chọn: {bi_mat} | Bạn chọn: {chon} Tôi thắng")
                    toi+=1
                elif chon=="KÉO" and bi_mat=="BAO":
                    print(f"Tôi chọn: {bi_mat} | Bạn chọn: {chon} Bạn thắng")
                    ban+=1
                elif bi_mat=="KÉO" and chon=="BÚA":
                    print(f"Tôi chọn: {bi_mat} | Bạn chọn: {chon} Bạn thắng")
                    ban+=1
                elif chon=="KÉO" and bi_mat=="BÚA":
                    print(f"Tôi chọn: {bi_mat} | Bạn chọn: {chon} Tôi thắng")
                    toi+=1
                elif bi_mat=="BÚA" and chon=="BAO":
                    print(f"Tôi chọn: {bi_mat} | Bạn chọn: {chon} Bạn thắng")
                    ban+=1
                elif bi_mat=="BAO" and chon=="BÚA":
                    print(f"Tôi chọn: {bi_mat} | Bạn chọn: {chon} Tôi thắng")
                    toi+=1
            if toi>ban:
                print(f"Tỉ số giữa tôi và bạn là {toi}:{ban}")
                print(f"=> TÔI THẮNG")
            elif toi==ban:
                print(f"Tỉ số giữa tôi và bạn là {toi}:{ban}")
                print(f"=> CHÚNG TA HÒA NHAU")
            else:
                print(f"Tỉ số giữa tôi và bạn là {toi}:{ban}")
                print(f"=> BẠN THẮNG")
            chon = input("Nhấn Enter để tiếp tục | Space + Enter để thoát: ")
            if chon == " ":
                print("Đã thoát chương trình")
                break
        print()
    #THOÁT CHƯƠNG TRÌNH
    elif chon==10:
        print("CHƯƠNG TRÌNH KẾT THÚC!")
        break