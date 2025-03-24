<template>
  <div style="background-color: #282828">
    <n-grid x-gap="0" y-gap="0" cols="10">
      <n-gi span="3" style="padding: 25px 25px 0;color: white">
        <n-h3 style="color: #f2f2f2; font-weight: bold">GLOBALink | Trump charged with 34 counts of falsifying business
          records, pleads not guilty
        </n-h3>
        <p>Former U.S. President Donald Trump is charged with 34 counts of falsifying business records, the Manhattan
          district attorney said on Tuesday. Trump, who was arraigned at the Manhattan Criminal Court in New York City,
          reportedly pleaded not guilty.</p>
      </n-gi>
      <n-gi span="7" style="height: auto;padding: 0">
        <div class="box" style="width: 100%; overflow: hidden">
          <div class="imgList" style="display: flex;height:270px;width: 100%">
            <img src="../../assets/pictures/sample6.jpg" alt="s6">
<!--            <img :src="pic" alt="asd">-->
            <!--            <el-image :src=pic />-->
            <img src="../../assets/pictures/sample6.jpg" alt="s5" style="transform: rotateY(180deg)">
            <img src="../../assets/pictures/sample6.jpg" alt="s5">
          </div>
        </div>
      </n-gi>
    </n-grid>
  </div>
</template>

<script setup>
// import {ref} from "vue";
//
// const pic = ref("@//src/assets/卖书柜.png")
// console.log(pic.value)
</script>

<style scoped>
p {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 5;
  overflow: hidden;
}

img {
  flex: 1;
}
</style>