
/** When your routing table is too long, you can split it into small modules**/

import Layout from "@/layout/index.vue";

const teRouter = [{
    path: '/te',
    component: Layout,
    redirect: '/te/comprehensive',
    // name: 'table',
    meta: {
        title: '超级表格',
        icon: 'School'
    },
    children: [
        {
            path: 'comprehensive',
            component: () => import('@/views/aftersaleman/customerQuestionList/index.vue'),
            name: 'comprehensive',
            meta: { title: 'te', keepAlive: true , icon: 'MenuIcon'}
        },

    ]
}]

export default teRouter
