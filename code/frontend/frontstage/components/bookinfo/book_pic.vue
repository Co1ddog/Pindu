<template>
  <el-breadcrumb :separator-icon="ArrowRight"
                 style="background-color:ghostwhite;  padding-top: 22px;padding-bottom: 30px;padding-left: 30px;font-size: large">
    <el-breadcrumb-item :to="{ path: '/' }">主页</el-breadcrumb-item>
    <el-breadcrumb-item :to="{ name:'shop'}">商城</el-breadcrumb-item>
    <el-breadcrumb-item>图书信息详情</el-breadcrumb-item>
  </el-breadcrumb>
  <div id="bookpic">
    <img :src=book.pict alt="no">
  </div>
  <div class="infos">
    <el-row>
      <el-col span="2">
        <el-text class="name" size="large" style="float:left">{{ book.b_name }}</el-text>
      </el-col>
    </el-row>
    <el-dialog v-model="dialogFormVisible" title="购买界面">
      <el-form>
        <el-form-item label=选择品相 :label-width="formLabelWidth">
          <el-select placeholder="选择品相" v-model="bookPost.inventory_conditionrate_name">
            <el-option v-for="condition in condition_inventory"
                       :key="condition.id"
                       :label="condition.condition_rate+'￥'+ Number(book.b_price*condition.buy_rate).toFixed(2)"
                       :value="condition.condition_rate">
            </el-option>
          </el-select>
        </el-form-item>
        <!--      <el-form-item name='num' label="数量" :label-width="formLabelWidth">-->
        <!--        <el-input v-model="book.b_conditions" autocomplete="off" />-->
        <!--      </el-form-item>-->
      </el-form>
      <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取消</el-button>
        <el-button type="primary" @click="open1(condition_inventory,bookPost)">
          确定
        </el-button>
      </span>
      </template>
    </el-dialog>


    <br><br>
    <div>
      <el-text class="price" style="font-size: 20px;float:left">
        ￥{{ Number(book.b_price * book.b_conditions[0].buy_rate).toFixed(2) }} ~
        ￥{{ Number(book.b_price * book.b_conditions[1].buy_rate).toFixed(2) }}
      </el-text>
      <div v-if="condition_inventory[0].condition_rate!=='此书无库存'">
        <el-button style="float: right" id="gwc" @click="dialogFormVisible=true"
        >添加至购物车
        </el-button>
      </div>
      <div v-else>
        <el-button disabled style="float: right">此书无库存</el-button>
      </div>
      <br><br><br>
    </div>
    <el-descriptions style=" padding-top: 10px " direction='vertical' :column="2" :border='true'>
      <el-descriptions-item label='品相'>
        <div v-for="condition in condition_inventory" :key="condition.id">
          <el-tag>{{ condition.condition_rate }}</el-tag>
        </div>
      </el-descriptions-item>
      <el-descriptions-item label="原价">
        ￥{{ book.b_price }}
      </el-descriptions-item>
      <el-descriptions-item label="ISBN">
        {{ book.b_isbn }}
      </el-descriptions-item>
      <el-descriptions-item label="作者">
        {{ book.b_writer }}
      </el-descriptions-item>
      <el-descriptions-item label='出版社'>
        {{ book.b_presshouse }}
      </el-descriptions-item>
      <el-descriptions-item label='出版时间'>
        {{ book.b_pressdate }}
      </el-descriptions-item>
      <el-descriptions-item label='类别'>
        {{ book.b_category }}
      </el-descriptions-item>
    </el-descriptions>
    <br><br>
    <div class="brief">
      <dl>
        <dt>内容简介:</dt>
        <dd style="font-size: large">
          {{ book.b_introduction }}
        </dd>
      </dl>
    </div>
    <br><br>

    <br><br>
    <dt>相关推荐</dt>
    <div v-if="display">
      <el-carousel height="360px" indicator-position="outside" autoplay>
        <el-carousel-item>
          <div class="outer">
            <div v-for="(val, ind) in page1" class="middle">
              <RouterLink :to="{name:'bookinfo',params:{isbn:val.isbn}}" style="text-decoration-line: none">
                <div class="inner" @click="handleClick(val.isbn)">
                  <img :src="val.picture" alt="" style="width: auto;height: 200px;">
                </div>
                <p class="name">{{ val.name }}</p>
                <p>{{ val.intro }}</p>
              </RouterLink>
            </div>
          </div>
        </el-carousel-item>

        <el-carousel-item>
          <div class="outer">
            <div v-for="(val, ind) in page2" class="middle">
              <RouterLink :to="{name:'bookinfo',params:{isbn:val.isbn}}" style="text-decoration-line: none">
                <div class="inner" @click="handleClick(val.isbn)">
                  <img :src="val.picture" alt="" style="width: auto;height: 200px;">
                </div>
                <p class="name">{{ val.name }}</p>
                <p>{{ val.intro }}</p>
              </RouterLink>
            </div>
          </div>
        </el-carousel-item>

        <el-carousel-item>
          <div class="outer">
            <div v-for="(val, ind) in page3" class="middle">
              <RouterLink :to="{name:'bookinfo',params:{isbn:val.isbn}}" style="text-decoration-line: none">
                <div class="inner" @click="handleClick(val.isbn)">
                  <img :src="val.picture" alt="" style="width: auto;height: 200px;">
                </div>
                <p class="name">{{ val.name }}</p>
                <p>{{ val.intro }}</p>
              </RouterLink>
            </div>
          </div>
        </el-carousel-item>

        <el-carousel-item>
          <div class="outer">
            <div v-for="(val, ind) in page4" class="middle">
              <RouterLink :to="{name:'bookinfo',params:{isbn:val.isbn}}" style="text-decoration-line: none">
                <div class="inner" @click="handleClick(val.isbn)">
                  <img :src="val.picture" alt="" style="width: auto;height: 200px;">
                </div>
                <p class="name">{{ val.name }}</p>
                <p>{{ val.intro }}</p>
              </RouterLink>
            </div>
          </div>
        </el-carousel-item>
      </el-carousel>
    </div>

    <!--      <el-row>&ndash;&gt;
    &lt;!&ndash;            <el-col&ndash;&gt;
    &lt;!&ndash;                    v-for="(o, index) in 3"&ndash;&gt;
    &lt;!&ndash;                    :key="o"&ndash;&gt;
    &lt;!&ndash;                    :span="6"&ndash;&gt;
    &lt;!&ndash;                    :offset="index > 0 ? 3 :0"&ndash;&gt;
    &lt;!&ndash;            >&ndash;&gt;
    &lt;!&ndash;                <el-card shadow="hover" :body-style="{ padding: '0px' }">&ndash;&gt;
    &lt;!&ndash;                    <img&ndash;&gt;
    &lt;!&ndash;                            src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"&ndash;&gt;
    &lt;!&ndash;                            class="image"&ndash;&gt;
    &lt;!&ndash;                    />&ndash;&gt;
    &lt;!&ndash;                    <div style="padding: 14px">&ndash;&gt;
    &lt;!&ndash;                        <span>Yummy hamburger</span>&ndash;&gt;
    &lt;!&ndash;                        <div class="bottom">&ndash;&gt;
    &lt;!&ndash;                            <time class="time">{{ currentDate }}</time>&ndash;&gt;
    &lt;!&ndash;                            <el-button type="danger" round>查看</el-button>&ndash;&gt;
    &lt;!&ndash;                        </div>&ndash;&gt;
    &lt;!&ndash;                    </div>&ndash;&gt;
    &lt;!&ndash;                </el-card>&ndash;&gt;
    &lt;!&ndash;            </el-col>&ndash;&gt;
    &lt;!&ndash;        </el-row>-->
  </div>


