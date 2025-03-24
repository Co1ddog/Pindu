import {defineStore} from 'pinia'
import {login} from "../../api/user";


export const useUserStore = defineStore({
    // id: 必须的，在所有 Store 中唯一
    id: 'userState',
    // state: 返回对象的函数
    state: () => ({
        // 登录token
        token: null,
        // 登录用户信息
        userInfo: {},
        // 角色
        roles: [],
        id: null,
        name: '',
        level: null
    }),
    getters: {},
    // 可以同步 也可以异步
    actions: {
        // 登录
        async login(userInfo) {
            const {username, password} = userInfo
            let level = null
            await login(userInfo).then(r => {
                if (r.data.status === true) {
                    level = r.data.level
                    this.id = r.data.admin_id
                    this.name = r.data.name
                }
            })
            console.log("outer:", level)
            return new Promise(async (resolve, reject) => {
                this.level = level
                console.log('this.id', this.id)
                this.token = username
                this.userInfo = userInfo
                await this.getRoles()
                resolve(username)
            })
        },
        // 获取用户授权角色信息，实际应用中 可以通过token通过请求接口在这里获取用户信息
        getRoles() {
            if (this.level === 1) {
                return new Promise((resolve, reject) => {
                    // 获取权限列表 默认就是超级管理员，因为没有进行接口请求 写死
                    this.roles = ['aftersaleman']
                    resolve(this.roles)
                })
            }
            if (this.level === 2) {
                return new Promise((resolve, reject) => {
                    // 获取权限列表 默认就是超级管理员，因为没有进行接口请求 写死
                    this.roles = ['assetman']
                    resolve(this.roles)
                })
            }
            if (this.level === 3) {
                return new Promise((resolve, reject) => {
                    // 获取权限列表 默认就是超级管理员，因为没有进行接口请求 写死
                    this.roles = ['buysaleman']
                    resolve(this.roles)
                })
            }

            if (this.level === 4) {
                return new Promise((resolve, reject) => {
                    // 获取权限列表 默认就是超级管理员，因为没有进行接口请求 写死
                    this.roles = ['bookman']
                    resolve(this.roles)
                })
            }

            // return new Promise((resolve, reject) => {
            //     // 获取权限列表 默认就是超级管理员，因为没有进行接口请求 写死
            //     this.roles = ['admin']
            //     resolve(this.roles)
            // })
        },
        // 获取用户信息 ，如实际应用中 可以通过token通过请求接口在这里获取用户信息
        getInfo(roles) {
            return new Promise((resolve, reject) => {
                this.roles = roles
                resolve(roles)
            })
        },
        // 退出
        logout() {
            return new Promise((resolve, reject) => {
                this.token = null
                this.userInfo = {}
                this.roles = []
                resolve(null)
            })
        },

    },
    // 进行持久化存储
    persist: {
        // 本地存储的名称
        key: "userState",
        //保存的位置
        storage: window.sessionStorage,//localstorage
    },

})
