from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
  # seller side
    
    path("seller-indexpage/",views.SellerIndexpage,name="index"),
    path("seller-register-page/",views.sellerregisterpage,name="registerpage"),
    path("seller/",views.Sellerloginpage,name="login"),
    path("register-seller/",views.regseller,name="registerseller"),
    path("login-seller/",views.LogSeller,name="loginseller"),
    path("sellerforgetpass/",views.sellerForgetpass,name="forgotpassword"),
    # path("selleraddproduct/",views.selleraddproduct,name="addproduct"),
    
    path("sellerlogout-page/",views.Logout,name='logout'),
    path("selleremailverify/",views.EmailVerificationPage,name="email-verify"),
    path("sellerOtpverify/",views.OTP_verify,name="OtpSverify"),
    path("sellerchanepass/",views.ChangePassword,name="changepassword"),
    path("sellerallproducts/",views.AllProduct,name="allproduct"),
    path("sellerproductadd/",views.addpro,name="productadd"),
    path("selleraddproduct/",views.selleraddproduct,name="addproduct"),

    path("seller-myprofile/",views.Sellermyprofile,name="sellermyprofile"),
    path("sellerupdateprofile/",views.s_updateprofile,name="Supdateprofile"),

    path("sellerdelete/<int:pk>",views.sellerdelete,name="sellerdelete"),

    path("sellerorder/",views.sellerorder,name="sellerorder"),

#user side
  
    
    path("",views.uIndexpage,name="uindex"),
    # path('userhomepage',views.userhome,name="uhome"),
    path("userregister/",views.uRegisterpage,name="uregister"),
    path("userlogin",views.uLoginpage,name="ulogin"),
    path("userforgetpas/",views.uForgetpass,name="uforgetpas"),


    # path("useraddcart/",views.uaddcart,name="uaddcart"),
    path("useraddcart/<int:pk>/",views.useraddcart,name="uaddcart"),

    path("userviewcart/",views.uViewcart,name="uviewcart"),
    path("usercheckout/",views.uCheckout,name="usercheckout"),
    path("userremoveproduct/<int:pk>",views.userremove,name="uremovepro"),

    path("userupdatecart/",views.updatecart,name="uupdatecart"),

    path("usermyprofile/",views.usermyprofilePage,name="umyprofile"),
    path("userupadateprofile/",views.u_updateprofile,name="uupdateprofile"),

    path("login-user/",views.uLoguser,name="loginuser"),
    path("register-user/",views.uReguser,name="registeruser"),
    path("useremailverify/",views.uEmailVerificationPage,name="useremail-verify"),
    path("userOtpverify/",views.uOtpverify,name="Otpverify"),
    path("userchangepass/",views.uChangepassword,name="uchangepass"),
    path("userlogout/",views.uLogout,name='userlogout'),
    # path("userallproduct/",views.uAllproduct,name="uallproduct"),
    
    
    
   

  path('pay/',views.pay,name='pay'),


]