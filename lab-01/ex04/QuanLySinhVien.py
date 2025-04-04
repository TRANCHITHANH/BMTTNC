from SinhVien import SinhVien
class QuanLySinhVien:
    listSinhVien = []
    def generateID(self):
        maxID = 1
        if(self.soLuongSinhVien() > 0):
            maxID = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if(sv._id > maxID):
                    maxID = sv._id
            maxID += 1
        return maxID
    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()
    def nhapSinhVien(self):
        svId = self.generateID()
        name= input("Nhập tên sinh viên: ")
        sex= input("Nhập giới tính: ")
        major= input("Nhập ngành học: ")
        diemTB= float(input("Nhập điểm trung bình: "))
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)
        
    def updateSinhVien(self, id):
        sv:SinhVien = self.findByID(ID)
        if(sv != None):
            name= input("Nhập tên sinh viên: ")
            sex = input("Nhập giới tính: ")
            major = input("Nhập ngành học: ")
            diemTB = float(input("Nhập điểm trung bình: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print("Không tìm thấy sinh viên có mã số", id)
    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)
        
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)
        
    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=True)
    
    def findByID(self, id):
        searchResult = None
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if(sv._id == id):
                    searchResult = sv
        return searchResult
    def findByName(self, name):
        searchResult = []
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if(sv._name == name):
                    searchResult.append(sv)
        return searchResult
    def deleteByID(self, id):
        isDeleted = False
        sv= self.findByID(id)
        if(sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted
    def xepLoaiHocLuc(self, sv:SinhVien):
        if(sv._diemTB >= 8):
            sv._hocLuc = "Giỏi"
        elif(sv._diemTB >= 6.5):
            sv._hocLuc = "Khá"
        elif(sv._diemTB >= 5):
            sv._hocLuc = "Trung bình"
        else:
            sv._hocLuc = "Yếu"
    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8}"
              .format("ID", "Name", "Sex", "Major", "DiemTB", "HocLuc"))
        if (listSV.__len__()>0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8}"
                      .format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
                print("/n")
    def getListSinhVien(self):
        return self.listSinhVien    
        