<template>
    <div class="common-layout">
        <el-container>
            <el-header> <span class="tittle">
          地址管理
        </span>
                <el-row justify="end">
                    <el-col span="6">
                        <el-button type="primary" @click="dialogFormVisible1 = true;">新增收货人地址</el-button>
                        <el-dialog v-model="dialogFormVisible1" title="新增收货人地址">
                            <el-form
                                    :model="form1"
                                    ref="ruleFormRef"
                                    :rules="rules"
                                    label-width="120px"
                                    class="demo-ruleForm"
                                    :size="formSize"
                                    status-icon
                            >
                                <el-form-item label="收件人姓名" :label-width="formLabelWidth"
                                              prop="form2.receiver_name">
                                    <el-input v-model="form1.receiver_name" autocomplete="off"/>
                                </el-form-item>

                                <el-form-item label="联系方式" :label-width="formLabelWidth"
                                              prop="form2.receiver_phone">
                                    <el-input v-model="form1.receiver_phone" autocomplete="off"/>
                                </el-form-item>

                                <el-form-item label="省市" :label-width="formLabelWidth" prop="form2.receiver_region">
                                    <el-select v-model="form1.receiver_region" placeholder="选择省市"
                                               :options="options">
                                        <el-option label="上海市" value="上海市"/>
                                        <el-option label="北京市" value="北京市"/>
                                        <el-option label="天津市" value="天津市"/>
                                        <el-option label="甘肃省" value="甘肃省"/>
                                    </el-select>
                                </el-form-item>

                                <el-form-item label="详细地址" :label-width="formLabelWidth"
                                              prop="form2.receiver_place">
                                    <el-input v-model="form1.receiver_place" autocomplete="off"
                                              placeholder="区、县/街道/门牌号"/>
                                </el-form-item>
                            </el-form>
                            <template #footer>

      <span class="dialog-footer">
        <el-button @click="dialogFormVisible1 = false">取消</el-button>
        <el-button type="primary" @click="add(form1),refresh(), dialogFormVisible1 = false">
        添加</el-button>
      </span>
                            </template>
                        </el-dialog>
                        <el-dialog v-model="dialogFormVisible2" title="编辑收货人地址">
                            <el-form
                                    :model="form2"
                                    ref="ruleFormRef"
                                    :rules="rules"
                                    label-width="120px"
                                    class="demo-ruleForm"
                                    :size="formSize"
                                    status-icon
                            >
                                <el-form-item label="收件人姓名" :label-width="formLabelWidth"
                                              prop="form2.receiver_name">
                                    <el-input v-model="form2.receiver_name" autocomplete="off"/>
                                </el-form-item>

                                <el-form-item label="联系方式" :label-width="formLabelWidth"
                                              prop="form2.receiver_phone">
                                    <el-input v-model="form2.receiver_phone" autocomplete="off"/>
                                </el-form-item>

                                <el-form-item label="省市" :label-width="formLabelWidth" prop="form2.receiver_region">
                                    <el-select v-model="form2.receiver_region" placeholder="选择省市"
                                               :options="options">
                                        <el-option label="上海市" value="上海市"/>
                                        <el-option label="北京市" value="北京市"/>
                                        <el-option label="天津市" value="天津市"/>
                                        <el-option label="甘肃省" value="甘肃省"/>
                                    </el-select>
                                </el-form-item>

                                <el-form-item label="详细地址" :label-width="formLabelWidth"
                                              prop="form2.receiver_place">
                                    <el-input v-model="form2.receiver_place" autocomplete="off"
                                              placeholder="区、县/街道/门牌号"/>
                                </el-form-item>
                            </el-form>
                            <template #footer>

      <span class="dialog-footer">
        <el-button @click="dialogFormVisible2 = false">取消</el-button>
        <el-button type="primary" @click="dialogFormVisible2 = false , modify(form2.id,form2) ">
        确认</el-button>
      </span>
                            </template>
                        </el-dialog>
                    </el-col>
                </el-row>
            </el-header>
            <el-main>
                <el-descriptions style="padding-top: 30px" v-for="(item,index) in address" :key="item.id"
                                 class="margin-top"
                                 :title="index+1"
                                 :column="3"
                                 :size="size"
                                 border>
                    <el-descriptions-item>
                        <template #label>
                            <div class="cell-item">
                                <el-icon :style="iconStyle">
                                    <user/>
                                </el-icon>
                                收件人姓名
                            </div>
                        </template>
                        {{ item.receiver_name }}
                    </el-descriptions-item>
                    <el-descriptions-item>
                        <template #label>
                            <div class="cell-item">
                                <el-icon :style="iconStyle">
                                    <iphone/>
                                </el-icon>
                                联系方式
                            </div>
                        </template>
                        {{ item.receiver_phone }}
                    </el-descriptions-item>
                    <el-descriptions-item>
                        <template #label>
                            <div class="cell-item">
                                <el-icon :style="iconStyle">
                                    <location/>
                                </el-icon>
                                省市
                            </div>
                        </template>
                        {{ item.receiver_region }}
                    </el-descriptions-item>
                    <el-descriptions-item>
                        <template #label>
                            <div class="cell-item">
                                <el-icon :style="iconStyle">
                                    <office-building/>
                                </el-icon>
                                详细地址
                            </div>
                        </template>
                        {{ item.receiver_place }}
                    </el-descriptions-item>
                    <template #extra>
                        <el-row justify="end">
                            <el-col span="10">
                                <el-button type="primary" size="small"
                                           @click="dialogFormVisible2 = true, edit(item.id,index)">
                                    编辑
                                </el-button>
                                <el-button type="danger" @click="open(item.id)" size="small">删除</el-button>
                            </el-col>
                        </el-row>
                    </template>
                </el-descriptions>
            </el-main>
        </el-container>
    </div>
