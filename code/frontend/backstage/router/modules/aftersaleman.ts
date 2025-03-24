/** When your routing table is too long, you can split it into small modules**/

import Layout from "@/layout/index.vue";

const aftersalemanRouter = [{
    path: '/customer_question_list',
    component: Layout,
    redirect: '/customer_question_list/all_records',
    // name: 'aftersaleman',
    meta: {
        title: '客户问题列表',
        icon: 'School',
        roles: ['aftersaleman']
    },
    children: [
        {
            // 大大大大大坑！子路由的name不能和其他组件的重复
            path: 'all_records',
            component: () => import('@/views/aftersaleman/customerQuestionList/allRecords.vue'),
            // name: 'all_records',
            meta: {title: '所有问题列表', keepAlive: true, icon: 'MenuIcon', roles: ['aftersaleman']}
        },
        {
            // 大大大大大坑！子路由的name不能和其他组件的重复
            path: 'pending_records',
            component: () => import('@/views/aftersaleman/customerQuestionList/pendingRecords.vue'),
            // name: 'pending',
            meta: {title: '待处理问题列表', keepAlive: true, icon: 'MenuIcon', roles: ['aftersaleman']}
        },
        {
            // 大大大大大坑！子路由的name不能和其他组件的重复
            path: 'pending_from_assetman_records',
            component: () => import('@/views/aftersaleman/customerQuestionList/pendingFromAssetmanRecords.vue'),
            // name: 'pending',
            meta: {title: '待反馈问题列表', keepAlive: true, icon: 'MenuIcon', roles: ['aftersaleman']}
        },
    ]
}]

export default aftersalemanRouter