</template>


<script setup>

import {getdbbook, getBookCondition, getCartNum, getBookIsFlow} from "../../api/GetBookService";
import {onBeforeMount, reactive} from "vue";

const display = ref(false)
const router = useRouter()
const books = []
let shuffled_books = reactive([])

const handleClick = (isbn) => {
  router.push('/')
}

let page1 = reactive([])
let page2 = reactive([])
let page3 = reactive([])
let page4 = reactive([])

const shuffle = (arr) => {
  let l = arr.length;
  let index, temp;
  while (l > 0) {
    index = Math.floor(Math.random() * l)
    temp = arr[l - 1]
    arr[l - 1] = arr[index]
    arr[index] = temp
    l--
  }
  return arr
}

onBeforeMount(async () => {
  await getBookIsFlow().then(r => {
    r.data.forEach((e, i) => books.push(e))
  })

  shuffled_books = shuffle(books)
  page1 = shuffled_books.slice(0, 3)
  page2 = shuffled_books.slice(5, 8)
  page3 = shuffled_books.slice(10, 13)
  page4 = shuffled_books.slice(15, 18)
  display.value = true
  console.log(page1)
})


const currentDate = ref(new Date())
import {onMounted, ref} from 'vue'
// import {getBookInventory} from "../../api/bookService";
import {ElNotification, selectKey} from "element-plus";
// import bookService from "../../api/bookService"
const dialogFormVisible = ref(false)
const formLabelWidth = '140px'
import pic1 from '@/assets/test1.webp'
import {getBookInventory} from "../../api/GetBookService";
import * as GetBookservice from "../../api/bookService";
import {postbooktoCart} from "../../api/CartBookServer"
import {ArrowRight} from "@element-plus/icons-vue";
import {useRouter} from "vue-router";

