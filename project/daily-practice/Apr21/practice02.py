"""
Đề bài: nhập vào 1 số bất kỳ, kiểm tra số đó chẵn hay lẻ
    """

a = int(input("Vui lòng nhập số muốn kiểm tra: "))
if a % 2 == 0:
    print(f"{a} là số chẵn")
else:
    print(f"{a} la số lẻ")