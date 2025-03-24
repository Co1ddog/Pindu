<template>
  <div class="app-container">
    <!-- 搜索栏 -->
    <div class="header">
      <el-form :inline="true" :model="formInline1">
        <el-form-item label="order_id">
          <el-input v-model="formInline1.order_id" placeholder="请输入订单号"/>
        </el-form-item>

        <el-form-item label="用户名">
          <el-input v-model="formInline1.username" placeholder="请输入姓名"/>
        </el-form-item>

        <el-form-item label="uid">
          <el-input v-model="formInline1.userid" placeholder="请输入用户ID"/>
        </el-form-item>

        <el-form-item label="省份">
          <el-input v-model="formInline1.region" placeholder="请输入省市"/>
        </el-form-item>

        <el-form-item label="地址">
          <el-input v-model="formInline1.address" placeholder="请输入地址"/>
        </el-form-item>

        <el-form-item label="联系方式">
          <el-input v-model="formInline1.phone" placeholder="请输入联系方式"/>
        </el-form-item>

        <el-form-item label="订单状态">
          <el-select v-model="formInline1.attitude">
            <el-option
                v-for="item in attitude"
                :key="item.value"
                :label="item.label"
                :value="item.value"
            />
          </el-select>
        </el-form-item>
        <br/>
        <el-row justify="end">
          <el-form-item>
            <el-button type="primary" @click="onSubmit">搜索</el-button>
            <el-button @click="resetInput()">重置</el-button>
          </el-form-item>
        </el-row>
      </el-form>
    </div>

    <!-- 页面主表 -->
    <div class="footer" v-if="load">
      <el-table :data="list" style="width: 100%" :border="true" v-loading="loading">
        <el-table-column prop="order_id" width="260" label="order_id" align="center"/>
        <el-table-column prop="uid" width="60" label="uid" align="center"/>
        <el-table-column prop="name" label="用户名" width="120px" align="center"/>
        <el-table-column prop="receiver_name" label="收货人" width="120px" align="center"/>
        <el-table-column prop="region" label="省份" width="120" align="center"/>
        <el-table-column
            prop="address"
            :show-overflow-tooltip="true"
            label="地址"
            width="280"
            align="center"
        />
        <el-table-column prop="phone" label="联系方式" width="200" align="center"/>
        <el-table-column prop="date" label="日期" width="180" align="center"/>
        <el-table-column prop="attitude" label="订单状态" width="180" align="center"/>
        <el-table-column prop="detail_book_name" label="订单详情" width="180" align="center"/>
        <el-table-column prop="detail_inventory_id" label="库存id" width="180" align="center"/>
        <el-table-column prop="operator" label="操作" width="180px" fixed="right" align="center">
          <template #default="scope">
            <el-button
                type="success"
                size="small"
                icon="CircleCheckFilled"
                :disabled="scope.row.attitude === 1"
                @click="confirmEdit(scope.$index, scope.row)"
            >
              提交
            </el-button>
          </template>
        </el-table-column>
      </el-table>
      <div style="width: 100%; display: flex; justify-content: center; padding-top: 20px">
        <el-pagination
            v-model:currentPage="currentPage1"
            :page-size="10"
            background
            layout="total, sizes, prev, pager, next, jumper"
            :total="transData.length"
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup name="inline-table">
import {computed, onMounted, ref, reactive} from 'vue'
import {loadBuyOrder, changeBuyOrder, loadBuyOrderDetail} from '../../../api/orderService'
import {changeInventoryNum, loadInventoryNum} from '../../../api/inventoryService'

onMounted(() => {
  getValue()
})

let data = []

let transData = ref(data)

let list = computed(() => {
  let arr = JSON.parse(JSON.stringify(transData.value))
  return arr.splice((currentPage1.value - 1) * 10, 10)
})

