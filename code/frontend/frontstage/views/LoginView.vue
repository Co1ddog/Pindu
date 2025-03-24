<template>
  <div style="height: 650px;">
    <n-grid x-gap="0" cols="11" style="height: 100%">
      <n-gi span="7">
        <div class="huanying"
             style="">
          <h1 style="font-weight: bolder; font-size: 150px; color: white;text-shadow: 0 0 5px white,0 0 30px #f469a9,0 0 20px #f469a9,0 0 20px white;">
            欢迎登录</h1>
          <!--          <img src="../assets/WechatIMG3519.jpeg" alt="" style="height: 650px; width: ">-->
        </div>
      </n-gi>
      <n-gi span="4">
        <RouterView>

        </RouterView>
      </n-gi>
    </n-grid>
  </div>
</template>

<script setup>

</script>

<style type="css/text">
h1, h3 {
  color: white;
}

.huanying {
  width: 100%;
  height: 100%;
  /*background-color: #2c3e50;*/
  background-image: url(../assets/WechatIMG3519.jpeg);
  background-size: 100% 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

</style>