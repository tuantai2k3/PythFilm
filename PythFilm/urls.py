from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from database import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('phim/', views.danh_sach_phim, name='danh_sach_phim'),
    path('phim/them/', views.them_phim, name='them_phim'),
    path('phim/sua/<int:id>/', views.sua_phim, name='sua_phim'),
    path('phim/xoa/<int:id>/', views.xoa_phim, name='xoa_phim'),

    # Đường dẫn cho quản lý người dùng
    path('nguoidung/', views.danh_sach_nguoi_dung, name='danh_sach_nguoi_dung'),
    path('nguoidung/them/', views.them_nguoi_dung, name='them_nguoi_dung'),
    path('nguoidung/sua/<int:id>/', views.sua_nguoi_dung, name='sua_nguoi_dung'),
    path('nguoidung/xoa/<int:id>/', views.xoa_nguoi_dung, name='xoa_nguoi_dung'),
    
    # Đường dẫn cho quản lý thể loại
    path('theloai/', views.danh_sach_the_loai, name='danh_sach_the_loai'),
    path('theloai/them/', views.them_the_loai, name='them_the_loai'),
    path('theloai/sua/<int:id>/', views.sua_the_loai, name='sua_the_loai'),
    path('theloai/xoa/<int:id>/', views.xoa_the_loai, name='xoa_the_loai'),
    
    # Đường dẫn cho quản lý định dạng phim
    path('dinhdangphim/', views.danh_sach_dinh_dang_phim, name='danh_sach_dinh_dang_phim'),
    path('dinhdangphim/them/', views.them_dinh_dang_phim, name='them_dinh_dang_phim'),
    path('dinhdangphim/sua/<int:id>/', views.sua_dinh_dang_phim, name='sua_dinh_dang_phim'),
    path('dinhdangphim/xoa/<int:id>/', views.xoa_dinh_dang_phim, name='xoa_dinh_dang_phim'),
    
    # Đường dẫn cho quản lý rạp chiếu
    path('rapchieu/', views.danh_sach_rap_chieu, name='danh_sach_rap_chieu'),
    path('rapchieu/them/', views.them_rap_chieu, name='them_rap_chieu'),
    path('rapchieu/sua/<int:id>/', views.sua_rap_chieu, name='sua_rap_chieu'),
    path('rapchieu/xoa/<int:id>/', views.xoa_rap_chieu, name='xoa_rap_chieu'),
    
    # Đường dẫn cho quản lý xuất chiếu
    path('xuatchieu/', views.danh_sach_xuat_chieu, name='danh_sach_xuat_chieu'),
    path('xuatchieu/them/', views.them_xuat_chieu, name='them_xuat_chieu'),
    path('xuatchieu/sua/<int:id>/', views.sua_xuat_chieu, name='sua_xuat_chieu'),
    path('xuatchieu/xoa/<int:id>/', views.xoa_xuat_chieu, name='xoa_xuat_chieu'),
    
    # Đường dẫn cho quản lý vé
    path('ve/', views.danh_sach_ve, name='danh_sach_ve'),
    path('ve/them/', views.them_ve, name='them_ve'),
    path('ve/sua/<int:id>/', views.sua_ve, name='sua_ve'),
    path('ve/xoa/<int:id>/', views.xoa_ve, name='xoa_ve'),
    
    # Đường dẫn cho quản lý ghế ngồi
    path('ghengoi/', views.danh_sach_ghe_ngoi, name='danh_sach_ghe_ngoi'),
    path('ghengoi/them/', views.them_ghe_ngoi, name='them_ghe_ngoi'),
    path('ghengoi/sua/<int:id>/', views.sua_ghe_ngoi, name='sua_ghe_ngoi'),
    path('ghengoi/xoa/<int:id>/', views.xoa_ghe_ngoi, name='xoa_ghe_ngoi'),
    
    # Combo Routes
    path('combos/', views.danh_sach_combo, name='danh_sach_combo'),
    path('combos/them/', views.them_combo, name='them_combo'),
    path('combos/sua/<int:id>/', views.sua_combo, name='sua_combo'),
    path('combos/xoa/<int:id>/', views.xoa_combo, name='xoa_combo'),
    
    # Comment Routes
    path('binh-luan/', views.danh_sach_binh_luan, name='danh_sach_binh_luan'),
    path('binh-luan/them/', views.them_binh_luan, name='them_binh_luan'),
    path('binh-luan/sua/<int:id>/', views.sua_binh_luan, name='sua_binh_luan'),
    path('binh-luan/xoa/<int:id>/', views.xoa_binh_luan, name='xoa_binh_luan'),
    
    # Web management for tickets
    path('adminn', views.quan_ly, name='quan_ly'),
    
    # Main Pages
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('comboselect/', views.select_combo, name='select_combo'),
    path('checkout/', views.check_out, name='check_out'), 
    path('tao-xuat-chieu/', views.tao_xuat_chieu_tu_dong, name='tao_xuat_chieu'),
    path('film/<int:phim_id>/', views.film_detail, name='film_detail'),
    path('seat/<int:phim_id>/<int:xuat_chieu_id>/', views.seat_selection, name='seat_selection'),
    path('comboselect/<int:phim_id>/<int:xuat_chieu_id>/<str:ghe_ngoi_ids>/', views.select_combo, name='select_combo'),
    path('checkout/<int:phim_id>/<int:xuat_chieu_id>/<str:ghe_ngoi_ids>/<str:combo_ids>', views.check_out, name='chec_kout'),
    path('ticket_success/<int:ve_id>/', views.ticket_success, name='ticket_success'),
    
    # Authentication Routes
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('password/', views.updatePassword, name='password'),
    path('update-user/', views.updateUser, name='update-user'),
    
    # Contact Routes
    path('contact/', views.contact_view, name='contact'),
    path('lienhe/', views.contact_list, name='danh_sach_lien_he'),
    path('lienhe/sua/<int:pk>/', views.contact_edit, name='sua_lien_he'),
    path('lienhe/xoa/<int:id>/', views.contact_delete, name='xoa_lien_he'),
    
    # Voucher Routes
    path('managevouchers/', views.manage_vouchers, name='managevouchers'),
    path('addvoucher/', views.add_voucher, name='add_voucher'),

    # Mini Game Routes
   # Mini Game Routes
path('game/', views.game_page, name='game_page'),
path('game/guess/<int:phim_id>/', views.guess_movie, name='guess_movie'),
path('game/result/', views.guess_result, name='guess_result'),
path('game/over/', views.guess_game_over, name='guess_game_over'),
path('reward/', views.reward_page, name='reward_page'),
path('game_results/', views.game_results, name='game_results'),
#listminigame
path('mini-games/', views.mini_game_list, name='mini_game_list'),
path('mini-game/<int:id>/', views.mini_game_detail, name='game_detail'),
path('claim-free-guess/', views.claim_free_guess, name='claim_free_guess'),
]
# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)