/** When your routing table is too long, you can split it into small modules**/

import Layout from "@/layout/index.vue";

const assetmanRouter = [{
    path: '/aftersaleman_question_list',
    component: Layout,
    redirect: '/aftersaleman_question_list/all_records',
    meta: {
        title: '售后人员问题列表',
        icon: 'School',
        roles: ['assetman']
    },
    children: [
        {
            // 大大大大大坑！子路由的name不能和其他组件的重复
            path: 'all_records',
            component: () => import('@/views/assetman/aftersalemanQuestionList/allRecords.vue'),
            // name: 'all_records',
            meta: {
                title: '所有问题列表', keepAlive: true, icon: 'MenuIcon', roles: ['assetman']
            }
        },
        {
            // 大大大大大坑！子路由的name不能和其他组件的重复
            path: 'pending_records',
            component: () => import('@/views/assetman/aftersalemanQuestionList/pendingRecords.vue'),
            // name: 'pending',
            meta: {title: '待处理问题列表', keepAlive: true, icon: 'MenuIcon', roles: ['assetman']}
        },
    ]
}]

export default assetmanRouter
