<template>
  <div class="box-card">
    <div class="wrap clearfix">
      <div class="location">当前位置：首页<span>&gt;</span><b class="red">卖书库</b></div>

      <div class="insertBook" id="insertBook">
        <el-input id="input1" type="text" placeholder="请输入ISBN号" v-model="inputtext"
                  @keydown.enter="findbookinfo()"></el-input>
      </div>
      <div class="insertbutton" id="insertBook">
        <el-button :icon="Search" round @click="findbookinfo()">添加书籍</el-button>
        <el-dialog
            v-model="centerDialogVisible"
            title="图书"
            width="60%"
            align-center
        >
          <el-form
              :model="form"
              ref="ruleFormRef"
              class="demo-ruleForm"
              status-icon
          >
            <div ref="test" class="test">

              <p id="bookdata" style="color: black">
                <img :src="bookinfo.img" width="300" height="300"/><br>
                书名：<a class="booktitle">{{ bookinfo.title }}</a><br>
                作者：<a class="bookauthor">{{ bookinfo.author }}</a><br>
                译者：<a>{{ bookinfo.translator }}</a><br>
                ISBN号：<a class="bookisbn">{{ bookinfo.isbn }}</a><br>
                价格：<a class="bookprice">{{ bookinfo.price }}</a><br>
                类别：<a class="bookcategory">{{ bookinfo.category }}</a><br>
                出版时间：<a class="bookpubdate">{{ bookinfo.pubdate }}</a><br>
                出版社：<a class="bookpublisher">{{ bookinfo.publisher }}</a><br>
                概要：<a class="booksummary">{{ bookinfo.summary }}</a><br>
              </p>

              <a class="red">请选择您的图书品质:&nbsp&nbsp</a>

              <el-select v-model="pinxiang" placeholder="选择品相" :options="options" @change="selectProductType">
<!--                <el-option label="全新" value="全新"/>-->
                <el-option label="优良" value="优良"/>
                <el-option label="中等" value="中等"/>
              </el-select>
            </div>
          </el-form>

          <template #footer>
      <span class="dialog-footer">
        <el-button @click="centerDialogVisible = false">取消</el-button>

        <el-button type="primary" @click="insertbook()">
          确认
        </el-button>
      </span>
          </template>
        </el-dialog>
      </div>
      <div>
        <table width="100%" class="cartTable" cellspacing="0" cellpadding="10px">

          <tr class="title" style="color: black">
            <td width="50"><input type="checkbox" name="" class="choose_all" v-model="isSelectedAll"></td>
            <td width="100" class=""><span style="margin-left: -10px;">全选</span></td>
            <td width="200"> 商品信息</td>
            <td width="100">品相</td>
            <td width="150"></td>
            <td width="148"></td>
            <!--            <td width="150">单价（元）</td>-->
            <!--            <td width="148">数量</td>-->
            <td width="150">金额（元）</td>
            <td width="80">操作</td>
          </tr>


          <tr v-for="(item, index) in cartData" :key="item.id" class="row">
            <td><input type="checkbox" class="choose" v-model="item.isSelected"></td>
            <td class="tal"><a href="#" class="pic"><img :src=item.img alt="picture" width="100"
                                                         height="100"></a>

            </td>

            <td class="tal"><a href="#">{{ item.name }}</a></td>
            <td class="tal"><a href="#">{{ item.pinxiang }}</a></td>
            <td class="tal"></td>
            <td class="tal"></td>
            <!--            <td class="unit">{{ item.price }}</td>-->
            <!--            <td>-->
            <!--              <div class="amount">-->
            <!--                <el-row class="amount-row">-->

            <!--                  <el-button href="#" class="Reduce" size="default" @click="reduceQuantity(index)">-</el-button>-->


            <!--                  <input type="text" class="unum" v-model="item.quantity" @blur="checkQuantity(index)"/>-->


            <!--                  <el-button class="Increase" href="#" size="default" @click="addQuantity(index)">+</el-button>-->

            <!--                </el-row>-->

            <!--              </div>-->
            <!--            </td>-->
            <td style="color: black"><b class="u-price"> {{ (item.price * item.quantity).toFixed(2) }} </b></td>
            <td>
              <el-button class="btn-del" type="danger" plain @click="removeProduct(index)">删除</el-button>
            </td>
          </tr>


          <tr class="count">
            <td colspan="7" class="delbutton">

              <el-button class="del_check" type="danger" plain @click="removeSelectedProducts">删除</el-button>
            </td>
            <div class="jiesuan clearfix">
              <div class="right fr clearfix">
                <td>商品数量: <span class="t-number"><a class="red p-number">{{ totalQuantity }}</a>件</span>
                </td>
                <br>
                <td>商品总价: <span class="t-price"><a class="red p-number">{{ totalPrice }}</a></span></td>
                <router-link
                    :to="{name: 'sellcheck', query:{myArray: JSON.stringify(this.cartData.filter((item) => item.isSelected))}}">
                  <button class="btn pay fr" @click.native.prevent="handleSell">确认卖书</button>
                </router-link>
              </div>
            </div>
            <td></td>
          </tr>

        </table>

      </div>
    </div>
  </div>

