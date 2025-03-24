<template>
    <div class="app-container" ref="appContainer" v-if="load">
        <div class="app-container-inner">
            <el-main>
                <PropTable
                        :loading="loading"
                        @selection-change="selectionChange"
                        :columns="column"
                        :data="list"
                >
                    <template v-slot:operation="scope">
                        <el-button type="primary" @click="handleAddData(scope.row)">判断品相</el-button>
                    </template>
                </PropTable>
            </el-main>
            <el-footer>
                <el-row justify="end">
                    <el-button type="danger" @click="dialogVisible1=true">提交</el-button>
                </el-row>
            </el-footer>
            <el-dialog v-model="dialogVisible1" title="提示" width="30%">
                <span>确定提交？</span>
                <template #footer>
          <span class="dialog-footer">
            <el-button @click="dialogVisible1 = false">取消</el-button>
              <router-link to="checked_orders">
            <el-button type="primary" @click="submitForm()">确定 </el-button>
                  </router-link>
          </span>
                </template>
            </el-dialog>
            <el-dialog v-model="dialogVisible2" title="判断品相" width="50%">
                <div>
                    <el-row justify="center">
                        <el-radio-group v-model="conditionForm.final_condition">
                            <el-radio-button label="中等"/>
                            <el-radio-button label="优良"/>
                            <el-radio-button label="不合格"/>
                        </el-radio-group>
                    </el-row>
                </div>
                <template #footer>
          <span class="dialog-footer">
            <el-button @click="dialogVisible2 = false">取消</el-button>
            <el-button type="primary" @click="addcondition(conditionForm)"> 确定 </el-button>
          </span>
                </template>
            </el-dialog>
        </div>
    </div>
</template>

<script lang="ts" setup>
import {nextTick, onBeforeMount, onMounted, reactive, ref} from 'vue'
import {useRoute, useRouter} from 'vue-router'

const loading = ref(true)
import PropTable from '@/components/Table/PropTable/index2.vue'
import {ElMessage, FormInstance, ElNotification} from 'element-plus'
import {
    sellOrderDetail,
    getBookCondition,
    sellCheckCondition,
    selldetailModify,
    modifyBalance,
    userDetail,
    addInventory
} from '../../../api/orderService'

const appContainer = ref(null)
let currentIndex = -1
const time = new Date
const isoString = time.toISOString();
const route = useRoute()
let note = ref('')
let note_id = ref('')
let note_user_id = ref('')
const options = [
    {
        value: '中等',
        label: '中等',
    },
    {
        value: '优良',
        label: '优良',
    },
    {
        value: '不合格',
        label: '不合格',
    },
]
const data = []

function sum() {
    Form.forEach((e, i) => {
        balance.value = balance.value + e.final_price
    })
    return {balance: parseFloat(balance.value).toFixed(2)}
}

function submitForm() {
    for (let i = 0; i < Form.length; i++) {
        if (Form[i].final_price == null) {
            ElNotification({
                title: '失败啦',
                message: '订单有书目没有审核！',
                type: 'error',
            })
            return 0
        }
    }
    console.log(Form.length)
    Form.forEach((e, i) => {
        sellCheckCondition(e.id, {final_condition: e.final_condition, final_price: e.final_price}).then(r => {
            console.log("rr:", r.data)
            if (e.final_condition != 5) {
                addInventory({book: e.book_isbn, condition_rate: e.final_condition, book_num: 1})
            }
        })
    })
    // console.log("formforeach:", form2)
    console.log(isoString)
    const status = reactive({
        status: 1,
        finish_time: isoString
    })
    console.log(status)
    selldetailModify(note_id, status)
    modifyBalance(note_user_id, sum())
    ElNotification({
        title: '成功啦',
        message: '订单审核工作结束！',
        type: 'success',
    })

}

function handleAddData(index) {
    dialogVisible2.value = true
    currentIndex = index.idd - 1
    console.log(currentIndex)
}


function addcondition(conditionForm) {
    dialogVisible2.value = false
    console.log(currentIndex)
    console.log(conditionForm)
    console.log(conditionForm.final_condition)
    // Form[currentIndex].final_condition = conditionForm.final_condition
    // console.log(Form[currentIndex].final_condition)
    if (conditionForm.final_condition == '中等') {
        Form[currentIndex].final_condition = 1
        Form[currentIndex].final_conditionrate = b_conditions[0].sell_rate
        Form[currentIndex].final_price = Form[currentIndex].book_price * b_conditions[0].sell_rate
    }
    if (conditionForm.final_condition == '优良') {
        Form[currentIndex].final_condition = 2
        Form[currentIndex].final_conditionrate = b_conditions[1].sell_rate
        Form[currentIndex].final_price = Form[currentIndex].book_price * b_conditions[1].sell_rate
    }
    if (conditionForm.final_condition == '不合格') {
        Form[currentIndex].final_condition = 5
        Form[currentIndex].final_conditionrate = 0
        Form[currentIndex].final_price = 0
    }
    console.log(Form)
    currentIndex = -1
}

const conditionForm = reactive({final_condition: ''})
let Form = reactive([])
const column = [
    {name: 'idd', label: '序号', inSearch: true, valueType: 'input', width: 60},
    // { name: 'book_picture', label: '封面', width: 220 },
    {
        name: 'book_name',
        label: '书名',
        valueType: 'input',
        width: 130,
    },
    {
        name: 'book_isbn',
        label: 'ISBN',
        valueType: 'input',
        width: 180,
    },
    {name: 'book_writer', label: '作者', width: 130, valueType: 'input'},
    {name: 'book_price', label: '原价', width: 150, valueType: 'input'},
    {name: 'customer_condition', label: '用户预期品相', width: 166, valueType: 'input'},
    {
        name: 'operation',
        slot: true,
        fixed: 'right',
        width: 140,
        label: '判断品相',
        valueType: 'input',
    },
]
const list = ref(data)
const load = ref(false)
const formSize = ref('default')
const ruleFormRef = ref<FormInstance>()
let balance = ref('')
const rowObj = ref({})
const selectObj = ref([])
const dialogVisible1 = ref(false)
let dialogVisible2 = ref(false)
const b_conditions = reactive([{id: '', condition: '', buy_rate: '', sell_rate: ''}])
const onSubmit = (val) => {
    console.log('val===', val)
    ElMessage.success('触发查询方法')
    loading.value = true

    setTimeout(() => {
        loading.value = false
    }, 500)
}
onMounted(() => {
    sellOrderDetail(note_id).then((r) => {
        console.log(r.data)
        let j = 1
        r.data.forEach((e, i) => {
            e.idd = j
            Form.push(e)
            j += 1
        })
        // Form = r.data
        console.log(Form)
        r.data.forEach((e, i) => {
            data.push(e)
        })
        load.value = true
    })
})

onBeforeMount(() => {
    note = JSON.parse(route.query.data)
    console.log(note)
    note_id = note.id
    note_user_id = note.user_id
    console.log(note_user_id)
    userDetail(note_user_id).then((r) => {
        balance.value = r.data.balance
        console.log(balance.value)
    })
    getBookCondition().then((r) => {
        b_conditions[0] = r.data[0]
        b_conditions[1] = r.data[1]
        console.log(b_conditions)
    })
})
onMounted(() => {
    nextTick(() => {
        // let data = appContainer.value.
    })
    setTimeout(() => {
        loading.value = false
    }, 500)
})
</script>
<style scoped>
.app-container {
    flex: 1;
    display: flex;
    width: 100%;
    padding: 16px;
    box-sizing: border-box;
}

.dialog-footer button:first-child {
    margin-right: 10px;
}
</style>