const bookPost = reactive({
      user_id: window.sessionStorage.getItem("id"),
      inventory_book_isbn: getIsbnFromUrl(window.location.pathname),
      inventory_conditionrate_name: '',
      book_num: '1'
    }
)


const book = reactive({
  pict: '',
  b_conditions: [
    {id: '', condition: '', buy_rate: ''},
    {id: '', condition: '', buy_rate: ''}],
  b_isbn: "",
  b_name: '',
  b_price: '',
  b_writer: '',
  b_category: '',
  b_introduction: '',
  b_presshouse: '',
  b_pressdate: '',
})

const open1 = (condition_inventory, bookPost) => {
  const user_id = window.sessionStorage.getItem("id")
  let cart_num1
  let condition
  if (bookPost.inventory_conditionrate_name === '中等') {
    condition = 0
  } else {
    condition = 1
  }
  console.log(condition)
  // console.log(condition_inventory[condition].total)
  getCartNum(user_id, bookPost.inventory_book_isbn, bookPost.inventory_conditionrate_name).then((r) => {
        console.log(r.data)
        cart_num1 = r.data
        console.log(cart_num1.book_num)
        if (cart_num1.book_num >= condition_inventory[condition].total) {
          console.log(cart_num1.book_num >= condition_inventory[condition].total)
          ElNotification({
            title: '失败啦',
            message: '所加入购物车数量大于库存。',
            type: 'error',
          })
        }
        if (cart_num1.book_num < condition_inventory[condition].total) {
          console.log(cart_num1.book_num < condition_inventory[condition].total)
          postbooktoCart(bookPost).then((r) => {
            return r.data
          })
          dialogFormVisible.value = false
          ElNotification({
            title: '成功啦',
            message: '添加购物车成功，点击购物车界面进行结算，有兴趣可以继续逛逛！',
            type: 'success',
          })
        }
      }
  ).catch((r) => {
    if (bookPost.inventory_conditionrate_name === '') {
      ElNotification({
        title: '失败啦',
        message: '没有选择品相！。',
        type: 'error',
      })
    } else {
      postbooktoCart(bookPost).then((r) => {
        return r.data
      })
      dialogFormVisible.value = false
      ElNotification({
        title: '成功啦',
        message: '添加购物车成功，点击购物车界面进行结算，有兴趣可以继续逛逛！',
        type: 'success',
      })
    }
  })

}
const condition_inventory = ref([
  {
    condition_rate: '',
    total: '',
    buy_rate: '',
  }
])

