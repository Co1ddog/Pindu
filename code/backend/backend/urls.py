from django.contrib import admin
from django.urls import path

import book.views
import buy.views
import feedback.views
import people.views
import sell.views

urlpatterns = [
    path('admin/', admin.site.urls),

    # people
    path('api/userlist/', people.views.UserList.as_view()),
    path('api/userregister/', people.views.UserRegister.as_view()),
    path('api/userlogin/', people.views.UserLogin.as_view()),
    path('api/useraddress/', people.views.UserAddressListCreate.as_view()),
    # 下面的url：pk=uid并发送get，返回此人的所有记录；pk=useraddressid并发送patch,delete，修改、删除该条记录
    path('api/useraddress/<int:pk>/', people.views.UserAddressRetrieveUpdateDestroy.as_view()),
    path('api/userdetail/<int:pk>/', people.views.UserDetail.as_view()),
    path('api/userchangepassword/', people.views.UserChangePw().as_view()),
    path('api/userverifypw/', people.views.UserPwVerify.as_view()),
    path('api/adminlist/', people.views.AdminListCreate.as_view()),
    path('api/adminlogin/', people.views.AdminLogin.as_view()),

    # book
    path('api/book/', book.views.BookListCreate.as_view()),
    path('api/book/<int:isbn>/', book.views.BookRetrieveUpdateDestroy.as_view()),
    path('api/bookisflow/', book.views.BookIsFlowList.as_view()),
    # shop的精髓之处
    path('api/bookcatepresspricesearch/<str:pk>/<str:qk>/<str:ok>/<str:rk>/<str:sk>/',
         book.views.BookRetrieveByCatePressPriceSearch.as_view()),
    path('api/bookcate/<str:pk>/<str:qk>/<str:ok>/<str:rk>/<str:sk>/',
         book.views.BookCategoryListByCatePressPriceSearch.as_view()),
    path('api/bookpress/<str:pk>/<str:qk>/<str:ok>/<str:rk>/<str:sk>/',
         book.views.BookPresshouseListByCatePressPriceSearch.as_view()),

    # conditionrate
    path('api/conditionrate/', book.views.ConditionRateListCreate.as_view()),
    path('api/conditionrate/<int:pk>/', book.views.ConditionRateRetreiveUpdateDelete.as_view()),

    # inventory
    path('api/inventory/', book.views.InventoryListCreate.as_view()),
    path('api/inventory/<int:pk>/', book.views.InventoryRetrieveUpdateDestroy.as_view()),
    path('api/inventorydetail/<int:pk>/', book.views.InventoryDetailRetrieve.as_view()),

    # cart
    path('api/cart/', buy.views.CartListCreate.as_view()),
    # get方法时pk为uid，patch、delete方法时pk为自增id
    path('api/cart/<int:pk>/', buy.views.CartRetrieveUpdateDestory.as_view()),
    # 购物车减少一件
    path('api/cartminus/', buy.views.CartMinus.as_view()),
    # 获得一个用户的一个inventory的数量
    path('api/cartinventorynum/<int:pk>/<int:qk>/<str:ok>/', buy.views.CartInventoryNumRetrieve.as_view()),

    # sell
    path('api/warehouse/', sell.views.WarehouseListCreate.as_view()),
    path('api/warehouse/<int:pk>/', sell.views.WarehouseRetrieveDestroy.as_view()),
    path('api/warehouse/uid=<int:pk>/', sell.views.WarehouseOfUserRetrieve.as_view()),

    # buy_order
    path('api/buyorder/', buy.views.BuyOrderListCreate.as_view()),
    path('api/buyorder/<int:pk>/', buy.views.BuyOrderRetrieveUpdateDelete.as_view()),
    # buyorderdetail
    path('api/buyorderdetail/', buy.views.BuyOrderDetailListCreate.as_view()),
    path('api/buyorderdetail/<int:pk>/', buy.views.BuyOrderDetailRetrieveUpdateDestory.as_view()),

    # sellorder
    path('api/sellorder/', sell.views.SellOrderListCreate.as_view()),
    path('api/sellorder/<int:pk>/', sell.views.SellOrderRetrieveUpdateDestroy.as_view()),
    path('api/sellorder/status=<int:pk>/', sell.views.SellOrderStatusList.as_view()),
    # sellorderdetail
    path('api/sellorderdetail/', sell.views.SellOrderDetailListCreate.as_view()),
    path('api/sellorderdetail/<int:pk>/', sell.views.SellOrderDetailRetrieveUpdateDestroy.as_view()),
    path('api/sellorderdetailpatch/<int:pk>/', sell.views.SellOrderDetailPatch.as_view()),

    # feedback 这两个是for user
    path('api/feedback/', feedback.views.FeedbackListCreate.as_view()),
    # # GET方法时pk=uid，返回此用户的所有历史问题，包括问题和回复及处理状态
    path('api/feedback/<int:pk>/', feedback.views.FeedbackRetrieveUpdateDestroy.as_view()),
    path('api/feedbackpending/', feedback.views.FeedbackListPending.as_view()),
    path('api/feedbackpendingfromasset/', feedback.views.FeedbackListPendingFromAsset.as_view()),
    path('api/feedbackfromaftersale/', feedback.views.FeedbackListFromAftersale.as_view()),
    path('api/feedbackpendingfromaftersale/', feedback.views.FeedbackListPendingFromAftersale.as_view()),

]
