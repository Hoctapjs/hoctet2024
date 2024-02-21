# print("chao mung den voi he thong ban ve tau dien")
# chieucao = int(input("ban cao bao nhieu (cm): "))
# if chieucao > 120:
#     print("ban co the mua ve tau dien sieu toc")
# else:
#     print("ban ko the mua ve tau dien sieu toc")

# chuong trinh kiem tra so chan, le
# print("chao mung den voi chuong trinh tim so chan le")
# num = int(input("nhap vao 1 so nguyen bat ky: "))
# if num % 2 == 1:
#     print("so la so le")
# else:
#     print("so la so chan")

# print("chao mung den voi he thong ban ve tau dien")
# chieucao = int(input("ban cao bao nhieu (cm): "))
# if chieucao > 120:
#     print("ban co the mua ve tau dien sieu toc")
#     dotuoi = int(input("nhap vao tuoi cua ban"))
#     if dotuoi < 18:
#         print("ve cua ban la 70.000")
#     else:
#         print("ve cua ban la 150.000")   
# else:
#     print("ban ko the mua ve tau dien sieu toc")

# he thong tinh ngay trong thang
# thang = int(input("nhap vao thang muon kiem tra: "))
# if thang != 2:
#     if thang == 1:
#         print("thang co 31 ngay")
#     elif thang == 3:
#         print("thang co 31 ngay")
#     elif thang == 5:
#         print("thang co 31 ngay")
#     elif thang == 7:
#         print("thang co 31 ngay")
#     elif thang == 8:
#         print("thang co 31 ngay")
#     elif thang == 10:
#         print("thang co 31 ngay")
#     elif thang == 12:
#         print("thang co 31 ngay")
#     else:
#         print("thang co 30 ngay")
# else:
#     print("thang co 28 / 29 ngay")
    
# can_nang = int(input("nhap vao can nang(kg): "))
# chieu_cao = float(input("nhap vao chieu cao(m): "))
# chiso_BMI = (can_nang/(chieu_cao**2))
# print(f"chi so khoi co the la: {chiso_BMI}")
# if chiso_BMI > 18.5:
#     if chiso_BMI < 25:
#         print("ban co can nang binh thuong")
#     elif (chiso_BMI > 25) & (chiso_BMI < 30):
#         print("ban dang thua can")
#     elif chiso_BMI > 30:
#         print("ban dang beo phi")
# else:
#     print("ban dang thieu can")

nam = int(input("nhap vao nam: "))
if nam % 4 == 0:
    if nam % 100 == 0:
        if nam % 400 == 0:
            print("nam la nam nhuan")
        else:
            print("nam khong phai la nam nhuan")
    else:
        print("nam la nam nhuan")
else:
    print("nam khong phai la nam nhuan")