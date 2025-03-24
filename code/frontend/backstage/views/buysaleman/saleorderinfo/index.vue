<template>
  <div v-if="load" class="app-container" ref="appContainer">
    <PropTable
        :loading="loading"
        @selection-change="selectionChange"
        :columns="column"
        :data="list"
        @reset="reset"
        @onSubmit="onSubmit"
    >
      <!--      <template v-slot:btn>-->
      <!--        <div style="display: flex; justify-content: flex-end">-->
      <!--          <el-button type="primary" @click="add"-->
      <!--            ><el-icon><plus /></el-icon>添加</el-button-->
      <!--          >-->
      <!--          <el-button type="danger" @click="batchDelete"-->
      <!--            ><el-icon><delete /></el-icon>删除</el-button-->
      <!--          >-->
      <!--        </div>-->
      <!--      </template>-->
      <template v-slot:status="scope">{{
          scope.row.status === 0
              ? '待处理'
              : scope.row.status === 1
                  ? '已发货'
                  : scope.row.status === 2
                      ? '已收货'
                      : scope.row.status === 3
                          ? '已取消'
                          : 'invalid option'
        }}
      </template>
      <template v-slot:operation="scope">
        <el-button type="primary" size="small" icon="Edit" @click="edit(scope.row)">
          详细信息
        </el-button>
      </template>
    </PropTable>

    <el-dialog v-model="dialogVisible" :title="title" width="50%">
      <prop-table :loading="loading" :columns="column1" :data="books"></prop-table>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="dialogclose">关闭</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>
<script lang="ts" setup name="comprehensive">
import {ref, reactive, onMounted, nextTick} from 'vue'
import * as dayjs from 'dayjs'
import {ElMessage, ElMessageBox} from 'element-plus'
import type {FormInstance} from 'element-plus'

const loading = ref(true)
const appContainer = ref(null)
import PropTable from '@/components/Table/PropTable/index.vue'
import {getsellorders} from '../../../api/getOrders.js'
import {getsellorderdetail} from '../../../api/orderDetails.js'

const load = ref(false)
const books = ref([])
const data = []
onMounted(() => {
  getsellorders().then((r) => {
    for (let i = 0; i < r.data.length; i++) {
      data.push({
        id: r.data[i].id,
        user_id: r.data[i].user_id,
        status: r.data[i].status,
        a_id: 2,
      })
    }
    console.log('tabledata', data)
    load.value = true
    // for (let i = 0; i < r.data.length; i++) {
    //   data.push({
    //     eb_id: i
    //     name: '王五' + i,
    //     u_id: i,
    //     eb_sta: i % 4,
    //     checked: true,
    //     a_id: 2,
    //     zip: 200333,
    //   })
    // }
  })
})
const column = [
  // { type: 'selection', width: 60, fixed: 'left' },
  {name: 'id', label: '卖书订单号', inSearch: true, valueType: 'input', width: 180},
  {name: 'user_id', label: '用户ID'},
  {
    name: 'status',
    label: '订单状态',
    slot: true,
    inSearch: true,
    options: [
      {
        value: 1,
        label: '已发货',
      },
      {
        value: 0,
        label: '待处理',
      },
      {
        value: 2,
        label: '已收货',
      },
      {
        value: 3,
        label: '已取消',
      },
    ],
    valueType: 'select',
  },
  {name: 'a_id', label: '业务管理员ID', inSearch: true, valueType: 'input'},
  // { name: 'admin', label: '账号', inSearch: true, valueType: 'input' },
  // { name: 'address', label: '地址', inSearch: true, valueType: 'input' , width: 180},
  // { name: 'date', label: '日期', sorter: true, inSearch: true, valueType: 'input', width: 180 },
  // { name: 'province', label: '省份' , width: 100},
  // { name: 'city', label: '城市' },
  // { name: 'zip', label: '邮编' },
  {name: 'operation', slot: true, fixed: 'right', width: 200, label: '操作'},
]

function dialogclose() {
  books.value.splice(0)
  dialogVisible.value = false
}

const column1 = [
  {name: 'b_isbn', label: 'ISBN'},
  {name: 'b_name', label: '书名'},
  {
    name: 'condition',
    label: '图书品相',
  },
  {
    name: 'num',
    label: '购买数量',
  },
]
const list = ref(data)

const formSize = ref('default')
const ruleFormRef = ref<FormInstance>()
const ruleForm = reactive({
  name: '',
  sex: null,
  price: null,
})

// const rules = reactive({
//   name: [
//     { required: true, message: '请输入活动名称活动区域', trigger: 'blur' },
//     { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' },
//   ],
//   price: [{ required: true, message: '请输入价格', trigger: 'blur' }],
//   sex: [
//     {
//       required: true,
//       message: '请选择性别',
//       trigger: 'change',
//     },
//   ],
// })

const dialogVisible = ref(false)
const title = ref('新增')
const rowObj = ref({})
const selectObj = ref([])

// const handleClose = async (done: () => void) => {
//   await ruleFormRef.value.validate((valid, fields) => {
//     if (valid) {
//       let obj = {
//         id: Date.now(),
//         ...ruleForm,
//         age: 0,
//         city: '普陀区',
//         address: '上海市普上海',
//         zip: 200333,
//         province: '上海',
//         admin: 'admin',
//       }
//       if (title.value === '新增') {
//         list.value = [obj, ...list.value]
//         ElMessage.success('添加成功')
//       } else {
//         list.value.forEach((item) => {
//           if (item.id === rowObj.value.id) {
//             item.name = obj.name
//             item.sex = obj.sex
//             item.price = obj.price
//           }
//         })
//       }
//       dialogVisible.value = false
//       console.log('submit!', obj)
//     } else {
//       console.log('error submit!', fields)
//     }
//   })
// }
function edit(row) {
  // edit = (row) => {
  title.value = '详细信息'
  rowObj.value = row
  getsellorderdetail(row.id).then((r) => {
    console.log(row.id)
    console.log(r)
    for (let i = 0; i < r.data.length; i++) {
      books.value.push({
        b_isbn: r.data[i].inventory_book_isbn,
        b_name: r.data[i].inventory_book_name,
        condition: r.data[i].inventory_conditionrate_condition,
        num: r.data[i].book_num,
      })
    }
    console.log(books)
    dialogVisible.value = true
    // load1.value = true
  })
}

const add = () => {
  title.value = '新增'
  dialogVisible.value = true
}

// const batchDelete = () => {
//   if (!selectObj.value.length) {
//     return ElMessage.error('未选中任何行')
//   }
//   ElMessageBox.confirm('你确定要删除选中项吗?', '温馨提示', {
//     confirmButtonText: '确定',
//     cancelButtonText: '取消',
//     type: 'warning',
//     draggable: true,
//   })
//     .then(() => {
//       ElMessage.success('模拟删除成功')
//       list.value = list.value.concat([])
//     })
//     .catch(() => {})
// }
const selectionChange = (val) => {
  selectObj.value = val
}

const reset = () => {
  loading.value = true
  setTimeout(() => {
    loading.value = false
  }, 500)
  ElMessage.success('触发重置方法')
}

const onSubmit = (val) => {
  console.log('val===', val)
  ElMessage.success('触发查询方法')
  loading.value = true
  setTimeout(() => {
    loading.value = false
  }, 500)
}

// const getHeight = () => {}

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
.edit-input {
  padding-right: 100px;
}

.app-container {
  flex: 1;
  display: flex;
  width: 100%;
  padding: 16px;
  box-sizing: border-box;
}

.cancel-btn {
  position: absolute;
  right: 15px;
  top: 10px;
}
</style>
