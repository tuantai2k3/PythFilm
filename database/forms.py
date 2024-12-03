from django import forms
from .models import Phim, NguoiDung, TheLoai, DinhDangPhim, XuatChieu, RapChieu, Ve, GheNgoi, Combo, BinhLuan, Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Combo

class ComboForm(forms.ModelForm):
    class Meta:
        model = Combo
        fields = ['ten_combo', 'gia_combo', 'img_combo']

class PhimForm(forms.ModelForm):
    class Meta:
        model = Phim
        fields = ['ten_phim', 'the_loai', 'dao_dien', 'dien_vien', 'thoi_luong', 'tom_tat', 'thumbnail', 'do_tuoi','gia_ve']

class NguoiDungForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = NguoiDung
        fields = ['username', 'email', 'sdt', 'password', 'gioi_tinh', 'ngay_sinh']
        widgets = {
            'password': forms.PasswordInput(),
            'ngay_sinh': forms.DateInput(attrs={'type': 'date', 'placeholder': 'dd/mm/yyyy'})
        }
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Mật khẩu và mật khẩu nhập lại không khớp!")
        return cleaned_data
        
class TheLoaiForm(forms.ModelForm):
    class Meta:
        model = TheLoai
        fields = ['ten_the_loai']
        
class DinhDangPhimForm(forms.ModelForm):
    class Meta:
        model = DinhDangPhim
        fields = ['ten_dinh_dang']
        
        
class RapChieuForm(forms.ModelForm):
    class Meta:
        model = RapChieu
        fields = ['ten_rap', 'dia_chi', 'so_dien_thoai', 'email']
        
        
        
class XuatChieuForm(forms.ModelForm):
    class Meta:
        model = XuatChieu
        fields = ['phim', 'thoi_gian_chieu', 'rap_chieu', 'dinh_dang_phim']
        widgets = {
            'thoi_gian_chieu': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # Định dạng cho thời gian chiếu
        }

# class VeForm(forms.ModelForm):
#     class Meta:
#         model = Ve
#         fields = ['phim', 'thoi_gian_chieu', 'rap', 'ghe_ngoi', 'loai_ghe', 'gia_ve', 'ma_qr_ve', 'user_mua_ve', 'link_face']



from django import forms
from .models import Ve, Combo, GheNgoi

class VeForm(forms.ModelForm):
    class Meta:
        model = Ve
        fields = ['phim', 'thoi_gian_chieu', 'rap', 'ghe_ngoi', 'ma_qr_ve', 'user_mua_ve', 'combo', 'link_face']
        widgets = {
            'phim': forms.Select(),
            'thoi_gian_chieu': forms.Select(),
            'rap': forms.Select(),
            'ma_qr_ve': forms.TextInput(),
            'user_mua_ve': forms.Select(),
            'ghe_ngoi': forms.CheckboxSelectMultiple(),  # Sử dụng CheckboxSelectMultiple để chọn nhiều ghế ngồi
            'combo': forms.CheckboxSelectMultiple(),  # Sử dụng CheckboxSelectMultiple để chọn nhiều combo
        }
    
    # Nếu bạn muốn chọn nhiều combo, bạn sẽ cần sử dụng ModelMultipleChoiceField
    combo = forms.ModelMultipleChoiceField(
        queryset=Combo.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False  # Chọn có thể không chọn bất kỳ combo nào
    )

    # Nếu bạn muốn chọn nhiều ghế ngồi, bạn sẽ cần sử dụng ModelMultipleChoiceField
    ghe_ngoi = forms.ModelMultipleChoiceField(
        queryset=GheNgoi.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=True  # Nếu bạn bắt buộc phải chọn ít nhất một ghế ngồi
    )




        
class GheNgoiForm(forms.ModelForm):
    class Meta:
        model = GheNgoi
        fields = ['ten_ghe', 'rap_chieu', 'loai_ghe', 'gia_ve']


class BinhLuanForm(forms.ModelForm):
    class Meta:
        model = BinhLuan
        fields = ['phim', 'user_binh_luan', 'rating', 'noi_dung']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'noi_dung': forms.Textarea(attrs={'rows': 3}),
        }



# forms.py
from django import forms
from .models import XuatChieu

class XuatChieuFormTuDong(forms.Form):
    phim = forms.ModelChoiceField(queryset=Phim.objects.all(), label="Phim")
    rap_chieu = forms.ModelChoiceField(queryset=RapChieu.objects.all(), label="Rạp chiếu")
    dinh_dang_phim = forms.ModelChoiceField(queryset=DinhDangPhim.objects.all(), label="Định dạng phim")
    ngay_chieu = forms.DateField(label="Ngày chiếu", widget=forms.DateInput(attrs={'type': 'date'}))



# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import NguoiDung

# Form đăng ký người dùng
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    sdt = forms.CharField(max_length=15, required=True)
    gioi_tinh = forms.ChoiceField(choices=[('Nam', 'Nam'), ('Nu', 'Nữ')], required=True)
    ngay_sinh = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)))

    class Meta:
        model = NguoiDung
        fields = ['username', 'email', 'sdt', 'gioi_tinh', 'ngay_sinh', 'password1', 'password2']

# Form chỉnh sửa thông tin người dùng (profile)
class ProfileForm(forms.ModelForm):
    class Meta:
        model = NguoiDung
        fields = ['email', 'sdt', 'gioi_tinh', 'ngay_sinh']


class NguoiDungForm(forms.ModelForm):
    class Meta:
        model = NguoiDung
        fields = ['username', 'email', 'sdt', 'gioi_tinh', 'ngay_sinh']
        widgets = {
            'ngay_sinh': forms.DateInput(attrs={'type': 'date', 'placeholder': 'dd/mm/yyyy'})  # Định dạng ngày sinh
        }

class UserForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

from .models import Voucher

class VoucherForm(forms.ModelForm):
    class Meta:
        model = Voucher
        fields = ['voucher_type', 'code', 'description', 'discount_value', 'discount_type', 'min_amount_required', 'start_date', 'end_date', 'active']