const getValue = async () => {

  await loadBuyOrder().then(async (resp) => {
    await resp.data.forEach(async (t, i) => {

      let detail_book_name = []
      let detail_inventory_id = []

      await loadBuyOrderDetail(t.id).then((resp_detail) => {
        // console.log(resp_detail.data)
        resp_detail.data.forEach((e, j) => {
          detail_book_name.push(e.inventory_book_name)
          detail_inventory_id.push(e.inventory_id)
        })
      })

      // 往data传数据
      data.push({
        order_id: t.id,
        uid: t.user_id,
        name: t.user_name,
        receiver_name: t.useraddress_receiver_name,
        region: t.useraddress_receiver_region,
        address: t.useraddress_receiver_place,
        phone: t.useraddress_receiver_phone,
        date: t.submit_time,
        attitude: t.status,
        detail_book_name: detail_book_name,
        detail_inventory_id: detail_inventory_id,
      })
    })

  })
  setTimeout(() => {
    load.value = true
    loading.value = false
    console.log("表里的数据：", data)
    transData.value = data
  }, 5000)
}

const ruleForm = reactive({
  name: '',
  sex: null,
  price: null,
})

const currentPage1 = ref(1)

const handleSizeChange = (val: number) => {
  console.log(`${val} items per page`)
}

const handleCurrentChange = (val: number) => {
  console.log(`current page: ${val}`)
  currentPage1.value = val
}

const loading = ref(false)

const load = ref(false)

// 提交发货订单操作
const confirmEdit = async (index, row) => {

  // loading.value = true
  const finish_time = new Date()
  console.log('row:', row)

  row.detail_inventory_id.forEach((i) => {
    console.log("inventory_id", i)
    loadInventoryNum(i).then(async (r) => {
      console.log("数量:", r.data.book_num)

      if (r.data.book_num < 1) {
        alert("此书库存不足，无法发货")
        loading.value = false
      } else {

        const new_book_num = r.data.book_num - 1
        await changeInventoryNum(i, {book_num: new_book_num})

        await changeBuyOrder(row.order_id, {finish_time: finish_time})
        changeBuyOrder(row.order_id, {status: 1}).then((r) => {
          data = []
          getValue()
        })
      }
    })
  })
}

//如果订单状态为1,就不让添加
const isEditable = (row) => {
  if (row.attitude === 1) {
    row.operator
  }

}

// 接收表单里的数据
const formInline1 = reactive({
  username: null,
  userid: null,
  address: null,
  region: null,
  phone: null,
  date: null,
  order_id: null,
  attitude: null,
})

// option里的内容
const attitude = ref([
  {
    value: 0,
    label: '待处理--0',
  },
  {
    value: 1,
    label: '已处理--1',
  },
])

// 直接把接收表单里的重置
const resetInput = () => {
  loading.value = true
  setTimeout(() => {
    loading.value = false
  }, 500)
  formInline1.username = ''
  formInline1.userid = ''
  formInline1.address = ''
  formInline1.region = ''
  formInline1.date = ''
  formInline1.phone = ''
  formInline1.order_id = ''
  formInline1.attitude = ''
  transData.value = data
}

//搜索触发onSubmit
const onSubmit = () => {
  // getValue()
  console.log('***********************')
  console.log(formInline1)
  loading.value = true
  setTimeout(() => {
    loading.value = false
  }, 500)
  const filteredData = data.filter(
      (item) =>
          item.order_id === Number(formInline1.order_id) ||
          item.name === formInline1.username ||
          item.uid === Number(formInline1.userid) ||
          item.region === formInline1.region ||
          item.address === formInline1.address ||
          item.phone === formInline1.phone ||
          item.attitude === formInline1.attitude,
  )
  console.log('***********************')
  console.log(filteredData)
  transData.value = filteredData
  // data = data.filter((item) => item.order_id === Number(formInline1.order_id))
  // console.log(data)
}
</script>

<style scoped lang="scss">
.header {
  display: flex;
  padding: 16px 16px 0 16px;
  margin-bottom: 16px;
  border-radius: 4px;
  background: white;
  box-shadow: 0 0 12px rgb(0 0 0 / 5%);
}

.footer {
  flex: 1;
  display: flex;
  padding: 16px;
  flex-direction: column;
  border-radius: 4px;
  overflow: hidden;
  background: white;
  box-shadow: 0 0 12px rgb(0 0 0 / 5%);
}
</style>
