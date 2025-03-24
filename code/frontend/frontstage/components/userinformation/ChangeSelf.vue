<template>
    <div class="common-layout">
        <el-container>
            <el-header> <span style="color: #f30213;font-size: 16px;">
         修改信息
        </span>
            </el-header>
            <el-main>
                <el-row class="row-bg" justify="center">
                    <el-col :span="6">
                        <el-avatar class="portrait" :icon="UserFilled"/>
                    </el-col>
                </el-row>
                <br>
                <el-form
                        ref="ruleFormRef"
                        :model="ruleForm"
                        status-icon
                        :rules="rules"
                        label-width="120px"
                        class="ruleForm">
                    <el-row justify="center">
                        <el-col span="1" :pull="3">
                            <div>
                                <el-form-item label="姓名" prop="first_name" style="width: 100%">
                                    <el-input v-model="ruleForm.first_name" placeholder="Please input"/>
                                </el-form-item>
                            </div>
                        </el-col>
                    </el-row>
                    <br>
                    <el-row justify="center">
                        <el-col span="1" :pull="3">
                            <div>
                                <el-form-item label="性别" prop="gender">
                                    <el-select v-model="ruleForm.gender" placeholder="男">
                                        <el-option label="男" value="男"></el-option>
                                        <el-option label="女" value="女"></el-option>
                                    </el-select>
                                </el-form-item>
                            </div>
                        </el-col>
                    </el-row>
                    <br>
                    <el-row justify="center">
                        <el-col span="1" :pull="3">
                            <el-form-item label="生日" prop="birth">
                                <el-date-picker
                                        v-model="ruleForm.birth"
                                        type="date"
                                        label="pick a date"
                                        placeholder="Pick a day"
                                        style="width: 100%"
                                        format="YYYY/MM/DD"
                                        value-format="YYYY-MM-DD"
                                />
                            </el-form-item>
                        </el-col>
                    </el-row>
                    <br>
                    <el-row justify="center">
                        <el-col span="1" :pull="3">
                            <el-form-item>
                                <el-button type="danger" @click="resetForm()">重置</el-button>
                            </el-form-item>
                        </el-col>
                        <el-col span="1" :pull="3">
                            <el-form-item>
                                <router-link :to="{name: 'self'}">
                                    <el-button type="primary" @click="submitForm(ruleForm)">确认修改</el-button>
                                </router-link>
                            </el-form-item>
                        </el-col>
                         <el-col span="1" :pull="3">
                            <el-form-item>
                                <router-link :to="{name: 'self'}">
                                    <el-button type="default" >返回</el-button>
                                </router-link>
                            </el-form-item>
                        </el-col>
                    </el-row>
                </el-form>
            </el-main>
        </el-container>
    </div>
</template>

<script lang="ts" setup>
import {UserFilled} from "@element-plus/icons-vue";
import {ref, reactive, onMounted} from 'vue'
import {userDetail, userModify} from "../../api/userService";
import {FormRules,} from 'element-plus'

const ruleForm = reactive({
    first_name: '',
    gender: '',
    birth: '',
})
const user_id=ref()
onMounted(() => {
    user_id.value= window.sessionStorage.getItem("id")
    console.log(user_id.value)
    userDetail(user_id.value).then((r) => {
        console.log(r.data)
        ruleForm.first_name = r.data.first_name
        ruleForm.gender = r.data.gender
        ruleForm.birth = r.data.birth
    })
})
function submitForm(ruleForm){
    console.log(ruleForm)
    userModify(user_id.value, ruleForm)
}
function resetForm(){
    ruleForm.first_name=''
    ruleForm.gender=''
    ruleForm.birth=''
}
const rules = reactive<FormRules>({
    name: [
        {required: true, message: 'Please input Activity name', trigger: 'blur'},
        {min: 2, max: 10, message: 'Length should be 2 to 10', trigger: 'blur'},
    ],
    sex: [
        {
            required: true,
            message: 'please select your sex',
            trigger: 'change'
        }
    ],
    date: [
        {
            type: 'date',
            required: true,
            message: 'Please pick a date',
            trigger: 'change',
        }
    ]
})





</script>

<style scoped>

</style>