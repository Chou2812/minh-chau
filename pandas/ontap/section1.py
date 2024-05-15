giaGa = float(input("Nhap so luong Ham Ga")) * 25
giaTom = float(input("Nhap so luong Ham Tom")) * 20
giaBo = float(input("Nhap so luong Ham Bo")) * 45
Tongbill = giaTom + giaGa + giaBo
if Tongbill > 100 and Tongbill < 200:
    print(f"gia tien phai thu: {Tongbill - (Tongbill * 0.05)}")
if Tongbill > 200 and Tongbill < 300:
    print(f"gia tien phai thu: {Tongbill - (Tongbill * 0.1)}")
if Tongbill > 300:
    print(f"gia tien phai thu: {Tongbill - (Tongbill * 0.15)}")
if Tongbill <100:
    print(f"gia tien phai thu: {Tongbill}")