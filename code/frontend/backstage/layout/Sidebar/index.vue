<template>
  <div :class="{ 'has-logo': themeConfig.showLogo }">
    <logo :isCollapse="isCollapse" v-if="themeConfig.showLogo" />
    <el-scrollbar wrap-class="scrollbar-wrapper">
      <u-menu />
    </el-scrollbar>
  </div>
</template>

<script lang="ts" setup>
  import UMenu from './components/Menu.vue'
  import logo from './components/Logo.vue'
  import { useSettingStore } from '@/store/modules/setting'
  import { computed } from 'vue'

  const SettingStore = useSettingStore()
  // 是否折叠
  const isCollapse = computed(() => !SettingStore.isCollapse)
  // 设置
  const themeConfig = computed(() => SettingStore.themeConfig)
</script>

<style lang="scss">
  .el-menu-vertical-demo:not(.el-menu--collapse) {
    //width: 200px;
    height: 100%;
  }
  .crollbar-wrapper {
    height: 100%;
    .el-scrollbar__view {
      height: 100%;
    }
  }
</style>
