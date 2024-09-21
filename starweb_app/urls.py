from django.urls import path
from .views import index_view,products_view,accept_cookies,reject_cookies,cookie_policy,BP_20M_31_28_24_22_pdf_view,BP_20C_20_25_10C20_pdf_view,BP_30M_35_31_28_pdf_view,PC_311W_MC_320F_merged,MC_251FW,BP_30C25Z_BP_30C25ZT,BP_50C26_50C31_50C36_50C45,M_8124cidn,PN_Q901_801_701_6011,PN_HW_751,PN_50TC1,Display_R65_2024_2,R_75_inch,display_r_series_86_inch,viewsonic_all_pdf,epson_all_pdf,panasonic_all_pdf,infocus_all_pdf,benq_all_pdf,optoma_all_pdf,fujitsu_all_pdf,hp_all_pdf


urlpatterns = [
    path('',index_view,name='index-view'),
    path('products/', products_view, name='products-view'),
    path('accept-cookies/', accept_cookies, name='accept_cookies'),
    path('reject-cookies/', reject_cookies, name='reject_cookies'),
    path('cookie-policy/', cookie_policy, name='cookie-policy'),
    
    #Products
    path('BP-20M-31-28-24-22-pdf/', BP_20M_31_28_24_22_pdf_view, name='BP-20M-31-28-24-22-pdf-view'),
    path('BP-20C-20-25-10C20-pdf/', BP_20C_20_25_10C20_pdf_view, name='BP-20C-20-25-10C20-pdf-view'),
    path('BP-30M-35-31-28-pdf/', BP_30M_35_31_28_pdf_view, name='BP-30M-35-31-28-pdf-view'),
    path('PC-311W-MC-320F-merged/', PC_311W_MC_320F_merged, name='PC-311W-MC-320F-merged'),
    path('MC-251FW/', MC_251FW, name='MC-251FW'),
    path('M-2040dn-2540dn-2640idw/', MC_251FW, name='M-2040dn-2540dn-2640idw'),
    path('BP-30C25Z-BP-30C25ZT/', BP_30C25Z_BP_30C25ZT, name='BP-30C25Z-BP-30C25ZT'),
    path('BP-50C26-50C31-50C36-50C45/', BP_50C26_50C31_50C36_50C45, name='BP-50C26-50C31-50C36-50C45'),
    path('M-8124cidn/', M_8124cidn, name='M-8124cidn'),
    path('PN-Q901-801-701-6011/', PN_Q901_801_701_6011, name='PN-Q901-801-701-6011'),
    path('PN-HW-751/', PN_HW_751, name='PN-HW-751'),
    path('PN-50TC1/', PN_50TC1, name='PN-50TC1'),
    path('Display-R65-2024-2/', Display_R65_2024_2, name='Display-R65-2024-2'),
    path('R-75-inch/', R_75_inch, name='R-75-inch'),
    path('display-r-series-86-inch/', display_r_series_86_inch, name='display-r-series-86-inch'),
    

    #Projectors
    path('viewsonic-all-pdf/', viewsonic_all_pdf, name='viewsonic-all-pdf'),
    path('epson-all-pdf/', epson_all_pdf, name='epson-all-pdf'),
    path('panasonic-all-pdf/', panasonic_all_pdf, name='panasonic-all-pdf'),
    path('infocus-all-pdf/', infocus_all_pdf, name='infocus-all-pdf'),
    path('benq-all-pdf/', benq_all_pdf, name='benq-all-pdf'),
    path('optoma-all-pdf/', optoma_all_pdf, name='optoma-all-pdf'),

    #other products
    path('benq-all-pdf/', fujitsu_all_pdf, name='benq-all-pdf'),
    path('hp-all-pdf/', hp_all_pdf, name='hp-all-pdf'),
    
]
