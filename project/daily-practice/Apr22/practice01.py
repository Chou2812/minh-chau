"""Đề bài: Nhập vào 3 điểm: Toán, Lý, Hóa
Tính và in ra điểm trung bình cộng 3 môn
Sau đó xet:
ĐTB >= 8 thì in: học sinh giỏi
6.5 <= ĐTB <8 thì in: học sinh khá
5 <= ĐTB < 6.5 thì in: Học sinh TB
ĐTB < 5 thì in: Học sinh Kém"""

a = float(input("Vui lòng nhập điểm Toán: "))
b = float(input("Vui lòng nhập điểm Lý: "))
c = float(input("Vui lòng nhập điểm Hóa: "))
diemTrungBinh = (a + b + c)/3
if diemTrungBinh >= 8:
    print(f"Điểm trung bình là: {diemTrungBinh}, đây là học sinh Giỏi")
if 6.5 <= diemTrungBinh <8:
    print(f"Điểm trung bình là: {diemTrungBinh}, đây là học sinh Khá")
if 5 <= diemTrungBinh < 6.5:
    print(f"Điểm trung bình là: {diemTrungBinh}, đây là học sinh Trung Bình")
if diemTrungBinh < 5:
    print(f"Điểm trung bình là: {diemTrungBinh}, đây là học sinh Yếu")