</template>


<script>
// import pic1 from "../images/pic1.png"
// import pic2 from "../images/pic2.png"
// import pic3 from "../images/pic3.png"
// import requests from "npm/lib/commands/pkg";
import {fetchbookinfo} from "../../api/test";

import {onMounted, reactive, ref} from 'vue'
// import salebook from "@/api/salebook";
import {string as dialogFormVisible} from "i/lib/util";
import axios from "axios";
import {getdbbook, postbooktobook} from "../../api/GetBookService";
import {getoutbook, postbooktowarehouse, getSalebook, deleteWareHouseBook} from "../../api/WareHouseBookServer";

import salebook from "../../api/salebook";
import api from "../../api/api";

let pinxiang = ref()
const form = reactive({
  summary: '',
  name: '',
  translator: '',
  author: '',
  isbn: '',
  category: '',
  pubdate: '',
  publisher: '',
  price: '',
  img: '',
  pinxiang: '',
})

export default {
  data() {
    return {
      pinxiang: ref(),
      options: [
        {
          value: "优良",
          lable: "优良",
        },

        {
          value: "中等",
          label: "中等",
        },
      ],
      booktodb: reactive({
        user_id: "",
        name: "",
        writer: "",
        isbn: "",
        price: '',
        category: "",
        pressdate: "",
        presshouse: "",
        intro: "",
        picture: "",
        translator: "",
        customer_condition: "",
      }),
      // booktodb: {
      //   title: "",
      //   author: "",
      //   isbn: "",
      //   price: '',
      //   category: "",
      //   pubdate: "",
      //   publisher: "",
      //   summary: "",
      //   img: "",
      //   translator: "",
      //   pinxiang: "",
      // },
      bookinfo: {
        title: "",
        author: "",
        isbn: "",
        price: '',
        category: "",
        pubdate: "",
        publisher: "",
        summary: "",
        img: "",
        translator: "",
      },
      value: '',
      label: '',
      centerDialogVisible: ref(false),
      cartData: [{
        id: "",
        isbn: "",
        name: "",
        price: "",
        img: "",
        quantity: "",
        pinxiang: "",
        writer: "",
      }],
      delId: [{id: ""}],
      // cartData: [
      //   {
      //     // id: "1",
      //     name: "高性能MySQL",
      //     price: 30,
      //     quantity: 1,
      //     img: pic1,
      //     isSelected: false,
      //     pinxiang: "全新"
      //   },
      //   {
      //     // id: "2",
      //     name: "Vue.js设计与实践",
      //     price: 20,
      //     quantity: 2,
      //     img: pic2,
      //     isSelected: false,
      //     pinxiang: "优良"
      //   },
      //   {
      //     // id: "3",
      //     name: "信息系统分析与设计",
      //     price: 15,
      //     quantity: 1,
      //     img: pic3,
      //     isSelected: false,
      //     pinxiang: "垃圾"
      //   },
      // ],
      inputtext: "",
    };
  },
  mounted() {
    getSalebook(window.sessionStorage.getItem("id")).then((r) => {
      console.log("卖书库，数据库", r.data.length)
 if (r.data.length) {
      this.cartData = r.data.map(s => {
        console.log("初始价格", s["book_price"])
        console.log("比率", s["condition_rate_customerrate"])
        let fin_price;
        fin_price = s["book_price"] * s["condition_rate_customerrate"]
        console.log("最终价格", fin_price)
        return {
          id: s["id"],
          isbn: s["book_isbn"],
          name: s["book_name"],
          price: fin_price.toFixed(2),
          img: s["book_pic"],
          quantity: 1,
          pinxiang: s["condition_rate_name"],
          writer: s["book_writer"]
        };
      })
      console.log(this.cartData)
   } else {
        console.log("数组为空",this.cartData)

        this.cartData.pop()
        console.log(this.cartData)
      }
    });
  },


  computed: {
    totalPrice() {
      let total = 0;
      this.cartData.forEach((item) => {
        if (item.isSelected) {
          total += item.price * item.quantity;
        }
      });
      return total.toFixed(2);
    },

    totalQuantity() {
      let total = 0;
      this.cartData.forEach((item) => {
        if (item.isSelected) {
          total += item.quantity;
        }
      });
      return total;
    },
    isSelectedAll: {
      get() {
        let result = true;
        let t = 0;
        // for(;this.cartData[t]!=null;t++)
        // {
        //   if (!this.cartData[t].isSelected) {
        //     result = false;
        //   }}

        this.cartData.forEach((item) => {
          if (!item.isSelected) {
            result = false;
          }
        });
        return result;
      },
      set(value) {
        this.cartData.forEach((item) => {
          item.isSelected = value;
        });
      },
    },
  },
  methods: {
    handleSell() {
      const selectedItems = this.cartData.filter(item => item.isSelected);
      if (selectedItems.length === 0) {
        alert('请至少选择一个商品');
      } else {
        this.$router.push({
          name: 'sellcheck',
          query: {myArray: JSON.stringify(selectedItems)}
        });
      }
    },

    showTips() {
      alert('请至少选择一件商品')
    },
    selectProductType(data) {
      // 将data对象解构
      const {value, label} = data;
      this.label = label;
      this.value = value;
    },
    addToCartData(r) {
      for (let s of r.data) {
        this.cartData.push({
          name: s["book_name"],
          price: s["b_price"],
          img: s["book_pic"],
          quantity: 1,
          pinxiang: s["customer_condition"],
        });
      }
    },
    async fetchData() {
      // 调用 API 获取数据
      const res = await getSalebook()
      const data = await res.json()

      // 转换数据格式
      const newdata = data.map((p) => ({
        name: item.b_title,
        num: item.b_num,
        img: item.b_img,
        pinxiang: b_pinxiang,
        price: item.b_price
      }))

      // 存储数据
      this.cartData = newdata
    },


    // fetchData() {
    //   axios.get('/api/sale')
    //       .then(res => {
    //         // 将b_name和b_age字段提取出来
    //         const cartdata = res.data.map(item => {
    //           return {name: item.b_title, num: item.b_num, img: item.b_img, pinxiang: b_pinxiang, price: item.b_price}
    //         });
    //         // 存入组件的person属性中
    //         this.cartData = cartdata;
    //       })
    // },
    click: function (e) {
      console.log(e.target.cartData())
    },
    addQuantity(index) {
      this.cartData[index].quantity++;
    },
    reduceQuantity(index) {
      if (this.cartData[index].quantity > 1) {
        this.cartData[index].quantity--;
      }
    },
    checkQuantity(index) {
      if (this.cartData[index].quantity < 1) {
        this.cartData[index].quantity = 1;
      }
    },
    removeProduct(index) {
      console.log(this.cartData[index].id)
      deleteWareHouseBook(this.cartData[index].id)
      // getSalebook(window.sessionStorage.getItem("id")).then((r) => {
      //   console.log(window.sessionStorage.getItem("id"))
      //   console.log("删除后数据库",r.data)
      //
      //   this.cartData = r.data.map(s => {
      //     let fin_price;
      //     fin_price = s["book_price"] * s["condition_rate_customerrate"]
      //     // console.log("价格", s["price"])
      //     return {
      //       id: s["id"],
      //       isbn: s["book_isbn"],
      //       name: s["book_name"],
      //       price: fin_price,
      //       img: s["book_pic"],
      //       quantity: 1,
      //       pinxiang: s["condition_rate_name"],
      //       writer: s["book_writer"]
      //     };
      //   })
      //   console.log(this.cartData)
      // })
      this.cartData.splice(index, 1);
    },
    removeSelectedProducts() {
      const deltodb = this.cartData.filter((item) => item.isSelected)
      console.log("要删除的数据", deltodb)
      this.delId = deltodb.map(s => {
        return {
          id: s["id"],
        };
      })
      console.log("要删除的id", this.delId)
      this.delId.forEach((item) => {
        console.log("准备删除的id为", item.id)
        deleteWareHouseBook(item.id)
      })
      // getSalebook(window.sessionStorage.getItem("id")).then((r) => {
      //   console.log(window.sessionStorage.getItem("id"))
      //   console.log("删除后数据库",r.data)
      //
      //   this.cartData = r.data.map(s => {
      //     let fin_price;
      //     fin_price = s["book_price"] * s["condition_rate_customerrate"]
      //     // console.log("价格", s["price"])
      //     return {
      //       id: s["id"],
      //       isbn: s["book_isbn"],
      //       name: s["book_name"],
      //       price: fin_price,
      //       img: s["book_pic"],
      //       quantity: 1,
      //       pinxiang: s["condition_rate_name"],
      //       writer: s["book_writer"]
      //     };
      //   })
      //   console.log(this.cartData)
      // })
      this.cartData = this.cartData.filter((item) => !item.isSelected);
    },
    chufa() {
      console.log(this.cartData.filter((item) => item.isSelected))
    },
    insertbook() {
      this.centerDialogVisible = false;
      // fetchbookinfo(this.inputtext).then(res => {
      //   console.log(res.data);
      //   let res1 = res;
      //   console.log(res1.data.data.summary);
      //   console.log(res1.data.data.title);
      //   console.log(res1.data.data.author);
      //   console.log(res1.data.data.isbn);
      //   console.log(res1.data.data.price);
      //   console.log(res1.data.data.publisher);
      //   console.log(res1.data.data.pubdate);
      //   console.log(res1.data.data.category);
      //   console.log(res1.data.data);
      //   console.log(res1.data);
      //
      //   this.bookinfo.summary = res1.data.data.summary;
      //   this.bookinfo.title = res1.data.data.title;
      //   this.bookinfo.translator = res1.data.data.translator;
      //
      //   this.bookinfo.author = res1.data.data.author;
      //   this.bookinfo.isbn = res1.data.data.isbn;
      //   this.bookinfo.category = res1.data.data.category;
      //   this.bookinfo.pubdate = res1.data.data.pubdate;
      //   this.bookinfo.publisher = res1.data.data.publisher;
      //   this.bookinfo.price = res1.data.data.price;
      //   this.bookinfo.img = res1.data.data.img;
      // })
      // console.log("booktodb" + this.booktodb)
      // console.log(this.booktodb)
      // console.log("bookinfo" + this.bookinfo);
      // console.log(this.bookinfo)

      this.booktodb.name = this.bookinfo.title;
      this.booktodb.writer = this.bookinfo.author
      this.booktodb.isbn = this.bookinfo.isbn
      this.booktodb.category = this.bookinfo.category
      this.booktodb.pressdate = this.bookinfo.pubdate
      this.booktodb.presshouse = this.bookinfo.publisher
      this.booktodb.picture = this.bookinfo.img
      this.booktodb.price = this.bookinfo.price.toString().substring(0, 5)
      console.log("price todb:", this.booktodb.price)
      console.log("price info:", this.bookinfo.price)

      this.booktodb.intro = this.bookinfo.summary
      this.booktodb.customer_condition = this.pinxiang
      this.booktodb.user_id = window.sessionStorage.getItem("id")

      console.log("id:", this.booktodb)


      postbooktowarehouse(this.booktodb).then(r => {
        getSalebook(window.sessionStorage.getItem("id")).then((r) => {

          console.log("添加后数据库", r.data)

          this.cartData = r.data.map(s => {
            let fin_price;
            fin_price = s["book_price"] * s["condition_rate_customerrate"]
            // console.log("价格", s["price"])
            return {
              id: s["id"],
              isbn: s["book_isbn"],
              name: s["book_name"],
              price: fin_price,
              img: s["book_pic"],
              quantity: 1,
              pinxiang: s["condition_rate_name"],
              writer: s["book_writer"]
            };
          })
          console.log(this.cartData)
        })
        // getSalebook(window.sessionStorage.getItem("id")).then((r) => {
        //   console.log(window.sessionStorage.getItem("id"))
        //   console.log(r.data)
        //   this.cartData = r.data.map(s => {
        //     console.log("价格", s["price"])
        //     return {
        //       name: s["book_name"],
        //       price: 22,
        //       img: s["book_pic"],
        //       quantity: 1,
        //       pinxiang: s["customer_condition"],
        //     };
        //   })
        // })
      })


      dialogFormVisible.value = false;


      // this.cartData.push({
      //   quantity: 1, name: this.bookinfo.title,
      //   price: this.bookinfo.price.substring(0, 5), img: this.bookinfo.img,
      //   isSelected: false, pinxiang: this.pinxiang,
      // });

    },
    findbookinfo() {
 if (this.inputtext.length !== 13 || !/^\d{13}$/.test(this.inputtext)) {
    alert("ISBN号应为13位数字，请重新输入！");
  } else{
      console.log(this.inputtext);
      this.centerDialogVisible = true
      console.log("发啊啊啊啊啊啊啊")
      //fetchbook↓
      getdbbook(this.inputtext).then(res => {
        console.log("触发啊啊啊啊啊啊啊")
        console.log(res);
        let res1 = res;
        if (res1.data.status) {
          console.log("图书库里有")
          console.log(res1.data)
          this.bookinfo.summary = res1.data.intro;
          this.bookinfo.title = res1.data.name;
          this.bookinfo.translator = '';
          this.bookinfo.author = res1.data.writer;
          this.bookinfo.isbn = res1.data.isbn;
          this.bookinfo.category = res1.data.category;
          this.bookinfo.pubdate = res1.data.pressdate;
          this.bookinfo.publisher = res1.data.presshouse;
          this.bookinfo.price = res1.data.price;
          this.bookinfo.img = res1.data.picture;
        } else {
          getoutbook(this.inputtext).then(res2 => {
            console.log("图书库里没有")

            this.bookinfo.summary = res2.data.data.summary;
            this.bookinfo.title = res2.data.data.title;
            this.bookinfo.translator = res2.data.data.translator;
            this.bookinfo.author = res2.data.data.author;
            this.bookinfo.isbn = res2.data.data.isbn;
            this.bookinfo.category = res2.data.data.category;
            this.bookinfo.pubdate = res2.data.data.pubdate;
            this.bookinfo.publisher = res2.data.data.publisher;
            this.bookinfo.price = res2.data.data.price;
            this.bookinfo.img = res2.data.data.img;

            this.booktodb.name = this.bookinfo.title;
            this.booktodb.writer = this.bookinfo.author
            this.booktodb.isbn = this.bookinfo.isbn
            this.booktodb.category = this.bookinfo.category
            this.booktodb.pressdate = this.bookinfo.pubdate
            this.booktodb.presshouse = this.bookinfo.publisher
            this.booktodb.picture = this.bookinfo.img
            this.booktodb.price = this.bookinfo.price.toString().substring(0, 5)
            this.booktodb.intro = this.bookinfo.summary
            this.booktodb.customer_condition = this.pinxiang
            this.booktodb.user_id = window.sessionStorage.getItem("id")

            console.log("price todb:", this.booktodb.price)
            console.log("price info:", this.bookinfo.price)
            postbooktobook(this.booktodb)

          })
        }
      })

    }
    },


  },

}


