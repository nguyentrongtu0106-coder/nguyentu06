print ("Sinh vien: NGUYEN TRONG TU")
print ("Ma so sv: 245752021610051")
chuoi = input("Nhập chuỗi các từ tiếng Anh, cách nhau bằng dấu cách: ")
ds_tu = chuoi.split()
ds_tu.sort()
print("Các từ sau khi sắp xếp theo thứ tự từ điển là:")
for tu in ds_tu:
    print(tu)
