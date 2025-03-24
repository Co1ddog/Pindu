<template>
  <el-table :data="tableData" style="width: 90%; background-color: gray">
    <el-table-column prop="date" label="封面" width="100">
      <template #default="scope">
        <el-image style="width: 70px; height: 70px" :src="scope.row.date" alt="" :fit="fill"></el-image>
      </template>
    </el-table-column>
    <el-table-column prop="name" label="作者" width="180"/>
    <el-table-column prop="address" label="简介"/>
    <el-table-column prop="yes" label="ISBN"/>
    <el-table-column prop="no" label="出版社"/>

  </el-table>
</template>

<script setup>
import sample3 from "@/assets/pictures/sample3.webp"
import sample4 from "@/assets/pictures/sample4.webp"
import sample5 from "@/assets/pictures/sample5.webp"


const tableData = [
  {
    date: sample3,
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
    yes: 'Tom',
    no: 'No. 189, Grove St, Los Angeles',

  },
  {
    date: sample4,
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
    yes: 'Tom',
    no: 'No. 189, Grove St, Los Angeles',

  },
  {
    date: sample5,
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
    yes: 'Tom',
    no: 'No. 189, Grove St, Los Angeles',

  },
  {
    date: sample3,
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
    yes: 'Tom',
    no: 'No. 189, Grove St, Los Angeles',

  },
  {
    date: sample4,
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
    yes: 'Tom',
    no: 'No. 189, Grove St, Los Angeles',

  },
  {
    date: sample5,
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
    yes: 'Tom',
    no: 'No. 189, Grove St, Los Angeles',

  },
  {
    date: sample3,
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
    yes: 'Tom',
    no: 'No. 189, Grove St, Los Angeles',

  },
  {
    date: sample4,
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
    yes: 'Tom',
    no: 'No. 189, Grove St, Los Angeles',

  },
  {
    date: sample5,
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
    yes: 'Tom',
    no: 'No. 189, Grove St, Los Angeles',

  },
  {
    date: sample3,
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
    yes: 'Tom',
    no: 'No. 189, Grove St, Los Angeles',

  },
  {
    date: sample4,
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
    yes: 'Tom',
    no: 'No. 189, Grove St, Los Angeles',

  },
  {
    date: sample5,
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
    yes: 'Tom',
    no: 'No. 189, Grove St, Los Angeles',

  },


]
</script>
