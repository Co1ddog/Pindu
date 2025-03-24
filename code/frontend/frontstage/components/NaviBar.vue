<template>
  <div id="t">
    <n-space align="center" justify="space-between">
      <n-space align="center">
        <RouterLink to="/" class="routerlink">
          <n-button text size="large" style="width: 55px;height: 55px;padding-left: 10px;padding-right: 10px">
            <img src="../assets/logo.png" alt="logo" width="55" height="55" style="padding-top: 7px">
          </n-button>
        </RouterLink>
        <RouterLink to="/shop/" class="routerlink">
          <n-button text color="white" size="medium" style="font-size: large;font-weight: bolder;width: 60px"><p>
            商店</p>
          </n-button>
        </RouterLink>
        <!--        <RouterLink to="/bookcase" class="routerlink">-->
        <!--          <n-button text color="white" size="medium" style="font-size: large;width: 60px">书柜</n-button>-->
        <!--        </RouterLink>-->
      </n-space>

      <n-space align="center" style="padding-right: 20px">
<!--        <div-->
<!--            style="padding: 3px 10px; background-color: cornflowerblue; display: flex; align-items: center; justify-content: center;">-->
<!--          <h2 style="color: #FFFFFF; padding-right: 10px">临时</h2>-->
<!--          <el-button plain type="danger" @click="alert_token">TOKEN</el-button>-->
<!--          <RouterLink to="/purchasecheck">-->
<!--            <n-button size="large" style="width: auto; height: 38px; color: white">-->
<!--              PurchaseCheck-->
<!--            </n-button>-->
<!--          </RouterLink>-->
<!--          <RouterLink to="/bookinfo">-->
<!--            <n-button size="large" style="width: auto; height: 38px; color: white">-->
<!--              BookInfo-->
<!--            </n-button>-->
<!--          </RouterLink>-->
<!--          <RouterLink to="/information/self">-->
<!--            <n-button size="large" style="width: auto; height: 38px; color: white">-->
<!--              UserInfo-->
<!--            </n-button>-->
<!--          </RouterLink>-->
<!--        </div>-->

<!--        <n-input size="medium" placeholder="搜索" round style="width: 230px; "/>-->
        <RouterLink to="/cart" class="routerlink">
          <n-button text size="large" style="width: 45px; height: 45px; padding-left: 0">
            <img src="../assets/购物车.png" alt="购物车" width="42" height="42">
          </n-button>
        </RouterLink>
        <RouterLink to="/warehouse" class="routerlink">
          <n-button text size="large" style="width: 45px; height: 45px; padding-left: 0">
            <img src="../assets/卖书柜.png" alt="卖书柜" width="38" height="38">
          </n-button>
        </RouterLink>

        <RouterLink to="/login/" class="routerlink">
          <n-button
              v-if="islogin"
              size="medium"
              style="color: white; background-color: #d53f68">
            登陆/注册
          </n-button>
        </RouterLink>

        <template v-if="islogin === false">
          <RouterLink to="/information/self/">
            <n-button
                size="medium"
                style="color: white; background-color: #d53f68">
              <p style="font-weight: bold">你好，{{ nickname }}</p>
            </n-button>
          </RouterLink>
          <!--          <RouterLink to="/">-->
          <n-button class="logout" quaternary @click="logout" type="default" size="tiny"
                    style="color: #f2f2f2; background-color: #282828;">
            登出
          </n-button>
          <!--          </RouterLink>-->

        </template>


      </n-space>
    </n-space>
  </div>
</template>

<script setup>
import {computed, getCurrentInstance, onMounted, onUpdated, ref, watch} from "vue";
import loginService from "../api/loginService";
import {useRouter} from "vue-router";


const alert_token = () => {
  alert("token: " + window.sessionStorage.getItem('token') + "\nuserid: " + window.sessionStorage.getItem('id'))
}
const islogin = computed(() => {
  if (sessionStorage.getItem('token') == null) {
    return true
  } else {
    return false
  }
})

const nickname = ref()
const uid = window.sessionStorage.getItem('id')
if (uid !== null) {
  loginService.GetUserInformation(uid).then(r => {
    nickname.value = r.data.first_name
    console.log(r.data.username)
  })
}

const router = useRouter()
const logout = async () => {
  window.sessionStorage.clear()
  // 大大大大大大大大坑！！！！！先跳转路由到'/'，再在then里面写reload
  await router.push('/').then(r => location.reload())

}


</script>

<style scoped>
.routerlink {
  text-decoration-line: none;
}

.logout:hover {
  color: red;
}

.n-button:hover {
  color: brown;
}

.n-button:focus {
  color: turquoise;
}

.n-button {
  outline: none;
  border-color: transparent;
  box-shadow: none;
  text-decoration-line: none;
}

#t {
  box-sizing: border-box;
  width: 100%;
  background-color: black;
  /*border: darkgray solid 1px;*/
}
</style>