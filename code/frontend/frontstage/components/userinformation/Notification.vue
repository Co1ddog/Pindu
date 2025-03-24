<template>
    <div class="common-layout">
        <el-container>
            <el-header> <span style="color: blueviolet;font-size: 16px;">
         通知
        </span>
            </el-header>

            <el-main>
              <div v-if="get">
                <el-scrollbar height="600px">
                <el-table :data="tableData" style="width: 100%">
                  <el-table-column label="反馈状态" prop="condition"/>
                  <el-table-column label="问题" prop="question"/>
                  <el-table-column label="回复" prop="answer"/>
                </el-table>
                </el-scrollbar>
              </div>
            </el-main>

        </el-container>
    </div>
</template>

<script lang="ts" setup>
import {onMounted,ref} from "vue";
import {getfeedback} from '../../api/getOrders'
const get=ref(false)
let tableData = ref([
    {
       condition:'',
        question: '',
        answer:''
    }])

function trans(num){
  if(num==1){
    return '售后发给资金'
  }
  if(num==0){
    return '未处理'
  }
  if(num==2){
    return '资金返给售后'
  }
  if(num==3){
    return '已回复'
  }
  else{
    return '未知状态'
  }
}
onMounted(()=>{
  const uid = window.sessionStorage.getItem("id")
  getfeedback(uid).then((r)=> {
    tableData = r.data.map(s => {
      return {
        condition: trans(s["que_condition"]),
        question: s['que_content_user2aftersaleman'],
        answer: s['que_content_aftersaleman2user'],
      }
    })
    console.log(tableData)
    get.value=true
  })
  })
</script>
<!--0-未处理-->
<!--1-售后发给资金-->
<!--2.资金返给售后-->
<!--3.结束-->