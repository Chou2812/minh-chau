"""Đề bài: nhập vào lương của nhân viên
Nếu lương lớn hơn 2 triệu thì trừ 10% lương
Tính số lương thực nhận
    """
    
a = float(input("Nhập số lương của mình: "))
luongThucnhan = a - (a * 0.1)
if a >= 2000000:
    print(f"lương thực nhận là: {luongThucnhan}")
else:
    print(f"lương thực nhận là {a}")