from django.db import models

# Create your models here.

class DANHMUCSANPHAM(models.Model):
    MaDanhMuc = models.AutoField(primary_key=True)
    TenDanhMuc = models.CharField(max_length=30, null=True)

class HANGSANXUAT(models.Model):
    MaHang = models.AutoField(primary_key=True)
    TenHang = models.CharField(max_length=20, null=True)

class SANPHAM(models.Model):
    MaSP = models.AutoField(primary_key=True)
    TenSP = models.CharField(max_length=100, null=True)
    MoTa = models.CharField(max_length=1000, null=True)
    Anh1 = models.CharField(max_length=20, null=True)
    Anh2 = models.CharField(max_length=20, null=True)
    Anh3 = models.CharField(max_length=20, null=True)
    
    Anh4 = models.CharField(max_length=20, null=True)
    Anh5 = models.CharField(max_length=20, null=True)
    Anh6 = models.CharField(max_length=20, null=True)
    SoLuongDaBan = models.IntegerField(null=True)
    SoLuongTrongKho = models.IntegerField(null=True)
    GiaTien = models.BigIntegerField(null=True)
    MaHang = models.ForeignKey(HANGSANXUAT, on_delete=models.CASCADE, null=True)
    MaDanhMuc = models.ForeignKey(DANHMUCSANPHAM, on_delete=models.CASCADE, null=True)


class DONHANG(models.Model):
    MaDonHang = models.AutoField(primary_key=True)
    MaTaiKhoan = models.IntegerField(null=True)
    TongTien = models.BigIntegerField(null=True)
    TinhTrang = models.IntegerField(null=True)
    NgayLap = models.DateField(null=True)

class GioHang(models.Model):
    MaTaiKhoan = models.IntegerField()
    MaSP = models.IntegerField()
    SoLuong = models.IntegerField(null=True)


class VANCHUYEN(models.Model):
    MaDonHang = models.IntegerField(primary_key=True)
    NguoiNhan = models.CharField(max_length=50, null=True)
    DiaChi = models.CharField(max_length=50, null=True)
    SDT = models.CharField(max_length=20, null=True)
    HinhThucVanChuyen = models.CharField(max_length=20, null=True)

class CHITIETSANPHAM(models.Model):
    MaSP = models.IntegerField(primary_key=True)
    CanNang = models.IntegerField(null=True)
    KichThuoc = models.CharField(max_length=30, null=True)
    CongSuat = models.CharField(max_length=30, null=True)
    NoiSanXuat = models.CharField(max_length=20, null=True)
    NamSanXuat = models.CharField(max_length=10, null=True)

class CHITIETDONHANG(models.Model):
    MaDonHang = models.ForeignKey(DONHANG, on_delete=models.CASCADE)
    MaSP = models.ForeignKey(SANPHAM, on_delete=models.CASCADE)
    SoLuongMua = models.IntegerField(null=True)

class DANHGIASANPHAM(models.Model):
    MaTaiKhoan = models.IntegerField()
    MaSP = models.IntegerField()
    DanhGia = models.IntegerField(null=True)
    NoiDungBinhLuan = models.CharField(max_length=200, null=True)
    NgayDanhGia = models.DateField(null=True)
