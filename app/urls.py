# Create your urls here.
from django.conf.urls import patterns, include, url
# -*- encoding: utf-8 -*-
from . import views

urlpatterns = [
    url(r'^$', views.login_view, name='app.login'),
    url(r'^buscar/$', views.search, name='app.search'),
    url(r'^dashboard/$', views.welcome_view, name='app.welcome'),
    url(r'^signup/$', views.signup_view, name='app.signup'),
    url(r'^login/$', views.logins_view, name='app.logins'),
    url(r'^inkacoin/$', views.inka_view, name='app.inka'),
    url(r'^nosotros/$', views.us_view, name='app.us'),
    url(r'^f_updateavatar/$', views.f_updateavatar, name='app.f_updateavatar'),
    url(r'^f_uploadtrack/$', views.f_uploadtrack, name='app.f_uploadtrack'),
    url(r'^app/$', views.app_view, name='app.app'),
    url(r'^documentacion-api/$', views.tasks_view, name='app.tasks'),
    url(r'^empresas/$', views.companies_view, name='app.companies'),
    url(r'^temas/$', views.categories_view, name='app.categories'),
    url(r'^temas/(?P<slug>[^\.]+)/$', views.category_view, name='app.category'),
    url(r'^blog/$', views.blogs_view, name='app.blogs'),
    url(r'^blog/(?P<slug>[^\.]+)/$', views.blog_view, name='app.blog'),
    url(r'^eventos/$', views.dates_view, name='app.dates'),
    url(r'^mercado-inkacoin/$', views.products_view, name='app.products'),
    url(r'^tienda/(?P<slug>[^\.]+)/$', views.product_view, name='app.product'),
    url(r'^pagos/$', views.payments_view, name='app.payments'),
    url(r'^pago/(?P<slug>[^\.]+)/$', views.payment_view, name='app.payment'),
    url(r'^cart/$', views.cart_view, name='app.cart'),
    url(r'^confirmando/$', views.confirmbuy_view, name='app.confirmbuy'),
    url(r'^addcart/(?P<slug>[^\.]+)/$', views.addcart_view, name='app.addcart'),
    url(r'^addowner/(?P<slug>[^\.]+)/$', views.addowner_view, name='app.addowner'),
    url(r'^ownerready/$', views.ownerready_view, name='app.ownerready'),
    url(r'^miscompras/$', views.owners_view, name='app.owners'),
    url(r'^deletecart/(?P<slug>[^\.]+)/$', views.deletecart_view, name='app.deletecart'),
    url(r'^buyment/$', views.buyment_view, name='app.buyment'),
    url(r'^confirmar-pagos/$', views.paymentc_view, name='app.paymentc'),
    url(r'^addbuyment/$', views.addbuyment_view, name='app.addbuyment'),
    url(r'^salir/$', views.logout_view, name='app.logout'),
    url(r'^nuevo-audio/$', views.uploadtrack_view, name='app.uploadtrack'),
    url(r'^audios/(?P<slug>[^\.]+)/$', views.track_view, name='app.track'),
    url(r'^publicar/$', views.createblog_view, name='app.createblog'),
    url(r'^@/(?P<slug>[^\.]+)/$', views.userprofile_view, name='app.userprofile'),
    url(r'^actualizar/foto-perfil/(?P<slug>[^\.]+)/$', views.updateavatar_view, name='app.updateavatar'),
    url(r'^actualizar/nombre-usuario/(?P<slug>[^\.]+)/$', views.updatenickname_view, name='app.updatenickname'),
    url(r'^actualizar/miembro-color-a/(?P<slug>[^\.]+)/$', views.updatecolora_view, name='app.colora'),
    url(r'^actualizar/miembro-color-b/(?P<slug>[^\.]+)/$', views.updatecolorb_view, name='app.colorb'),
    url(r'^actualizar/miembro-color-c/(?P<slug>[^\.]+)/$', views.updatecolorc_view, name='app.colorc'),
    url(r'^actualizar/miembro-color-d/(?P<slug>[^\.]+)/$', views.updatecolord_view, name='app.colord'),
    url(r'^actualizar/miembro-color-e/(?P<slug>[^\.]+)/$', views.updatecolore_view, name='app.colore'),
    url(r'^actualizar/miembro-color-f/(?P<slug>[^\.]+)/$', views.updatecolorf_view, name='app.colorf'),
    url(r'^actualizar/miembro-color-g/(?P<slug>[^\.]+)/$', views.updatecolorg_view, name='app.colorg'),
    url(r'^actualizar/miembro-color-h/(?P<slug>[^\.]+)/$', views.updatecolorh_view, name='app.colorh'),
    url(r'^actualizar/miembro-color-i/(?P<slug>[^\.]+)/$', views.updatecolori_view, name='app.colori'),
    url(r'^actualizar/miembro-color-j/(?P<slug>[^\.]+)/$', views.updatecolorj_view, name='app.colorj'),
    url(r'^actualizar/miembro-color-k/(?P<slug>[^\.]+)/$', views.updatecolork_view, name='app.colork'),
    url(r'^actualizar/miembro-color-l/(?P<slug>[^\.]+)/$', views.updatecolorl_view, name='app.colorl'),
    # API REST 
    url(r'^api/tracks', views.TracksApi.as_view(), name='api-tracks'),
    url(r'^api/device', views.device, name='api-device'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # APP 
    url(r'^app/eventos$', views.dates_app, name='app.dates_app'),
    url(r'^app/loading$', views.loading_app, name='app.loading_app'),
    url(r'^app/charges$', views.charge_app, name='app.charge_app'),
    url(r'^charge/(?P<userid>[^\.]+)/(?P<monto>[^\.]+)/$', views.monto_app, name='app.monto_app'),
    url(r'^ikc/(?P<currency>[^\.]+)/$', views.ikc_app, name='app.ikc_app'),
    url(r'^ikcdown/(?P<bajada>[^\.]+)/$', views.ikcdown_app, name='app.ikcdown_app'),
    url(r'^ikcup/(?P<subida>[^\.]+)/$', views.ikcup_app, name='app.ikcup_app'),
    url(r'^addfriends/(?P<userid>[^\.]+)/$', views.addfriends_app, name='app.addfriends_app'),
    url(r'^addfriend/$', views.addfriend_view, name='app.addfriend_view'),
    url(r'^friends/$', views.friends_view, name='app.friends_view'),
###################################################################################
###########################################################################
############################################################################
###########################################################################
# PROYECTO UVAS 2.0
    url(r'^academy/$', views.academy, name='app.academy'),

]