<template>
  <div>
    <el-card class='box-card' style="margin-left: auto; margin-right: auto">
      <div style="padding: 14px">
        <el-row :gutter="20">
          <el-col :span="15">
            <h2 style="display: inline-block">寄件人信息</h2>
          </el-col>
          <el-col :span="3" :offset="6">
            <router-link :to="{name: 'warehouse'}">
              <el-button class="button">返回上一级</el-button>
            </router-link>
          </el-col>
        </el-row>
      </div>
      <div style="padding-left: 30px">
        <el-radio-group v-model="radio1">
          <el-row>
            <el-col>
              <div v-for="item in addresses" :key="item.id">
                <el-radio class="address-radio" :label="item.id">{{ item.receiver_name }} - {{ item.receiver_phone }} -
                  {{ item.receiver_region }} - {{ item.receiver_place }}
                </el-radio>
              </div>
            </el-col>

          </el-row>
        </el-radio-group>
      </div>
      <br/>
      <hr/>

      <!-- 取件时间 -->
      <div style="padding: 14px">
        <h2>取件时间</h2>
        <div style="margin: 10px">
          <el-time-select
              v-model="time_value"
              start="08:30"
              step="00:30"
              end="18:30"
              placeholder="选择取件时间"
          />
        </div>
      </div>
      <br/>
      <hr/>

      <!-- 书目信息 -->
      <div style="padding: 14px">
        <h2>书目信息</h2>
        <div v-for="item in book_data">
          <el-card :body-style="{ padding: '0px' }">
            <div style="padding: 14px">
              <el-row :gutter="10">
                <el-col :span="3">
                  <img :src="item.img" width="120" height="120">
                </el-col>
                <el-col :span="19">
                  <p>{{ item.name }}</p>
                  <p style="color:dimgrey">{{ item.writer }}</p>
                  <p style="color:goldenrod">{{ item.pinxiang }}</p>
                </el-col>
                <el-col :span="2">
                  <p>￥ {{ item.price }}</p>
                </el-col>
              </el-row>
            </div>
          </el-card>
        </div>
      </div>
    </el-card>

    <!-- 交钱 -->
    <el-card class="box-card"
             style="margin-right: auto; margin-left: auto; background-color: #474747; border-color: #474747">
      <el-row :gutter="20" justify="end">
        <el-col>
          <div>
            <el-row>
              <el-col :span="6">
                <p class="letter" style="font-size: large">预收金额:</p>
              </el-col>
              <el-col :span="6">
                <div>
                  <p class="letter" style="font-size: large; color: yellow">￥ {{ totalprice }}</p>
                </div>
              </el-col>
            </el-row>
          </div>
        </el-col>
      </el-row>
      <div class="bottom">
        <time class="time">{{ currentDate }}</time>
        <el-button text class="button" @click="addSellOrderDetail" style="background-color: red; color:white; font-weight: bold; font-size: large">
          提交订单
        </el-button>
      </div>
    </el-card>
  </div>
</template>

<script lang="ts" setup>
import {onMounted, reactive, ref} from 'vue'
import {FormRules} from 'element-plus'
import {addUserAddress, loadUserAddress} from "../api/userAddressService"
import {createSellOrder, createSellOrderDetail, loadSellOrder, loadSellOrderDetail} from "../api/OrderService"
import {useRoute, useRouter} from "vue-router";
import {deleteWareHouseBook} from "../api/WareHouseBookServer"

const router = useRouter()
const radio1 = ref(undefined)
const radio2 = ref('1')
const radio3 = ref('1')
const radio4 = ref('1')
const checkList = ref(['Option A'])
let dialogFormVisible = ref(false)
const formLabelWidth = '140px'
const route = useRoute()
let book_data = JSON.parse(Object(route.query.myArray))
let totalprice = ref(0)

onMounted(() => {
  console.log("nihao")
  loadUserAddress(window.sessionStorage.getItem("id")).then((r) => {
        addresses.value = r.data
        console.log(addresses.value)
      }
  )
  total_price()
  console.log(book_data)
})

const form = reactive({
  name: '',
  region: '',
  place: '',
  phone: '',
})

const time_value = ref('')

const addresses = ref()

function addAddress() {
  if (form.name === '' || form.phone === '' || form.region === '' || form.place === '') {
    console.log("error")
  } else {
    const data = {
      user_id: window.sessionStorage.getItem("id"),
      receiver_name: form.name,
      receiver_phone: form.phone,
      receiver_region: form.region,
      receiver_place: form.place
    }
    console.log(data)
    addUserAddress(data)
    dialogFormVisible.value = false;
    location.reload()
  }
}

const rules = reactive<FormRules>({
  name: [
    {required: true, message: '请填写收货人姓名', trigger: 'blur'},
    {min: 3, max: 5, message: '输入格式有误', trigger: 'blur'},
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

const options = Array.from({length: 10000}).map((_, idx) => ({
  value: `${idx + 1}`,
  label: `${idx + 1}`,
}))

const total_price = () => {
  let sum = 0
  book_data.forEach(t => {
    sum += Number(t.price)
    console.log(t.price)
  })
  totalprice.value = sum
}

let sendData = {}

async function addSellOrder() {
  const system_time = new Date()

  //sell_order的data
  const so_data = {
    user_id: window.sessionStorage.getItem("id"),
    useraddress_id: radio1.value,
    status: 0,
    finish_time: null,
    submit_time: system_time.getTime(),
  }
  sendData = {...so_data}
  console.log(so_data)
  console.log(radio1.value)
  return createSellOrder(so_data)
}

function addSellOrderDetail() {
  let order_id = null
  addSellOrder().then(resp => {
    console.log(resp.data)
    order_id = resp.data.id
    let sod_data = book_data.map(function (item) {
      return {book_isbn: item.isbn, predict_price: item.price, customer_condition: item.pinxiang}
    })

    sod_data.forEach(t => {
      t.final_price = null
      t.final_condition = null
      t.order_id = order_id
    })
    sendData = {...sendData, ...sod_data}
    console.log(sod_data)
    sod_data.forEach(t => {
      createSellOrderDetail(t)
    })

    router.push({name: 'sellorder', state: {data: sendData}})

    //删除卖书库中的对应信息
    //todo 用户地址没进入数据库
    const deltodb = book_data
    console.log("要删除的数据", deltodb)

    let delId = deltodb.map(s => {
      return {
        warehouseid: s["id"],
      };
    })

    console.log("要删除的id", delId)
    delId.forEach((item) => {
      console.log("准备删除的id为", item.warehouseid)
      deleteWareHouseBook(item.warehouseid)
    })
  })

}
</script>


<style scoped>
.box-card {
  padding: 0;
  width: 1200px;
}

.time {
  font-size: 12px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.button {
  padding: 0;
  min-height: auto;
  border-radius: 5px
}

.image {
  width: 100%;
  display: block;
}

.letter {
  color: #f2f2f2;
  font-weight: bold
}

.address-radio {
  display: block;
  margin: 10px 0;
}
</style>