function getIsbnFromUrl(url) {
  const regex = /\/([^\/]+)$/;
  const matches = url.match(regex);
  if (matches && matches.length > 1) {
    return matches[1];
  }
  return null;
}

function refresh() {
  location.reload()
}

onMounted(() => {
  book.b_isbn = getIsbnFromUrl(window.location.pathname)
  getdbbook(book.b_isbn).then((r) => {
    // console.log(r.data)
    book.pict = r.data.picture
    book.b_name = r.data.name
    book.b_price = r.data.price
    book.b_writer = r.data.writer
    book.b_category = r.data.category
    book.b_introduction = r.data.intro
    book.b_presshouse = r.data.presshouse
    book.b_pressdate = r.data.pressdate
  })

})

onMounted(() => {
  getBookCondition().then((r) => {
    console.log(r.data)
    book.b_conditions[0] = r.data[0]
    book.b_conditions[1] = r.data[1]
  })
})
onMounted(() => {
  book.b_isbn = getIsbnFromUrl(window.location.pathname)
  getBookInventory(book.b_isbn).then((r) => {
    console.log(r.data)
    condition_inventory.value = r.data
    if (condition_inventory.value.length === 2) {
      condition_inventory.value[0].buy_rate = book.b_conditions[0].buy_rate
      condition_inventory.value[1].buy_rate = book.b_conditions[1].buy_rate
      condition_inventory.value[0].condition_rate = '中等'
      condition_inventory.value[1].condition_rate = '优良'
    }
    if (condition_inventory.value.length === 1 && condition_inventory.value[0].condition_rate === 1) {
      condition_inventory.value[0].buy_rate = book.b_conditions[0].buy_rate
      condition_inventory.value[0].condition_rate = '中等'
    }
    if (condition_inventory.value.length === 1 && condition_inventory.value[0].condition_rate === 2) {
      condition_inventory.value[0].buy_rate = book.b_conditions[1].buy_rate
      condition_inventory.value[0].condition_rate = '优良'
    }

  })
})
</script>
<style scoped>

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
}

.image {
  width: 200px;
  height: 200px;
  display: block;
}

.brief {
  text-align: left;
}

dt {
  text-align: left;
  font-size: 20px;
  color: white;
}

.brief dd {
  color: white;
  font-size: 10px;
}

#el-carousel__item {
  text-align: center;
}

.labels {
  background: red;
}

.name {
  color: white;
  font-size: 30px;
}

.infos {
  background-color: transparent;
  text-align: center;
  size: 200px;
  padding: 20px 300px;
}

.price {
  color: yellow;
  font-size: 30px;
}

#zoumadeng {
  height: 700px;
}

#bookpic {
  text-align: center;
  border-right: solid 1px var(--el-border-color);
  width: 100%;
  height: 100%;
  box-sizing: border-box;
  vertical-align: center;
}

.el-carousel__item:nth-child {
  color: #2c3e50;
  size: inherit;
  width: 100%;
  height: 100%;
}

img {
  /*设置图片宽度和浏览器宽度一致*/
  width: 480px;
  height: 640px;
  text-align: center;
}

.card-header {
  display: flex;
  justify-content: space-between;
  color: white;
}

.text {
  color: white;
  font-size: 14px;
}

#gwc {
  background-color: red;
  color: white;

}


.firstname {
  padding: 20px 300px;
}

.picture {
  height: 640px;
}

.outer {
  display: -webkit-flex;
  display: flex;
  -webkit-justify-content: space-around;
  justify-content: space-around;
  padding: 15px 10px;
}

.middle {
  height: 350px;
  width: 370px;
  background-color: #282828;
}

.inner {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 96%;
  margin-left: 2%;
  background-color: white;
}
p {
  padding: 3px 15px;
  color: white;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 4;
  overflow: hidden;
}
.name {
  color: #f2f2f2;
  font-size: large;
  font-weight: bold;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 1;
  overflow: hidden;
  padding-bottom: 0;
  padding-top: 6px;
}
</style>
