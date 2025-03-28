import {createRouter, createWebHashHistory, RouteRecordRaw} from 'vue-router'
import Layout from "@/layout/index.vue";
//
import aftersalemanRouter from "./modules/aftersaleman";
import assetmanRouter from "./modules/assetman";
import bookmanRouter from "./modules/bookman";
import buysalemanRouter from "./modules/buysaleman";
import buysellmanRouter from "./modules/buysellman";


// 扩展继承属性
interface extendRoute {
    hidden?: boolean
}

// 异步组件
export const asyncRoutes = [
    ...aftersalemanRouter,
    ...assetmanRouter,
    ...bookmanRouter,
    ...buysalemanRouter,
    // ...buysellmanRouter,
]

/**
 * path ==> 路由路径
 * name ==> 路由名称
 * component ==> 路由组件
 * redirect ==> 路由重定向
 * alwaysShow ==> 如果设置为true，将始终显示根菜单，无论其子路由长度如何
 * hidden ==> 如果“hidden:true”不会显示在侧边栏中（默认值为false）
 * keepAlive ==> 设为true 缓存
 * meta ==> 路由元信息
 * meta.title ==> 路由标题
 * meta.icon ==> 菜单icon
 * meta.affix ==> 如果设置为true将会出现在 标签栏中
 * meta.breadcrumb ==> 如果设置为false，该项将隐藏在breadcrumb中（默认值为true）
 */

export const constantRoutes: Array<RouteRecordRaw & extendRoute> = [
    {
        path: '/login',
        name: 'Login',
        component: () => import('@/views/login/index.vue'),
        hidden: true,
        meta: {title: '登录',}
    },
    {
        path: '/',
        name: 'layout',
        component: Layout,
        redirect: '/home',
        children: [
            {
                path: '/home',
                component: () => import('@/views/home/index.vue'),
                name: 'home',
                meta: {title: '首页', icon: 'House', affix: true, role: ['other']}
            },
        ]
    },
]

const router = createRouter({
    // history: createWebHistory(process.env.BASE_URL), // history
    history: createWebHashHistory('/vue-admin-simple/'), // hash
    routes: constantRoutes
})

export default router
