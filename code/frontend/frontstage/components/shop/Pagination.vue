<template>
  <el-pagination v-model:page="page" :page-size="2" layout="total, sizes, prev, pager, next, jumper" :total="books.length" style="background-color: white" size="large" @size-change="handleSizeChange"
          @current-change="handleCurrentChange"/>
<!--  <el-pagination-->
<!--          v-model:currentPage="currentPage1"-->
<!--          :page-size="10"-->
<!--          background-->
<!--          layout="total, sizes, prev, pager, next, jumper"-->
<!--          :total="data.length"-->
<!--          @size-change="handleSizeChange"-->
<!--          @current-change="handleCurrentChange"-->
<!--        />-->
</template>

<script setup>
import {onMounted, reactive, ref} from "vue";
import {getBookIsFlow} from "../../api/GetBookService";
const page = ref(1);
const data= {
      type: Array,
      default: () => [],
    }
const books = reactive([])

onMounted(async () => {
  const response = await getBookIsFlow()
  books.push(...response.data)
  console.log("书有",books.length)
})
// for (let item of props.columns) {
//     if (item.inSearch) {
//       obj[item.name] = null
//     }
//     if (item.inSearch) {
//       search.push(item)
//     }
//   }
// let props = defineProps({
//     // columns: {
//     //   type: Array,
//     //   default: () => [],
//     // },
//     data: {
//       type: Array,
//       default: () => [],
//     },
//     // loading: {
//     //   type: Boolean,
//     //   default: false,
//     // },
//   });
 const handleSizeChange = (number) => {
    console.log(`${number} items per page`)
  };
const handleCurrentChange = (number) => {
    console.log(`current page: ${number}`)
    console.log('数据', page.value.valueOf())
    page.value = number
  };
</script>