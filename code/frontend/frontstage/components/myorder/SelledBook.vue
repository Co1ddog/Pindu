<template>
  <el-header> <span style="color: blueviolet;font-size: 16px;">
         卖过的书
        </span>
  </el-header>
  <el-scrollbar height="400px">


  <div v-if="visible">
    <el-table :data="tableData" name="orders">
      <el-table-column label="日期" prop="date">

      </el-table-column>
      <el-table-column label="订单号" prop="order">

      </el-table-column>
      <el-table-column label="订单状态" prop="status">

      </el-table-column>
      <el-table-column align="right">
      <template v-slot:default="{row}">
        <router-link :to="{name: 'soldorderinfo'  ,params:{oid:row.order.toString()} }">
          <el-button size="default" type="success" >
          查看详情
          </el-button>
        </router-link>
        </template>
      </el-table-column>
    </el-table>
  </div>
  </el-scrollbar>
</template>

<script setup>
import {computed, onMounted, provide, reactive, ref} from 'vue';
import {getsellorders} from "../../api/getOrders";


let tableData = reactive([{date: '', order: ''}])
let columnname = ref("订单号")


  const visible = ref(false);



function goodman(row){
    console.log(tableData[row].order)
}
const uid = window.sessionStorage.getItem("id")
console.log(uid)
function trans(str){
  if(str==1){
    return "已完成"
  }
  if(str==0){
    return '进行中'
  }
  else return "不清楚"
}
onMounted(() => {
  getsellorders(uid).then((r) => {
    tableData = r.data.map(s => {
      return {
        date: s["submit_time"],
        order: s["id"],
        status:trans(s['status'])
      }
    })
    console.log("tabledata", tableData)
    visible.value=true
  })
})

</script>
<style scoped>
.scrollbar-demo-item {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 50px;
  margin: 10px;
  text-align: center;
  border-radius: 4px;
  background: var(--el-color-primary-light-9);
  color: var(--el-color-primary);
}
</style>