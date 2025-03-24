/** When your routing table is too long, you can split it into small modules**/

import Layout from "@/layout/index.vue";

const bookmanRouter = [{
    path: '/book_list',
    component: Layout,
    redirect: '/book_list/all_records',
    // name: 'aftersaleman',
    meta: {
        title: '平台图书库',
        icon: 'School',
        roles: ['bookman']
    },
    children: [
        {
            // 大大大大大坑！子路由的name不能和其他组件的重复
            path: 'book',
            component: () => import('@/views/bookman/tablemodel.vue'),
            // name: 'all_records',
            meta: {title: '图书库', keepAlive: true, icon: 'MenuIcon', roles: ['bookman']}
        },
    ]
}]

export default bookmanRouter
