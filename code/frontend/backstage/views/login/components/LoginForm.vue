<template>
  <el-form ref="ruleFormRef" :model="ruleForm" :rules="rules" label-width="0">
    <el-form-item label="" prop="username">
      <el-input
        placeholder="请输入用户名"
        autoComplete="on"
        style="position: relative"
        v-model="ruleForm.username"
        @keyup.enter.native="submitForm(ruleFormRef)"
      >
        <template #prefix>
          <el-icon class="el-input__icon">
            <UserFilled />
          </el-icon>
        </template>
      </el-input>
    </el-form-item>
    <el-form-item label="" prop="password">
      <el-input
        placeholder="请输入密码"
        autoComplete="on"
        @keyup.enter.native="submitForm(ruleFormRef)"
        v-model="ruleForm.password"
        :type="passwordType"
      >
        <template #prefix>
          <el-icon class="el-input__icon">
            <GoodsFilled />
          </el-icon>
        </template>
        <template #suffix>
          <div class="show-pwd" @click="showPwd">
            <svg-icon :icon-class="passwordType === 'password' ? 'eye' : 'eye-open'" />
          </div>
        </template>
      </el-input>
    </el-form-item>
    <el-form-item style="width: 100%">
      <el-button
        :loading="loading"
        class="login-btn"
        type="primary"
        @click="submitForm(ruleFormRef)"
        >登录
      </el-button>
    </el-form-item>
  </el-form>
</template>
<script lang="ts" setup>
  import { reactive, ref } from 'vue'
  import type { FormInstance } from 'element-plus'
  import { ElNotification } from 'element-plus'
  import { useRouter } from 'vue-router'
  import { useUserStore } from '@/store/modules/user'
  import { getTimeState } from '@/utils/index'

  const ruleFormRef = ref<FormInstance>()
  const router = useRouter()
  const UserStore = useUserStore()

  const passwordType = ref('password')
  const loading = ref(false)
  const rules = reactive({
    password: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
    username: [{ required: true, message: '请输入密码', trigger: 'blur' }],
  })
  // 表单数据
  const ruleForm = reactive({
    username: '',
    password: '',
  })

  const showPwd = () => {
    if (passwordType.value === 'password') {
      passwordType.value = ''
    } else {
      passwordType.value = 'password'
    }
  }
  const submitForm = (formEl: FormInstance | undefined) => {
    loading.value = true
    if (!formEl) return
    formEl.validate((valid) => {
      if (valid) {
        // 登录
        setTimeout(async () => {
          await UserStore.login(ruleForm).then(async (r) => {
            await router.push({
              path: '/',
            })
            const msg = UserStore.name + '，欢迎登陆品读！'
            ElNotification({
              title: getTimeState(),
              message: msg,
              type: 'success',
              duration: 3000,
            })
            console.log(UserStore.id)
          })
        }, 500)
      } else {
        console.log('error submit!')
        return false
      }
    })
  }
</script>

<style lang="scss" scoped>
  @import '../index.scss';
</style>
