# chuong trinh chia tien co tip

print("chao mung ban den voi chuong trinh chia tien co tip")
hoadon = int(input("tien theo hoa don cua ban la: "))
phantram = int(input("ban muon tip bao nhieu phan tram cua hoa don: "))
songuoi = int(input("so nguoi chia deu hoa don: "))
tiencanhan = (hoadon + (hoadon*(phantram/100))) / songuoi
print(f"so tien ma moi nguoi phai tra: {tiencanhan}")