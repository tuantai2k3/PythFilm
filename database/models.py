

from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.conf import settings  # Thêm dòng này
# Bảng Combo (Combo)
class Combo(models.Model):
    ten_combo = models.CharField(max_length=100)  # Tên combo
    gia_combo = models.DecimalField(max_digits=10, decimal_places=2)  # Giá combo
    img_combo = models.ImageField(upload_to='img_combo/')

    def __str__(self):
        return f"{self.ten_combo} - {self.gia_combo}"

# Bảng Rạp Chiếu (Cinema)
class RapChieu(models.Model):
    ten_rap = models.CharField(max_length=200)  # Tên rạp chiếu
    dia_chi = models.CharField(max_length=255)  # Địa chỉ của rạp chiếu
    so_dien_thoai = models.CharField(max_length=15)  # Số điện thoại liên hệ
    email = models.EmailField()  # Email của rạp chiếu

    def __str__(self):
        return self.ten_rap

# Bảng Định Dạng Phim (Film Format)
class DinhDangPhim(models.Model):
    ten_dinh_dang = models.CharField(max_length=50)

    def __str__(self):
        return self.ten_dinh_dang

# Bảng Thể Loại (Genre)
class TheLoai(models.Model):
    ten_the_loai = models.CharField(max_length=100)

    def __str__(self):
        return self.ten_the_loai

# Bảng Phim (Movie)
class Phim(models.Model):
    ten_phim = models.CharField(max_length=200)
    the_loai = models.ManyToManyField('TheLoai')  # Một phim có thể thuộc nhiều thể loại
    dao_dien = models.CharField(max_length=100)
    dien_vien = models.TextField()
    thoi_luong = models.PositiveIntegerField()  # Thời lượng tính bằng phút
    tom_tat = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/')  # Đường dẫn lưu ảnh thumbnail
    do_tuoi = models.PositiveIntegerField(validators=[MinValueValidator(0)], default=0)  # Độ tuổi được xem phim
    gia_ve = models.DecimalField(max_digits=10, decimal_places=2, default=100000.00)  # Set default value to 0.00
    ad_description = models.CharField(max_length=255, blank=True)  # Mô tả ngắn quảng cáo
    image = models.ImageField(upload_to='movies/', default='default_image.jpg')  # Placeholder default image


    def __str__(self):
        return self.ten_phim
    
    def get_thumbnail_url(self):
        return self.thumbnail.url 
# Bảng Xuất Chiếu (Showtimes)
class XuatChieu(models.Model):
    phim = models.ForeignKey(Phim, on_delete=models.CASCADE)
    thoi_gian_chieu = models.DateTimeField()
    rap_chieu = models.ForeignKey(RapChieu, on_delete=models.CASCADE)  # Liên kết đến bảng rạp chiếu
    dinh_dang_phim = models.ForeignKey(DinhDangPhim, on_delete=models.CASCADE)  # Liên kết đến bảng định dạng phim

    def __str__(self):
        return f"{self.phim.ten_phim} - {self.thoi_gian_chieu}"

# Bảng Ghế Ngồi (Seat)
class GheNgoi(models.Model):
    ten_ghe = models.CharField(max_length=10)  # Tên ghế
    rap_chieu = models.ForeignKey(RapChieu, on_delete=models.CASCADE)  # Rạp chiếu liên kết
    loai_ghe = models.CharField(max_length=50)  # Loại ghế
    gia_ve = models.DecimalField(max_digits=10, decimal_places=2)  # Giá vé

    def __str__(self):
        return f"{self.ten_ghe} - {self.rap_chieu.ten_rap} ({self.loai_ghe})"

from django.contrib.auth.models import AbstractBaseUser
from django.db import models

# models.py
from django.contrib.auth.models import BaseUserManager

class NguoiDungManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email phải được cung cấp')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields) 
        user.set_password(password)
        user.save(using=self._db)
        score = models.IntegerField(default=0)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)

    def get_by_natural_key(self, username):
        return self.get(username=username)


# Cập nhật lại lớp NguoiDung để sử dụng manager này
class NguoiDung(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    sdt = models.CharField(max_length=15)
    gioi_tinh = models.CharField(max_length=10, choices=[('Nam', 'Nam'), ('Nu', 'Nữ')])
    ngay_sinh = models.DateField()
    date_joined = models.DateTimeField(default=timezone.now)
    score = models.IntegerField(default=0)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'sdt', 'gioi_tinh', 'ngay_sinh']

    objects = NguoiDungManager() 

    def __str__(self):
        return self.username