</script>


<style scoped>
/* 公共样式 */
.dialog-footer button:first-child {
  margin-right: 10px;
}

.box-card {
  margin-left: 150px;
  margin-right: 150px;
  margin-top: 10px;


  background-color: darkgray;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 90%;
  width: 80%;

}

.insertBook {
  margin-left: 2%;
  margin-bottom: 0.5%;
  height: 90%;
  width: 40%;
  justify-content: center;
  align-items: center;
}

.insertbutton {
  float: left;

}

#insertBook {
  display: inline-block;
}

.clearfix {
  content: '';
  display: block;
  clear: both;
}

.red {
  color: #f30213;
}

.fl {
  float: left;
}

.fr {
  float: right;
}

/* 清除默认样式 */
* {
  margin: 0px;
  padding: 0px;
  font-size: 14px;
}

a {
  text-decoration: none;
  color: #333;
}

input {
  outline: none;
}

.wrap {
  width: 1180px;
  margin: 0 auto;
}

.wrap .location {
  padding: 10px 0;
  border-bottom: 1px solid #ccc;
  margin-bottom: 20px;
}

.cartTable {
  border: 1px solid #ccc;
  text-align: center;

}

.cartTable tr.title {
  background-color: rgb(241, 243, 244);
  font-weight: bold;
}

