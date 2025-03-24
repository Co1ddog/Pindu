<template>
  <el-card class="box-card" >
    <div class="wrap clearfix">
      <div class="location">当前位置：首页<span>&gt;</span><b class="red">购物车</b></div>


      <div>
        <table width="100%" class="cartTable" cellspacing="0" cellpadding="10px">

          <tr class="title">
            <td width="50"><input type="checkbox" name="" class="choose_all" v-model="isSelectedAll"></td>
            <td width="100" class=""><span style="margin-left: -10px;">全选</span></td>
            <td width="200"> 商品信息</td>
            <td width="100">品相</td>
            <td width="150">单价（元）</td>
            <td width="148">数量</td>
            <td width="150">金额（元）</td>
            <td width="80">操作</td>
          </tr>


          <tr v-for="(item, index) in cartData" :key="item.id" class="row">
            <td><input type="checkbox" class="choose" v-model="item.isSelected"></td>
          <td class="tal"><a href="#" class="pic"><img :src=item.loc alt="picture" width="100"
                                                         height="100"></a>

            </td>

            <td class="tal"><a href="#">{{ item.name }}</a></td>
            <td class="tal"><a href="#">{{ item.pinxiang }}</a></td>
            <td class="unit">{{ item.price }}</td>
            <td>
              <div class="amount">
                <el-row class="amount-row">

                  <el-button href="#" class="Reduce" size="default" @click="reduceQuantity(index)">-</el-button>


                  <input type="text" class="unum" v-model="item.quantity" @blur="checkQuantity(index)"/>


                  <el-button class="Increase" href="#" size="default" @click="addQuantity(index)">+</el-button>

                </el-row>

              </div>
            </td>
            <td><b class="u-price"> {{ item.price * item.quantity }} </b></td>
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
                <router-link to="/purchasecheck/">
                  <button class="btn pay fr">提交订单</button>
                </router-link>
              </div>
            </div>
            <td></td>
          </tr>
        </table>

      </div>
    </div>
  </el-card>
</template>

<script>
import pic1 from "../images/pic1.png"
import pic2 from "../images/pic2.png"
import pic3 from "../images/pic3.png"
export default {
  data() {
    return {
      cartData: [
        {
          id:"1",
          name: "高性能MySQL",
          price: 30,
          quantity: 1,
          loc:pic1,
          isSelected: false,
          pinxiang: "全新"
        },
        {
          id:"2",
          name: "Vue.js设计与实践",
          price: 20,
          quantity: 2,
          loc: pic2,
          isSelected: false,
          pinxiang: "优良"
        },
        {
          id:"3",
          name: "信息系统分析与设计",
          price: 15,
          quantity: 1,
          loc: pic3,
          isSelected: false,
          pinxiang: "垃圾"
        },
      ],
    };
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
       console.log(this.cartData[index])
      const deltodb=[this.cartData[index]]
      console.log(deltodb)
      deleteCartBook(window.sessionStorage.getItem("id"), deltodb)
      this.cartData.splice(index, 1);
    },
    removeSelectedProducts() {
      const deltodb=this.cartData.filter((item) => item.isSelected)
      console.log(deltodb)
      deleteCartBook(window.sessionStorage.getItem("id"), this.cartData.filter((item) => item.isSelected))
      this.cartData = this.cartData.filter((item) => !item.isSelected);
    },
  },
};
</script>

<style scoped>
/* 公共样式 */
.box-card {
  margin-left: 10%;
  margin-right: 10%;
  margin-top: 5%;

  background-color:darkgray;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 90%;
  width: 80%;


}

.clearfix {
  content: '';
  display: block;
  clear: both;
  justify-content: center;
  align-items: center;
  height: 90%;
  width: 80%;
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