class PlayerScore(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

class Ve(models.Model):
    phim = models.ForeignKey(Phim, on_delete=models.CASCADE)
    thoi_gian_chieu = models.ForeignKey(XuatChieu, on_delete=models.CASCADE)
    rap = models.ForeignKey(RapChieu, on_delete=models.CASCADE)
    ghe_ngoi = models.ManyToManyField(GheNgoi)
    ma_qr_ve = models.CharField(max_length=500, default='')  # Set default value
    user_mua_ve = models.ForeignKey(NguoiDung, on_delete=models.CASCADE)
    link_face = models.ImageField(upload_to='face/', default='face/default_face.jpg')
    combo = models.ManyToManyField(Combo, blank=True)

    def __str__(self):
        return f"Vé {self.phim.ten_phim} - {self.user_mua_ve.username}"


# Bảng Bình Luận (Comment)
class BinhLuan(models.Model):
    phim = models.ForeignKey(Phim, on_delete=models.CASCADE)  # Tên phim liên kết
    user_binh_luan = models.ForeignKey(NguoiDung, on_delete=models.CASCADE)  # Người dùng bình luận
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])  # Rating 1-5
    noi_dung = models.TextField()  # Nội dung bình luận

    def __str__(self):
        return f"Bình luận của {self.user_binh_luan.username} - {self.phim.ten_phim}"

# Bảng Contact
class Contact(models.Model):
    name = models.CharField(max_length=255)  # lưu trữ các chuỗi văn bản có độ dài tối đa được chỉ định
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField() # một trường văn bản không giới hạn độ dài
    # biểu diễn dưới dạng chuỗi (string)
    def __str__(self):
        return f"{self.name} - {self.email}"
    
# vourcher

class Voucher(models.Model):
    VOUCHER_TYPE_CHOICES = [
        ('new_user', 'Người Mới'),
        ('holiday', 'Ngày Lễ'),
    ]
    
    DISCOUNT_TYPE_CHOICES = [
        ('percentage', 'Giảm Theo Phần Trăm'),
        ('fixed', 'Giảm Cố Định'),
    ]

    voucher_type = models.CharField(max_length=50, choices=VOUCHER_TYPE_CHOICES)
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    discount_value = models.FloatField()  # Discount value
    discount_type = models.CharField(max_length=20, choices=DISCOUNT_TYPE_CHOICES)  # Discount type
    min_amount_required = models.FloatField(default=0)  # Minimum amount to use the voucher
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.code

class UserVoucher(models.Model):
    nguoi_dung = models.ForeignKey(NguoiDung, on_delete=models.CASCADE)
    voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE)
    used = models.BooleanField(default=False)
    date_issued = models.DateTimeField(default=timezone.now)
    date_used = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.nguoi_dung.username} - {self.voucher.code}'



# Bảng profile
from django.contrib.auth.models import AbstractUser
class profile(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    sdt = models.CharField(max_length=15)
    gioi_tinh = models.CharField(max_length=10, choices=[('Nam', 'Nam'), ('Nu', 'Nữ')])
    ngay_sinh = models.DateField()
    
class Player(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)  # Current score of the player

    def __str__(self):
        return self.user.username
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


class MiniGame(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
def mini_game_list(request):
    games = MiniGame.objects.all()  # Lấy tất cả các game từ cơ sở dữ liệu
    return render(request, 'mini_game_list.html', {'games': games})
class Game(models.Model):
    # Các trường hiện tại giữ nguyên
    ad_view_available = models.BooleanField(default=True)  # Có thể xem quảng cáo để thêm lượt không
    ad_bonus_used = models.BooleanField(default=False)  # Đã dùng lượt thưởng từ quảng cáo chưa
    player = models.ForeignKey(Player, on_delete=models.CASCADE)  # Link to player
    phim = models.ForeignKey(Phim, on_delete=models.CASCADE)  # Link to movie
    time_taken = models.FloatField(default=0)  # Time taken for the game
    correct_guess = models.BooleanField(default=False)  # If the guess was correct
    attempts = models.IntegerField(default=0)  # Number of attempts made
    correct_guesses = models.IntegerField(default=0)  # Number of correct guesses
    is_active = models.BooleanField(default=True)  # Game status (active or ended)
    score = models.IntegerField(default=0)  # Game score
    description = models.TextField(blank=True, null=True) 
    def __str__(self):
        return f"Game of {self.player.user.username} - Movie: {self.phim.ten_phim}"

    def update_score(self, correct: bool):
        """Update score and correct guess count"""
        if correct:
            self.correct_guesses += 1
            self.score += 10  # Add 10 points per correct guess
            self.player.score += 10  # Update player score
        self.save()
        self.player.save()

    def end_game(self):
        """End the game, update status and final score"""
        self.is_active = False
        self.player.save()
        self.save()
# models.py
class AdVideo(models.Model):
    title = models.CharField(max_length=200)
    youtube_id = models.CharField(max_length=20)
    duration = models.IntegerField(default=30)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
