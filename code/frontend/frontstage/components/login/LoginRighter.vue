<template>
  <div style="width: 100%; height: 90%;display: flex;align-items: center;justify-content: center;">

    <div style="">
      <form style="float: right">
        <h3>账号：</h3>
        <input type="text" v-model="username">
        <h3>密码：</h3>
        <input type="password" v-model="password">
        <br>

        <div style="display: flex; align-items: center; justify-content: space-between;  padding-top: 10px">
          <RouterLink :to="{name: 'register'}" style="color: lightsteelblue; float: left; text-decoration-line: none">
            注册
          </RouterLink>
          <button type="button" @click="login">登陆</button>
        </div>
      </form>
    </div>

  </div>

</template>

<script setup>
import {onBeforeUpdate, ref} from "vue";
import loginService from "@/api/loginService";
import {useRoute, useRouter} from "vue-router";

const router = useRouter()
const route = useRoute()

const username = ref('')
const password = ref('')

const login = () => {
  loginService.Login(username.value, password.value).then((r) => {
    // localStorage 里面存储的数据没有过期时间设置，而存储在 sessionStorage 里面的数据在页面会话结束时会被清除。
    window.sessionStorage.setItem("token", r.data.token);
    window.sessionStorage.setItem("id", r.data.user_id);
    console.log(r.data)
    // console.log(window.sessionStorage)
    window.location.reload()
    // alert("login!\n" + "token: " + r.data.token + "\nuser id: " + r.data.user_id)

  }).catch((err) => {
    console.error(err);
    // 可以使用友好的提示方式告诉用户信息输入有误等问题
    alert("登录失败，请检查您输入的用户名和密码是否正确！");
  })
  // router.push('/information/self/')
  router.push('/')
}

</script>

<style scoped>

</style>