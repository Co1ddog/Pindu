<template>
    <div class="common-layout">
        <el-container>
            <el-header> <span class="big-tittle">
         我的钱包
        </span>
            </el-header>
            <el-main>
                <el-row justify="center">
                    <el-col :span="4">
                        <div class="statistic-card">
                            <el-statistic :value=balance1 value-style="color: #FFFFFF">
                                <template #title>
                                    <div style="display: inline-flex; align-items: center; color: #FFFFFF">
                                        钱包余额
                                        <el-tooltip
                                                effect="dark"
                                                content="购买与售卖图书将会从中扣除与增加金额"
                                                placement="top"
                                        >
                                            <el-icon style="margin-left: 4px" :size="12">
                                                <Warning/>
                                            </el-icon>
                                        </el-tooltip>
                                    </div>
                                </template>
                            </el-statistic>
                        </div>
                    </el-col>
                </el-row>
                <br>
                <el-row :gutter="40">

                    <el-col :offset="9">
                        <el-button type="primary" @click="dialogVisible = true" round>充值</el-button>
                        <el-button type="success" @click="dialogVisible1 = true" round>提现</el-button>
                    </el-col>

                </el-row>
            </el-main>
        </el-container>
    </div>
    <el-dialog
            v-model="dialogVisible1"
            title="提现"
            width="30%"
    >
        <div>
            <el-form
                    ref="formRef1"
                    :model="numberValidateForm"
                    label-width="100px"
                    class="ruleForm"
            >
                <el-form-item
                        label="金额"
                        prop="balance2"
                >
                    <el-input-number v-model="numberValidateForm1.balance" :step='10' precision="0.1"
                                     placeholder="输入提现金额"/>
                </el-form-item>
            </el-form>
        </div>
        <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogVisible1 = false">取消</el-button>
        <el-button type="primary" @click="dialogVisible1 = false,submitForm1()">
          确定
        </el-button>
      </span>
        </template>
    </el-dialog>
    <el-dialog
            v-model="dialogVisible"
            title="充值"
            width="30%"
            :before-close="handleClose"
    >
        <div>
            <el-form
                    ref="formRef"
                    :model="numberValidateForm"
                    label-width="100px"
                    class="ruleForm"
            >
                <el-form-item
                        label="金额"
                        prop="balance2"
                >
                    <el-input-number v-model="numberValidateForm.balance" :step='10' precision="0.1"
                                     placeholder="输入充值金额"/>
                </el-form-item>
            </el-form>
        </div>
        <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="dialogVisible = false,submitForm()">
          确定
        </el-button>
      </span>
        </template>
    </el-dialog>
</template>

<script lang="ts" setup>

import {ElMessage, ElMessageBox} from 'element-plus'
import {onMounted, reactive, ref} from 'vue'
import type {FormInstance} from 'element-plus'
import {userDetail, userModify} from "../../api/userService";

let balance1 = ref()
const dialogVisible = ref(false)
const dialogVisible1 = ref(false)

const user_id = ref()
onMounted(() => {
    user_id.value = window.sessionStorage.getItem("id")
    userDetail(user_id.value).then((r) => {
        console.log(r.data)
        balance1.value = r.data.balance

    })

})

function refresh() {
    location.reload()
}

const formRef = ref<FormInstance>()
const formRef1 = ref<FormInstance>()
const numberValidateForm = reactive({
    balance: ''
})
const numberValidateForm1 = reactive({
    balance: ''
})

function sum() {
    return {balance: parseFloat(balance1.value) + parseFloat(numberValidateForm.balance)}
}

function del() {
    return {balance: parseFloat(balance1.value) - parseFloat(numberValidateForm1.balance)}
}

function submitForm() {
    console.log(typeof balance1.value)
    console.log(typeof numberValidateForm.balance)
    console.log(sum())
    if (numberValidateForm.balance <= 0) {
        ElMessage({
            type: 'info',
            message: '充值失败！充值金额不能小于0',
        })
    } else {
        userModify(user_id.value, sum()).then((r) => {
            console.log(r.data)
            refresh()
        })
    }
}

function submitForm1() {
    console.log(typeof balance1.value)
    console.log(typeof numberValidateForm1.balance)
    console.log(del())
    if (numberValidateForm1.balance <= 0) {
        ElMessage({
            type: 'info',
            message: '提现失败！提现金额不能小于0',
        })
    }
    else if (numberValidateForm1.balance>balance1.value) {
         ElMessage({
            type: 'info',
            message: '提现失败！提现金额不能大于余额',
        })
    } else {
        userModify(user_id.value, del()).then((r) => {
            console.log(r.data)
            refresh()
        })
    }
}

const handleClose = (done: () => void) => {
    ElMessageBox.confirm('您确定取消充值？',
        '提示', {
            confirmButtonText: '确认',
            cancelButtonText: '取消',
            type: 'warning',
        })
        .then(() => {
            done()
        })
        .catch(() => {
            // catch error
        })
}
</script>

<style scoped>
.big-tittle {
    color: aqua;
    font-size: 16px;
}

.dialog-footer button:first-child {
    margin-right: 10px;
}

</style>