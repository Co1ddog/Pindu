<template>
  <div class="common-layout" style="height: 650px">
    <el-container style="background: black; height: 100%; width: 100%">
      <Aside />
      <el-main>
        <router-view />
      </el-main>
    </el-container>
  </div>
</template>


<script lang="ts" setup>
import {
  Setting,
} from '@element-plus/icons-vue'
import Aside from "../components/userinformation/Aside.vue";

const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}


</script>

<style scoped>

</style>