</template>

<script lang="ts" setup>
import {onMounted, reactive, ref} from "vue";

let dialogFormVisible1 = ref(false)
let dialogFormVisible2 = ref(false)

const formLabelWidth = '140px'
import {FormRules,} from 'element-plus'
import {addUserAddress, loadUserAddress,modifyUserAddress,deleteUserAddress} from "../../api/userAddressService"

const user_id = ref()

const address = ref()
onMounted(() => {
    user_id.value = window.sessionStorage.getItem("id")
    loadUserAddress(user_id.value).then((r) => {
            address.value = r.data
            console.log(address.value)
        }
    )
})

function add(form1) {
    console.log(form1)
    addUserAddress(form1).then((r) => {
        console.log(r.data)
    })

}

function modify(id, form2) {
    console.log(form2)
    modifyUserAddress(id, form2).then((r) => {
        console.log(r.data)
        refresh()
    })

}
function refresh(){
    location.reload()
}
function edit(id, index) {
    console.log(address.value[index])
    form2.id = address.value[index].id
    form2.receiver_name = address.value[index].receiver_name
    form2.receiver_region = address.value[index].receiver_region
    form2.receiver_phone = address.value[index].receiver_phone
    form2.receiver_place = address.value[index].receiver_place
}

const form1 = reactive({
    user_id: window.sessionStorage.getItem("id"),
    receiver_name: '',
    receiver_phone: '',
    receiver_region: '',
    receiver_place: '',
})

const form2 = reactive({
    // user_id: window.sessionStorage.getItem("id"),
    id: '',
    receiver_name: '',
    receiver_phone: '',
    receiver_region: '',
    receiver_place: '',
})
const options = Array.from({length: 10000}).map((_, idx) => ({
    value: `${idx + 1}`,
    label: `${idx + 1}`,
}))


const rules = reactive<FormRules>({
    name: [
        {required: true, message: '请填写收货人姓名', trigger: 'blur'},
        {min: 2, max: 5, message: '输入格式有误', trigger: 'blur'},
    ],
    phone: [
        {required: true, message: '请填写联系方式', trigger: 'blur'},
        {min: 11, max: 11, message: '联系方式必须11位', trigger: 'blur'},
    ],
    place: [
        {
            required: true,
            message: '请填写地址',
            trigger: 'blur',
        },
    ],
    region: [
        {
            required: true,
            message: '请选择省/市',
            trigger: 'blur',
        },
    ],
})

import {ElMessage, ElMessageBox} from 'element-plus'

function open(id) {
    ElMessageBox.confirm(
        '您确定删除这个收获地址？',
        '提示',
        {
            confirmButtonText: '确认',
            cancelButtonText: '取消',
            type: 'warning',
        }
    ).then(() => {
        deleteUserAddress(id).then((r) => {
            console.log(r)
            refresh()
            ElMessage({
                type: 'success',
                message: '删除成功',
            })
        }).catch((e) => {
            console.log(e)
            ElMessage({
                type: 'info',
                message: '删除失败',
            })
        })
    })
}

</script>

<style scoped>
.tittle {
    color: aqua;
    font-size: 16px;
}

.margin-top {
    color: #FFFFFF;
}
</style>