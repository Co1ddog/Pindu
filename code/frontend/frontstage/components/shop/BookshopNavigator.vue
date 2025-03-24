<template>
  <div style="height: 70px;width: 100%; display: flex; align-items: center; justify-content: center">
    <div style="width: 90%; height: 100%;background-color: white; padding: 12px 20px;color: white">
      <h1 style="font-weight: bolder; color: black; padding-bottom: 8px">品读 · 商店</h1>

<!--      <el-breadcrumb separator=">" >-->
<!--        <el-breadcrumb-item :to="{ path: '/shop' }">商店</el-breadcrumb-item>-->
<!--        <el-breadcrumb-item>promotion management</el-breadcrumb-item>-->
<!--        <el-breadcrumb-item>promotion list</el-breadcrumb-item>-->
<!--        <el-breadcrumb-item>promotion detail</el-breadcrumb-item>-->
<!--      </el-breadcrumb>-->
    </div>
  </div>
</template>

<script>
export default {
  name: "BookshopNavigator"
}
</script>

<style scoped>
/deep/ .el-breadcrumb__separator {
  color: black;
}
</style>