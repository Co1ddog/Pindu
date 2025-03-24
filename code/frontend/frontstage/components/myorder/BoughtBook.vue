<template>
    <el-header> <span style="color: blueviolet;font-size: 16px;">
        买过的书</span>
    </el-header>
    <el-scrollbar height="400px">
        <div v-if="visible">
            <el-table :data="tableData" name="orders">
                <el-table-column label="时间" prop="date"
                                 >
<!--                  :formatter="dateFormat"-->
                </el-table-column>
                <el-table-column label="订单号" prop="order">
                </el-table-column>
                <el-table-column label="订单状态" prop="status">
                </el-table-column>
                <el-table-column align="right">
                    <template v-slot:default="{row}">
                 <router-link :to="{name: 'boughtorderinfo'  ,params:{oid:row.order.toString()} }">
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
<script lang="ts" setup>
import {computed, onMounted, provide, reactive, ref} from 'vue';
import {getbuyorders} from "../../api/getOrders";
import {ElTable, ElTableColumn} from 'element-plus'
// import moment from 'moment'

// let tableData = reactive([{date: '', order: ''}])
let tableData = reactive([{date: '', order: '',status:''}])
const uid = window.sessionStorage.getItem("id")
console.log(uid)
const visible = ref(false)
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
    getbuyorders(uid).then((r) => {
        tableData = r.data.map(s => {
            return {
                date: s["submit_time"],
                order: s["id"],
                status:trans(s['status'])
            };
        })
        console.log(tableData)
      visible.value=true
    })
})



// function dateFormat(row, column) {
//     var date = row[column.property];
//     if (date == undefined) {
//         return "";
//     }
//     return moment(date).format("YYYY-MM-DD HH:mm:ss");
// }


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