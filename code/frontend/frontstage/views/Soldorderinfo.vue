<!--<script>-->
<!--import soldorderinfo from "@/components/orderinfo/Soldorder.vue";-->
<!--</script>-->

<!--<template>-->
<!--  <soldorderinfo/>-->

<!--</template>-->

<!--<style scoped>-->

<!--</style>-->


<template>
  <div class="common-layout">
    <el-container>
      <el-main style="background: #FFFFFF">
        <br>
        <br>
        <div class="Opanel">
          <dt>下单成功</dt>
          <time class="time">{{ dateTime2str(new Date(), "yyyy-MM-dd hh:mm:ss") }}</time>
          <br><br>
          <dt>品读线上审核</dt>
          <time class="time">预计{{ dateTime2str(new Date(), "yyyy-MM-dd hh:mm:ss") }}前完成</time>
          <br><br>
          <dt>安排快递上门取件</dt>
          <time class="time">预计{{ dateTime2str(new Date(), "yyyy-MM-dd hh:mm:ss") }}前，无需支付快递费用
          </time>
          <br><br>
          <dt>快递取件</dt>
          <br>
          <dt>品读审核打款</dt>
          <time class="time">
            快递签收后1-3天完成验收审核。审核后，除去未收到和审核拒绝的书，将即刻打款到您的品读钱包
          </time>
          <br><br>
          <hr>
          <div class="booknum"><h2>共{{theOrderInfo.bookinfos.length}}本</h2></div>
          <hr>

          <div v-for="orderbook in theOrderInfo.bookinfos" class="books">
            <el-row :gutter="20">
              <el-col :span="6"><img class="images" :src="orderbook.bookcover" alt="no idea"/></el-col>
              <el-col :span="6" class="bookinfo">
                <div class="bookname">{{ orderbook.name}}({{orderbook.condition}})</div>
                <br>
                <div class="author">{{ orderbook.author }}</div>
              </el-col>
              <el-col :span="3" :offset="9" class="bookinfo">
                <div class="bookprice">￥{{ orderbook.price }}</div>
              </el-col>
            </el-row>
          </div>
          <hr>
          <br>
          <el-row :gutter="0">
            <router-link :to="{ name:'boughtbook'}">
              <el-button type="primary" :icon="ArrowLeft">返回</el-button>
            </router-link>
            <el-col :span="3" :offset="16">
              <div class="button">
                <el-button round text @click="feedbackdialog = true">联系客服</el-button>
              </div>
            </el-col>

          </el-row>

          <el-dialog v-model="feedbackdialog" title="联系客服">
            <el-form>
              <el-form-item label="问题反馈" :label-width="formLabelWidth">
                <el-input v-model="question"/>
              </el-form-item>
            </el-form>
            <template #footer>
      <span class="dialog-footer">
        <el-button @click="feedbackdialog = false">取消</el-button>
        <el-button type="primary"  @click="open1">
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
import {onMounted, reactive, ref} from "vue";
import image1 from "@/assets/pictures/sample10.jpg";
import image2 from "@/assets/pictures/sample11.jpg";
import {ArrowLeft, ArrowRight} from "@element-plus/icons-vue";
import {ElMessage, ElNotification} from "element-plus";
import {feedback, getbuyorderdetail, getsellorderdetail} from "../api/orderDetails"
const question = ref('')
const formLabelWidth = '140px'
const feedbackdialog = ref(false)
let oid=ref('')


const open1 = () => {
  const uid = window.sessionStorage.getItem("id")
  console.log(question.value)
  console.log(uid)

  feedback(uid,question.value)

  console.log(feedbackdialog)
  feedbackdialog.value = false
  console.log(feedbackdialog)
  console.log(question)

  ElNotification({
    title: 'Success',
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

const theOrderInfo=reactive({
  bookinfos:[{
    bookcover:'',
    isbn:'',
    condition:'',
    name: '',
    author: '',
    price: '',
    num:1
  }],
  submitTime:''
  })
const time=ref('')


function sumbook_num(bookinfo){
  let p=0;
    for(let i=0;i<bookinfo.length;i++){
      p=p+bookinfo[i].num
  }
return p
}
function getoidFromUrl(str) {
  const index = str.lastIndexOf('info/');
  if (index !== -1) {
    return str.substring(index + 5);
  }
  return '';
}
onMounted(() => {
   oid= getoidFromUrl(window.location.pathname),
  console.log(oid);

  getsellorderdetail(oid).then((r) => {
    console.log(r.data)
    theOrderInfo.bookinfos = r.data.map(s => {
      return {
        condition: s["customer_condition"],
        price: s["predict_price"],
        isbn: s["book_isbn"],
        name:s["book_name"],
        author:s["book_writer"],
        bookcover:s["book_picture"],

      }
    })
    console.log("bookinfos", theOrderInfo.bookinfos)
  })
})
//isbn=>bookname,author
</script>

<style scoped>
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