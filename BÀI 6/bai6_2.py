print ("Sinh vien: NGUYEN TRONG TU ")
pongint ("Ma so sv: 245752021610051")
class Hinhchunhat:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong
    def dientich(self):
        return self.dai * self.rong
hcn = Hinhchunhat(5, 3)
print("Diện tích hình chữ nhật là:", hcn.dientich())

