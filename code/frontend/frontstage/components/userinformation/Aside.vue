<template>
  <div class="common-layout" style="max-width: 168px ">
    <el-container>
      <el-aside width="200px">
        <el-row class="tac">
          <el-col :span="30">
            <el-menu
                active-text-color="#409EFF"
                background-color="#000000"
                text-color="#FFFFFF"
                default-active="2"
                class="el-menu-vertical-demo"
                @open="handleOpen"
                @close="handleClose"
            >
              <el-sub-menu index="1">
                <template #title>
                  <el-icon>
                    <User/>
                  </el-icon>
                  <span>我的信息</span>
                </template>
                <el-menu-item-group>
                  <router-link :to="{name: 'self'}" class="routerlink">
                    <el-menu-item index="1-1">基本信息</el-menu-item>
                  </router-link>
                  <router-link :to="{name: 'address'}" class="routerlink">
                    <el-menu-item index="1-2">地址管理</el-menu-item>
                  </router-link>
                  <router-link :to="{name: 'wallet'}" class="routerlink">
                    <el-menu-item index="1-3">我的钱包</el-menu-item>
                  </router-link>
                  <router-link :to="{name: 'notification'}" class="routerlink">
                    <el-menu-item index="1-4">通知</el-menu-item>
                  </router-link>
                </el-menu-item-group>

              </el-sub-menu>
              <el-sub-menu index="2">
                <template #title>
                  <el-icon>
                    <Edit/>
                  </el-icon>
                  <span>我的订单</span>
                </template>
                <el-menu-item-group>
                  <router-link :to="{name:'boughtbook'}" class="routerlink">
                    <el-menu-item index="2-1">买过的书</el-menu-item>
                  </router-link>
                  <router-link :to="{name:'selledbook'}" class="routerlink">
                    <el-menu-item index="2-2">卖过的书</el-menu-item>
                  </router-link>
                </el-menu-item-group>
              </el-sub-menu>
              <el-menu-item index="3">
                <template #title>
                  <el-icon>
                    <setting/>
                  </el-icon>
                  <router-link :to="{name:'setting'}" class="routerlink">
                    <span>设置</span>
                  </router-link>
                </template>
              </el-menu-item>
            </el-menu>
          </el-col>
        </el-row>
      </el-aside>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "Aside"
}
</script>

<style scoped>
.routerlink {
  color: white;
  text-decoration-line: none;
}
</style>