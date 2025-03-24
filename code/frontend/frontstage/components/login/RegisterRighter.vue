<template>
  <div style="height: 95%; display: flex; align-items: center; justify-content: center">

    <form style="float: right">
      <h3>账号：</h3>
      <input type="text" v-model="username">
      <h3>昵称：</h3>
      <input type="text" v-model="nickname">
      <h3>密码：</h3>
      <input type="password" v-model="password">
      <br>

      <div style="display: flex; align-items: center; justify-content: space-between; padding-top: 10px">
        <RouterLink to="/login/" style="color: white; text-decoration-line: none">
          返回登录
        </RouterLink>
        <button type="button" @click="register">注册</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import {ref} from "vue";
import loginService from "@/api/loginService";
import router from "../../router";
import {useMessage} from "naive-ui";

const username = ref("")
const nickname = ref("")
const password = ref("")

const register = () => {
  console.log(username.value)
  console.log(password.value)

  //校验登录名：只能输入5-20个以字母开头、可带数字的字串
  const pat = /^[a-zA-Z]([a-zA-Z0-9]){4,19}$/;
  //校验密码：只能输入6-20个字母、数字、下划线
  const patrn = /^(\w){6,20}$/
  const r = pat.test(username.value);
  const rpw = patrn.test(password.value)

  console.log(r)
  console.log(rpw)
  if (r != null && rpw != null) {
    if (r && rpw) {
      // 账密合格
      loginService.Register(username.value, password.value, nickname.value).then(r => {
        if (r.data.status === true) {
          alert("注册成功，请登录！")
          router.push('/login/')
        } else {
          // 账号已注册
          username.value = ''
          alert("账号已注册，请更换！")
        }
      })
    } else {
      // 账密格式不对
      alert("账号或密码格式不对。\n账号：5-20位以字母开头、可带数字\n密码：6-20位字母、数字、下划线")
    }
  } else {
    //账密为空
    alert("账号密码不能为空")
  }

}

</script>

<style scoped>

</style>