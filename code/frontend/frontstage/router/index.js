import {createRouter, createWebHistory} from 'vue-router'
// 1. 导入路由组件
import HomeView from '@/views/HomeView.vue'
import ShopView from "@/views/ShopView.vue";
import BookCaseView from "@/views/BookCaseView.vue";
import CartView from "@/views/CartView.vue";
import WareHouseView from "@/views/WareHouseView.vue";
import LoginView from "@/views/LoginView.vue";
import RegisterRighter from "@/components/login/RegisterRighter.vue";
import LoginRighter from "@/components/login/LoginRighter.vue";
import PurchaseCheckView from "@/views/PurchaseCheckView.vue";
import SellCheckView from "@/views/SellCheckView.vue";
import UserInformation from "@/views/UserInformation.vue";
import Self from "@/components/userinformation/Self.vue";
import Address from "@/components/userinformation/Address.vue";
import Wallet from "@/components/userinformation/Wallet.vue";
import Notification from "@/components/userinformation/Notification.vue"
import SelledBook from "@/components/myorder/SelledBook.vue";
import BoughtBook from "@/components/myorder/BoughtBook.vue";
import Setting from "@/components/myorder/Setting.vue";
import BookInfo from "@/views/BookInfo.vue";
import ChangeSelf from "../components/userinformation/ChangeSelf.vue";
// import Boughtorder from "../components/orderinfo/Boughtorder.vue";
// import Soldorder from "../components/orderinfo/Soldorder.vue"
import Boughtorderinfo from "@/views/BoughtorderInfo.vue";
import Soldorderinfo from "@/views/Soldorderinfo.vue";
import sellorderinfo from "@/views/Sellorderinfo.vue";
import Buyorderinfo from "@/views/Buyorderinfo.vue";
import sellorder from "@/components/orderinfo/sellorder.vue";
import Buyorder from "@/components/orderinfo/Buyorder.vue";


// 2. 创建路由实例并传递 `routes` 配置
const router = createRouter({
    // 4. 内部提供了 history 模式的实现。
    history: createWebHistory(),
    // 3. 定义一些路由，每个路由都需要映射到一个组件。
    // 默认情况下，所有路由是不区分大小写的，并且能匹配带有或不带有尾部斜线的路由。
    // 例如，路由 /users 将匹配 /users、/users/、甚至 /Users/。
    // 这种行为可以通过 strict 和 sensitive 选项来修改
    routes: [

        {
            path: '/',
            name: 'home',
            component: HomeView
        },
        {
            path: '/shop/',
            name: 'shop',
            component: ShopView,
        },
        {
            path: "/bookinfo/:isbn",
            name: 'bookinfo',
            component: BookInfo
        },
        // {
        //     path: "/boughtorder/",
        //     name: 'boughtorder',
        //     component: Boughtorder
        // },
        // {
        //     path: "/soldorder/",
        //     name: 'soldorder',
        //     component: Soldorder
        // },
        {
            path:"/sellorder/",
            name:'sellorder',
            component: sellorder
        },
          {
            path:"/Buyorder/",
            name:'Buyorder',
            component: Buyorder
        },
        {
            path: "/bookcase/",
            name: 'bookcase',
            component: BookCaseView
        },
        {
            path: '/cart/',
            name: 'cart',
            component: CartView
        },
        {
            path: '/warehouse/',
            name: 'warehouse',
            component: WareHouseView
        },
        {
            path: '/purchasecheck/',
            name: 'purchasecheck',
            component: PurchaseCheckView
        },
        {
            path: '/sellcheck/',
            name: 'sellcheck',
            component: SellCheckView
        },
        {

            path: '/boughtorderinfo/:oid',
            name: 'boughtorderinfo',
            component: Boughtorderinfo
        },
        {

            path: '/soldorderinfo/:oid',
            name: 'soldorderinfo',
            component: Soldorderinfo,

        },
        {
            path: '/sellorderinfo/',
            name: 'sellorderinfo',
            component: sellorderinfo
        },
        {
            path: '/Buyorderinfo/',
            name: 'Buyorderinfo',
            component: Buyorderinfo
        },
        {
            path: '/login/',
            name: 'login',
            component: LoginView,
            children: [{
                path: 'register/',
                name: 'register',
                component: RegisterRighter
            },
                {
                    path: '',
                    component: LoginRighter
                }
            ]

        },
        {
            path: '/information/',
            name: 'information',
            component: UserInformation,

            children: [
                {
                    path: 'self/',
                    name: 'self',
                    component: Self,
                },
                {
                    path: 'address/',
                    name: 'address',
                    component: Address,
                },
                {
                    path: 'wallet/',
                    name: 'wallet',
                    component: Wallet,
                },
                {
                    path: 'notification/',
                    name: 'notification',
                    component: Notification,
                },
                {
                    path: 'boughtbook/',
                    name: 'boughtbook',
                    component: BoughtBook,
                },
                {
                    path: 'selledbook/',
                    name: 'selledbook',
                    component: SelledBook,
                },
                {
                    path: 'setting/',
                    name: 'setting',
                    component: Setting,
                },
                {
                    path: 'changeself/',
                    name: 'changeself',
                    component: ChangeSelf
                }
            ]
        },
// {
//     path: '/about',
//     name: 'about',
//     // route level code-splitting
//     // this generates a separate chunk (About.[hash].js) for this route
//     // which is lazy-loaded when the route is visited.
//     component: () => import('../views/AboutView.vue')
// }
    ],
})
router.beforeEach((to, from, next) => {
    // to => 将要访问的页面
    // from => 代表从哪个路径跳转而来
    // next=>是否放行 next()放行 next('/login')强制跳转到/login

    ///login直接放行
    // const allowed_path = ['/', '/login', '/login/register', '/register']

    if (to.path === '/' || to.path === '/login/' || to.path === '/login/register/' || to.path === '/shop/')
        return next()

    //其它判断是否有token
    const tokenstr = window.sessionStorage.getItem('token')

    if (tokenstr === null)
        return next('/login/')
    next()
})

export default router
