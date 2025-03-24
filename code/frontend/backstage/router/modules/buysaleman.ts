/** When your routing table is too long, you can split it into small modules**/

import Layout from "@/layout/index.vue";

const buysalemanRouter = [
    {
    path: '/buysaleman',
    component: Layout,
    redirect: '/buysaleman/buyorderinfo',
    meta: {
        title: '买书/卖书订单',
        icon: 'School',
        roles: ['buysaleman']
    },
    children: [
        {
            // 大大大大大坑！子路由的name不能和其他组件的重复
            path: 'buyorderinfo',
            component: () => import('@/views/buysaleman/buyorderinfo/index.vue'),
            // name: 'all_records',
            meta: {title: '平台买书订单', keepAlive: true, icon: 'MenuIcon', roles: ['buysaleman']}
        },
        {
            // 大大大大大坑！子路由的name不能和其他组件的重复
            path: 'saleorderinfo',
            component: () => import('@/views/buysaleman/saleorderinfo/index.vue'),
            // name: 'pending',
            meta: {title: '平台卖书订单', keepAlive: true, icon: 'MenuIcon', roles: ['buysaleman']}
        },
    ]
},
    {
        path: '/buysaleman9',
        component: Layout,
        redirect: '/buysaleman9/send',
        meta: {
            title: '购售专员',
            icon: 'School',
            roles: ['buysaleman']
        },
        children: [
            {
                // 大大大大大坑！子路由的name不能和其他组件的重复
                path: 'send',
                component: () => import('@/views/buysaleman/send/send.vue'),
                // name: 'all_records',
                meta: {title: '发货', keepAlive: true, icon: 'MenuIcon', roles: ['buysaleman']}
            },
        ]
    },
    {
        path: '/buysaleman8',
        component: Layout,
        redirect: '/buysaleman8/rules',
        meta: {
            title: '购售专员',
            icon: 'School',
            roles: ['buysaleman']
        },
        children: [
            {
                // 大大大大大坑！子路由的name不能和其他组件的重复
                path: 'rules',
                component: () => import('@/views/buysaleman/rules/index.vue'),
                // name: 'pending',
                meta: {title: '修改价格比率', keepAlive: true, icon: 'MenuIcon', roles: ['buysaleman']}
            },
        ]
    },
    {
        path: '/buysaleman1',
        component: Layout,
        redirect: '/buysaleman1/all_orders',
        meta: {
            title: '订单信息',
            icon: 'School',
            roles: ['buysaleman'],
        },
        children: [
            {
                // 大大大大大坑！子路由的name不能和其他组件的重复
                path: 'all_orders',
                component: () => import('@/views/buysaleman/buysellmanOrderList/allOrders.vue'),
                // name: 'all_records',
                meta: {
                    title: '全部订单信息',
                    keepAlive: true,
                    icon: 'MenuIcon',
                    roles: ['buysaleman'],
                },
            },
            {
                // 大大大大大坑！子路由的name不能和其他组件的重复
                path: 'uncheck_orders',
                component: () => import('@/views/buysaleman/buysellmanOrderList/uncheckOrders.vue'),
                // name: 'pending',
                meta: {title: '未审核订单', keepAlive: true, icon: 'MenuIcon', roles: ['buysaleman']},
            },
            {
                // 大大大大大坑！子路由的name不能和其他组件的重复
                path: 'checked_orders',
                component: () => import('@/views/buysaleman/buysellmanOrderList/checkedOrders.vue'),
                // name: 'pending',
                meta: {title: '已审核订单', keepAlive: true, icon: 'MenuIcon', roles: ['buysaleman']},
            },
            {
                // 大大大大大坑！子路由的name不能和其他组件的重复
                path: 'check_work',
                component: () => import('@/views/buysaleman/buysellmanOrderList/checkWork.vue'),
                name: 'checkwork',
                hidden: true,
                meta: {title: '审核订单', keepAlive: true, icon: 'MenuIcon', roles: ['buysaleman']},
            },
        ]
    }
]

export default buysalemanRouter
