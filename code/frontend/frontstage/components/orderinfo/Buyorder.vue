<template>
  <div class="common-layout" v-if="load">
    <el-container>
      <el-main style="background: #FFFFFF">
        <br>
        <br>
        <div class="Opanel">
          <dt>下单成功</dt>
          <time class="time">{{ dateTime2str(new Date(), "yyyy-MM-dd hh:mm:ss") }}</time>
          <br><br>
          <dt>平台发货</dt>
          <time class="time">预计{{ dateTime2str(new Date(), "yyyy-MM-dd hh:mm:ss") }}前，无需支付快递费用
          </time>
          <br><br>
          <dt>运输中</dt>
          <br>
          <dt>订单已签收</dt>
          <time class="time">
            快递签收后1-3天完成验收审核。审核后，除去未收到和审核拒绝的书，将即刻打款到您的品读钱包
          </time>

          <br><br>
          <hr>
          <div class="booknum"><h2>共{{ sumbook_num(theOrderInfo.bookinfos) }}本</h2></div>
          <hr>

          <div v-for="orderbook in theOrderInfo.bookinfos" class="books">
            <el-row :gutter="20">
              <el-col :span="6"><img class="images" :src="orderbook.bookcover" alt="no idea"/></el-col>
              <el-col :span="6" class="bookinfo">
                <div class="bookname">{{ orderbook.name }}({{ orderbook.condition }})</div>
                <br>
                <div class="author">{{ orderbook.author }}</div>
              </el-col>
              <el-col :span="3" :offset="9" class="bookinfo">
                <div class="bookprice">{{ orderbook.num }}本<br>￥{{ orderbook.price * orderbook.num }}
                </div>
              </el-col>
            </el-row>
          </div>
          <hr>
          <br>
          <el-row :gutter="0">
            <el-col>
              <router-link :to="{ name:'home'}">
                <el-button type="primary" :span="3">
                  返回至主页
                </el-button>
              </router-link>
            </el-col>
            <el-col :span="3" :offset="22">
              <div class="button">
                <el-button type="primary" round @click="feedbackdialog = true">联系客服</el-button>
              </div>
            </el-col>

          </el-row>

          <el-dialog v-model="feedbackdialog" title="联系客服">
            <el-form>
              <el-form-item label="问题反馈" :label-width="formLabelWidth">
                <div style="margin: 20px 0;"></div>
                <el-input
                    type="textarea"
                    placeholder="请输入内容"
                    v-model="question"
                    minlength="10"
                    maxlength="300"
                    show-word-limit
                    :rows="7"
                    style="height: 140px;"
                >
                </el-input>
              </el-form-item>
            </el-form>
            <template #footer>
      <span class="dialog-footer">
        <el-button @click="feedbackdialog = false">取消</el-button>
        <el-button type="primary" plain @click="open1">
          确定
        </el-button>
      </span>
            </template>
          </el-dialog>


          <br><br>
        </div>
      </el-main>
    </el-container>
  </div>
</template>

<script setup>
import {onBeforeMount, onMounted, reactive, ref} from "vue";
import image1 from "@/assets/pictures/sample10.jpg";
import image2 from "@/assets/pictures/sample11.jpg";
import {ArrowLeft, ArrowRight} from "@element-plus/icons-vue";
import {ElMessage, ElNotification} from "element-plus";
import {getdbbook} from "../../api/GetBookService";
import {feedback, getbuyorderdetail, getsellorderdetail} from "../../api/orderDetails"

const load = ref(false)
const question = ref('')
const formLabelWidth = '140px'
const feedbackdialog = ref(false)

const open1 = () => {
  const uid = window.sessionStorage.getItem("id")
  // console.log(question.value)
  // console.log(uid)

  feedback(uid, question.value)

  // console.log(feedbackdialog)
  feedbackdialog.value = false
  // console.log(feedbackdialog)
  // console.log(question)
  if (question.value === '') {
    ElNotification({
      title: '失败啦',
      message: '请在输入栏中输入您的问题！',
      type: 'error',
    })
  } else
    ElNotification({
      title: '成功啦',
      message: '已将您的意见发给专员，将在1-3个工作日内回复您！',
      type: 'success',
    })
}

function dateTime2str(dateTime, format) {
  var z = {
    y: dateTime.getFullYear(),
    M: dateTime.getMonth() + 1,
    d: dateTime.getDate(),
    h: dateTime.getHours(),
    m: dateTime.getMinutes(),
    s: dateTime.getSeconds()
  };
  return format.replace(/(y+|M+|d+|h+|m+|s+)/g, function (v) {
    return ((v.length > 1 ? "0" : "") + eval('z.' + v.slice(-1))).slice(-(v.length > 2 ? v.length : 2))
  });
}

const theOrderInfo = reactive({
  bookinfos: [{
    bookcover: '',
    isbn: '',
    condition: '',
    name: '',
    author: '',
    price: '',
    num: 0,
  }],
  submitTime: ''
})

const time = ref('')
const name5 = history.state.data
const oid = name5[0].order_id

function sumbook_num(bookinfo) {
  let p = 0;
  for (let i = 0; i < bookinfo.length; i++) {
    p = p + bookinfo[i].num
  }
  return p
}


onMounted(() => {
      setTimeout(() => {
        getbuyorderdetail(oid).then((r) => {
              console.log("name5", name5)
              theOrderInfo.bookinfos = r.data.map(s => {
                return {
                  condition: s["inventory_conditionrate_condition"],
                  price: s["order_book_price"],
                  isbn: s["inventory_book_isbn"],
                  name: s["inventory_book_name"],
                  author: s["inventory_book_writer"],
                  bookcover: s["inventory_book_picture"],
                  num: s["book_num"],
                }
              })
            })
        load.value = true
      }, 2000)
      console.log("bookinfos", theOrderInfo.bookinfos)

    }
)
//isbn=>bookname,author
</script>

<style scoped>
.time {
  color: black;
}


.title {
  font-size: 30px;
  color: white;
}

.Opanel {
  background-color: white;
  padding-left: 50px;
}

.booknum {
  padding: 50px 0px;
  font-weight: bold;
  color: #000000;
}

dt {
  font-weight: bold;
  color: #000000;
}

.images {
  height: 300px;
  width: 300px;
}

.bookinfo {
  padding: 50px 0;
  color: #000000;
}

.bookname {
  font-size: large;
  font-weight: bold;
  color: #000000;
}

.author {
  font-size: small;
  color: #000000;
}

.bookprice {
  font-size: 30px;
  font-weight: bold;
  color: #000000;
}
.time{
  color: black;
}
</style>