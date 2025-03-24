<template>
  <div class="advancedForm">
    <el-card class="box-card" style="margin-top: 20px">
      <template #header>
        <div class="card-header">
          <span>公司买卖书规则维护</span>
        </div>
      </template>
      <h3>优良品相</h3>
      <AdvancedForm :columns="g_columns" @submit="onSubmit1" :byHeight="true"/>
      <h3>中等品相</h3>
      <AdvancedForm :columns="n_columns" @submit="onSubmit2" :byHeight="true"/>
    </el-card>
  </div>
</template>

<script lang="ts" setup>
import AdvancedForm from '@/components/SearchForm/advancedForm/index.vue'
import {onMounted, reactive, ref} from 'vue'
import {ElMessage, ElMessageBox} from 'element-plus'
import {updaterate, updatebuyrate, updatesellrate, getrate} from '../../../api/updaterate.js'

let g_columns = ref([
  {
    type: 'input',
    name: 'name1',
    title: '平台买书',
    placeholder: '售价占原价的比值(%)',
    span: 8,
  },
  {
    type: 'input',
    name: 'name2',
    title: '平台卖书',
    placeholder: '收购价格比值(%)',
    span: 8,
  },
])

let n_columns = ref([
  {
    type: 'input',
    name: 'name3',
    title: '平台买书',
    placeholder: '售价占原价的比值(%)',
    span: 8,
  },
  {
    type: 'input',
    name: 'name4',
    title: '平台卖书',
    placeholder: '收购价格比值(%)',
    span: 8,
  },
])
onMounted(() => {
  getrate().then((r) => {
    console.log(r.data)
    n_columns.value[1].placeholder = r.data[0].buy_rate
    n_columns.value[0].placeholder = r.data[0].sell_rate
    g_columns.value[1].placeholder = r.data[1].buy_rate
    g_columns.value[0].placeholder = r.data[1].sell_rate
  })
  console.log(g_columns.value[0].placeholder)
})
const formValue = ref({})
const row = ref(1)

function onSubmit1(formInline) {

  if (formInline.name1 != null && formInline.name2 != null) {
    updaterate(2, formInline.name2, formInline.name1)
  }
  if (formInline.name1 == null && formInline.name2 != null) {
    updatebuyrate(2, formInline.name2)
  }
  if (formInline.name1 != null && formInline.name2 == null) {
    updatesellrate(2, formInline.name1)
  }
  formValue.value = formInline

  ElMessage.success(JSON.stringify(formInline))
}

function onSubmit2(formInline) {
  if (formInline.name3 != null && formInline.name4 != null) {
    updaterate(1, formInline.name4, formInline.name3)
  }
  if (formInline.name3 == null && formInline.name4 != null) {
    updatebuyrate(1, formInline.name4)
  }
  if (formInline.name3 != null && formInline.name4 == null) {
    updatesellrate(1, formInline.name3)
  }

  formValue.value = formInline
  ElMessage.success(JSON.stringify(formInline))
}

const showRow = (number) => {
  row.value = number
}
</script>

<style lang="scss" scoped>
.advancedForm {
  padding: 20px;
}

name3 {
  size: 20px;
}
</style>
