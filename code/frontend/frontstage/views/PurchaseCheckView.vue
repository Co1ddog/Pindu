<template>
  <div>
    <el-card class='box-card' style="margin-left: auto; margin-right: auto">
      <div style="padding: 14px">
        <el-row :gutter="20">
          <el-col :span="3">
            <h2 style="display: inline-block">收货人信息</h2>
          </el-col>
          <el-col :span="12">
            <el-button class="button" style="border:none; color:blue" @click="dialogFormVisible = true">新增收货人地址
            </el-button>

            <el-dialog v-model="dialogFormVisible" title="新增收货人地址">
              <el-form
                  :model="form"
                  ref="ruleFormRef"
                  :rules="rules"
                  label-width="120px"
                  class="demo-ruleForm"
                  :size="formSize"
                  status-icon
              >
                <el-form-item label="收件人姓名" :label-width="formLabelWidth" prop="name">
                  <el-input v-model="form.name" autocomplete="off"/>
                </el-form-item>

                <el-form-item label="联系方式" :label-width="formLabelWidth" prop="phone">
                  <el-input v-model="form.phone" autocomplete="off"/>
                </el-form-item>

                <el-form-item label="省市" :label-width="formLabelWidth" prop="region">
                  <el-select v-model="form.region" placeholder="选择省市" :options="options">
                    <el-option label="上海市" value="上海市"/>
                    <el-option label="北京市" value="北京市"/>
                    <el-option label="天津市" value="天津市"/>
                    <el-option label="甘肃省" value="甘肃省"/>
                  </el-select>
                </el-form-item>

                <el-form-item label="详细地址" :label-width="formLabelWidth" prop="place">
                  <el-input v-model="form.place" autocomplete="off" placeholder="区、县/街道/门牌号"/>
                </el-form-item>
              </el-form>


              <template #footer>

      <span class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取消</el-button>


        <el-button type="primary"
                   @click="addAddress()">添加</el-button>
      </span>
              </template>
            </el-dialog>
          </el-col>
          <el-col :span="3" :offset="6">
            <router-link :to="{name: 'cart'}">
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
                <el-radio class="address-radio" :value="item.id" :label="item.id">{{ item.receiver_name }} -
                  {{ item.receiver_phone }} -
                  {{ item.receiver_region }} - {{ item.receiver_place }}
                </el-radio>
              </div>
            </el-col>

          </el-row>
        </el-radio-group>
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
                  <p style="color:dimgrey">{{ item.author }}</p>
                  <p style="color:goldenrod">{{ item.pinxiang }}</p>
                </el-col>
                <el-col :span="2">
                  <p align="right">￥ {{ item.price }}/本</p>
                  <p style="color: dimgrey" align="right">{{ item.quantity }}本</p>
                  <p align="right">总计￥ {{ ((item.price * item.quantity).toFixed(2)) }}</p>
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
                <p class="letter" style="font-size: large">应付金额:</p>
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
        <!--        <RouterLink to="/Buyorderinfo">-->
        <el-button text class="button" @click="isAbleToBuy"
                   style="background-color: red; color:white; font-weight: bold; font-size: large">
          提交订单
        </el-button>
        <!--        </RouterLink>-->
      </div>
    </el-card>
  </div>
</template>

<script lang="ts" setup>
import {onMounted, reactive, ref} from 'vue'
import {FormRules} from 'element-plus'
import {addUserAddress, loadUserAddress} from "../api/userAddressService"
import {useRoute, useRouter} from "vue-router";
import {createBuyOrder, createBuyOrderDetail} from "../api/OrderService"
import {deleteCartBook} from "../api/CartBookServer"
import {userDetail, userModify} from "../api/userService";

const radio1 = ref(undefined)
const radio2 = ref('1')
const radio3 = ref('1')
const radio4 = ref('1')
const checkList = ref(['Option A'])
let dialogFormVisible = ref(false)
const formLabelWidth = '140px'
const route = useRoute()
const router = useRouter()
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
  userDetail(window.sessionStorage.getItem("id")).then((r) => {
    console.log(r.data.balance)
  })
  console.log(totalprice)
  console.log(book_data)
})

const form = reactive({
  name: '',
  region: '',
  place: '',
  phone: '',
})

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
    sum += Number((t.price) * t.quantity)
    console.log(t.price)
  })
  totalprice.value = Number(sum.toFixed(2))
}

let sendData = {}

async function addBuyOrder() {
  const system_time = new Date()

  //buy_order的data
  const bo_data = {
    user_id: window.sessionStorage.getItem("id"),
    useraddress_id: radio1.value,
    status: 0,
    finish_time: null,
    submit_time: system_time.getTime(),
  }
  sendData = {...bo_data}
  console.log(bo_data)
  console.log(radio1.value)
  return createBuyOrder(bo_data)
}

function addBuyOrderDetail() {
  let order_id = null

  addBuyOrder().then(async resp => {
    console.log(resp.data)
    order_id = resp.data.id
    console.log(resp.data.id)
    // console.log(order_id)
    let bod_data = book_data.map(function (item) {
      return {
        book_num: item.quantity, order_book_price: item.price, inventory_book_isbn: item.isbn,
        inventory_conditionrate_condition: item.pinxiang
      }
    })

    bod_data.forEach(t => {
      t.order_id = order_id
    })
    sendData = {...sendData, ...bod_data}
    console.log(bod_data)
    bod_data.forEach(t => {
      createBuyOrderDetail(t)
    })

    router.push({name: 'Buyorder', state: {data: sendData}})

    //用户钱包扣钱
    const u_id = window.sessionStorage.getItem("id")
    let old_balance = 0
    await userDetail(u_id).then(r => {
      old_balance = r.data.balance
    })
    const new_balance = old_balance - totalprice.value
    console.log("oldbal:", old_balance)
    console.log("newbal:", new_balance)
    userModify(u_id, {balance: new_balance}).then(r => {
      console.log("r.data:", r.data)
    })

    //删除购物车中的对应信息
    const deltodb = book_data
    console.log("要删除的数据", deltodb)

    let delId = deltodb.map(s => {
      return {
        cartid: s["cartid"],
      };
    })

    console.log("要删除的id", delId)
    delId.forEach((item) => {
      console.log("准备删除的id为", item.cartid)
      deleteCartBook(item.cartid)
    })
  })
}

function isAbleToBuy() {
  const user_id = window.sessionStorage.getItem("id")
  userDetail(user_id).then(resp => {
    console.log(Number(resp.data.balance), totalprice.value)
    if (Number(resp.data.balance) < Number(totalprice.value)) {
      alert("余额不足")
    } else {
      addBuyOrderDetail()
    }
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