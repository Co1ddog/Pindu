<template>
  <div class="app-container" ref="appContainer" v-if="load">
    <div class="app-container-inner">
      <PropTable
        :loading="loading"
        @selection-change="selectionChange"
        :columns="column"
        :data="list"
        @reset="reset"
        @onSubmit="onSubmit"
      >
        <template v-slot:operation="scope">
          <el-button @click="handleClick(scope.row)" type="primary" size="small" icon="Edit">
            审核</el-button
          >
        </template>
      </PropTable>
    </div>
  </div>
</template>
<script lang="ts" setup>
  import { ref, reactive, onMounted, onBeforeMount, nextTick } from 'vue'
  import { ElMessage } from 'element-plus'
  import type { FormInstance } from 'element-plus'
  import { sellOrder0 } from '../../../api/orderService'
  import moment from 'moment'
  import { useRoute, useRouter } from 'vue-router'
  const router = useRouter()

  const appContainer = ref(null)

  const loading = ref(true)
  import PropTable from '@/components/Table/PropTable/index.vue'

  function handleClick(row) {
    router.push({
      path: 'check_work',
      query: { data: JSON.stringify(row) },
    })
  }

  const data = []
  const column = [
    { name: 'id', label: '订单号', inSearch: true, valueType: 'input', width: 120 },
    // { name: 'status', label: '订单状态', width: 200 },
    {
      name: 'user_id',
      label: '用户ID',
      inSearch: true,
      valueType: 'input',
      width: 120,
    },
    {
      name: 'user_name',
      label: '用户名称',
      inSearch: true,
      valueType: 'input',
      width: 200,
    },
    {
      name: 'submit_time',
      label: '日期',
      sorter: true,
      inSearch: true,
      valueType: 'input',
      width: 300,
    },
    { name: 'operation', slot: true, fixed: 'right', width: 200, label: '操作' },
  ]
  const list = ref(data)
  const load = ref(false)
  const formSize = ref('default')
  const ruleFormRef = ref<FormInstance>()

  const dialogVisible = ref(false)
  const title = ref('品相判断')
  const rowObj = ref({})
  const selectObj = ref([])

  const reset = () => {
    loading.value = true
    setTimeout(() => {
      loading.value = false
    }, 500)
    ElMessage.success('触发重置方法')
  }
  onBeforeMount(() => {
    sellOrder0().then((r) => {
      console.log(r.data)
      r.data.forEach((e, i) => {
        data.push(e)
      })
      data.forEach((e, i) => {
        e.submit_time = moment(e.submit_time).format('YYYY-MM-DD HH:mm:ss')
      })
      load.value = true
    })
  })

  function rowId(row) {
    rowObj.value = row
    console.log(row.id)
    return row.id
  }

  const onSubmit = (val) => {
    console.log('val===', val)
    ElMessage.success('触发查询方法')
    loading.value = true

    setTimeout(() => {
      loading.value = false
    }, 500)
  }

  onMounted(() => {
    nextTick(() => {
      // let data = appContainer.value.
    })
    setTimeout(() => {
      loading.value = false
    }, 500)
  })
</script>

<style scoped>
  .edit-input {
    padding-right: 100px;
  }

  .app-container {
    flex: 1;
    display: flex;
    width: 100%;
    padding: 16px;
    box-sizing: border-box;
  }

  .cancel-btn {
    position: absolute;
    right: 15px;
    top: 10px;
  }
</style>
