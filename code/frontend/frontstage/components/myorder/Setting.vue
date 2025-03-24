<template>
    <el-header>
        <div style="color: #f30213">修改密码</div>
    </el-header>
    <el-main>
        <div class="container">
            <el-form ref="formRef" :model="form" label-width="80px">
                <el-form-item label="旧密码" prop="oldPassword">
                    <el-input style="width: 200px" v-model="form.old_pw"></el-input>
                </el-form-item>
                <el-form-item label="新密码" prop="newPassword">
                    <el-input style="width: 200px" type="password" v-model="form.new_pw"></el-input>
                </el-form-item>
                <el-form-item label="确认密码" prop="confirmPassword">
                    <el-input style="width: 200px" type="password" v-model="form.confirm_pw"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="submitForm()">提交</el-button>
                </el-form-item>
            </el-form>
        </div>
    </el-main>
</template>

<script lang="ts" setup>
import {reactive, ref} from "vue";
import {userCPassword, userTPassword} from "../../api/userService";
import {ElMessage} from "element-plus";

const form = reactive({
    user_id: window.sessionStorage.getItem("id"),
    old_pw: '',
    new_pw: '',
    confirm_pw: '',
})
const Tform = reactive({
    user_id: window.sessionStorage.getItem("id"),
    user_password: ''
})
const submitForm = () => {
    const {old_pw, new_pw, confirm_pw} = form;
    Tform.user_password = form.old_pw
    let consequnence = ''
    userTPassword(Tform).then((r) => {
        console.log(Tform)
        consequnence = r.data.status
        if (consequnence == true && old_pw && new_pw && confirm_pw && new_pw === confirm_pw) {
            // 处理密码修改逻辑
            console.log('旧密码：', old_pw);
            console.log('新密码：', new_pw);
            console.log('确认密码：', confirm_pw);
            userCPassword(form).then((r) => {
                console.log(r.data)
                ElMessage({
                    message: '修改密码成功',
                    type: 'success',
                })
                location.reload()
            })
        } else {
            ElMessage({
                message: '修改密码失败',
                type: 'warning',
            })
        }
    })
};

</script>

<style scoped>
.container {
    display: flex;
    justify-content: center;
    /*align-items: center;*/
    height: 100vh;
    margin-right: 90px
}

</style>