.cartTable tbody tr td {
  /* border: 1px solid rgb(245, 245, 245); */
  padding: 10px;
}

/* 原价 */
.cartTable tbody tr td .tdl {
  text-decoration: line-through;
  color: #999;
}

/* 商品数量 */
.cartTable tr .amount .unum {
  width: 70px;
  height: 30px;
  box-sizing: border-box;
  text-align: center;
  font-size: 16px;
  float: left;
}

/* 数量加减按钮 */
.cartTable tr .amount el-button {
  display: block;
  width: 30px;
  height: 30px;
  line-height: 30px;
  text-align: center;
  font-size: 18px;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

.cartTable tr .amount el-button.Increase {
  border-right: none;
  float: left;
  text-align: center;
  width: 10px;
  height: 30px;
}

.cartTable tr .amount el-button.Reduce {
  border-left: none;
  float: left;
  text-align: center;
  width: 10px;
  height: 30px;
}

.cartTable tr.count .jiesuan .right {
  text-align: right;

}

.cartTable tr.count .jiesuan .right p {
  margin: 5px 0;
}

.cartTable tr.count .jiesuan .right .pay {
  display: block;
  width: 160px;
  height: 50px;
  line-height: 50px;
  background-color: #f30213;
  color: #fff;
  font-weight: bold;
  text-align: center;
  font-size: 20px;
}

.delbutton {

  text-align: left;
  padding-left: 20px;
  margin-left: 20px;

}

.amount .amount-row {
  align-items: center;
}

.p-number {
  font-size: 30px;
}

</style>