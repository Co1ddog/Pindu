<template>
  <div class="app-container" ref="appContainer" v-if="load">
    <!--    sale-->
    <PropTable
      :loading="loading"
      @selection-change="selectionChange"
      :columns="column"
      :data="list"
      @reset="reset"
      @onSubmit="onSubmit"
    >
      <template v-slot:operation="scope">
        <el-button type="primary" size="small" icon="Edit" @click="edit(scope.row)">
          处理
        </el-button>
        <el-button @click="del(scope.row)" type="danger" size="small" icon="Delete">
          删除
        </el-button>
      </template>
    </PropTable>

    <el-dialog v-model="dialogVisible" :title="title" width="50%">
      <el-form
        ref="ruleFormRef"
        :model="ruleForm"
        label-width="120px"
        class="demo-ruleForm"
        :size="formSize"
      >
        <el-form-item label="问题号：">
          {{ ruleForm.id }}
        </el-form-item>
        <el-form-item label="用户：">
          {{ ruleForm.user }}
        </el-form-item>
        <el-form-item label="处理状态：">
          {{ ruleForm.que_condition_text }}
        </el-form-item>
        <el-form-item label="详细内容：">
          {{ ruleForm.que_content_user2aftersaleman }}
        </el-form-item>
        <el-form-item label="联系资金：">
          <el-input v-model="ruleForm.que_content_aftersaleman2assetman" type="textarea"></el-input>
        </el-form-item>
        <el-form-item label="资金反馈：">
          {{ ruleForm.que_content_assetman2aftersaleman }}
        </el-form-item>
        <el-form-item label="处理内容：">
          <el-input v-model="ruleForm.que_content_aftersaleman2user" type="textarea"></el-input>
        </el-form-item>
      </el-form>

      <template #footer>
        <span class="dialog-footer">
          <el-button @click="dialogVisible = false">取消</el-button>
          <el-button type="primary" @click="handleClose(ruleFormRef)">确定</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script lang="ts" setup>
  import { nextTick, onBeforeMount, onMounted, reactive, ref } from 'vue'
  import type { FormInstance } from 'element-plus'
  import { ElMessage, ElMessageBox } from 'element-plus'
  import PropTable from '@/components/Table/PropTable/index2.vue'
  import { feedbackDelete, feedbackList, feedbackUpdate } from '../../../api/feedbackService'

  const loading = ref(true)
  const appContainer = ref(null)
  const load = ref(false)

  // data是表格数据
  const data = []
  onBeforeMount(() => {
    feedbackList().then((r) => {
      r.data.forEach((e, i) => {
        data.push(e)
      })

      data.forEach((e, i) => {
        e.user = e.user_name + '(' + e.user_id + ')'
        if (e.aftersaleman_id === null) {
          e.aftersaleman = '-'
        } else {
          e.aftersaleman = e.aftersaleman_name + '(' + e.aftersaleman_id + ')'
        }
        if (e.assetman_id === null) {
          e.assetman = '-'
        } else {
          e.assetman = e.assetman_name + '(' + e.assetman_id + ')'
        }

        if (e.que_condition == 0) {
          e.que_condition_text = '待处理'
        } else if (e.que_condition == 1) {
          e.que_condition_text = '待资金回复'
        } else if (e.que_condition == 2) {
          e.que_condition_text = '待反馈'
        } else if (e.que_condition == 3) {
          e.que_condition_text = '已完成'
        }
      })
      console.log(data)
      load.value = true
    })
  })

  const column = [
    { name: 'id', label: '问题', inSearch: true, valueType: 'input', width: '60' },
    { name: 'user', label: '用户', inSearch: true, valueType: 'input', width: '90' },
    { name: 'aftersaleman', label: '售后专员', inSearch: true, valueType: 'input', width: '100' },
    {
      name: 'que_condition_text',
      label: '处理状态',
      inSearch: true,
      valueType: 'input',
      width: '90',
    },
    {
      name: 'que_content_user2aftersaleman',
      label: '问题内容',
      inSearch: true,
      valueType: 'input',
    },
    { name: 'operation', slot: true, fixed: 'right', width: 200, label: '操作' },
  ]

  const list = ref(data)

  const formSize = ref('default')
  const ruleFormRef = ref<FormInstance>()
  const ruleForm = reactive({
    id: '',
    user: '',
    que_condition_text: '',
    que_content_user2aftersaleman: '',
    que_content_aftersaleman2user: '',
    que_content_aftersaleman2assetman: '',
    que_content_assetman2aftersaleman: '',
  })

  const dialogVisible = ref(false)
  const title = ref('修改')
  const rowObj = ref({})
  const selectObj = ref([])

  const handleClose = async (done: () => void) => {
    await ruleFormRef.value.validate((valid, fields) => {
      if (valid) {
        let obj = {
          ...ruleForm,
        }
        list.value.forEach((item) => {
          if (item.id === rowObj.value.id) {
            item.que_content_aftersaleman2user = obj.que_content_aftersaleman2user
            item.que_content_aftersaleman2assetman = obj.que_content_aftersaleman2assetman
            feedbackUpdate(item.id, {
              que_content_aftersaleman2user: item.que_content_aftersaleman2user,
              que_content_aftersaleman2assetman: item.que_content_aftersaleman2assetman,
            }).then((r) => {
              console.log('patch resp:', r.data)
            })
            alert(rowObj.value.id)
          }
        })
        dialogVisible.value = false

        console.log('submit!', obj)
      } else {
        console.log('error submit!', fields)
      }
    })
  }

  const selectionChange = (val) => {
    selectObj.value = val
  }

  const edit = (row) => {
    title.value = '处理详情'
    rowObj.value = row
    dialogVisible.value = true

    ruleForm.id = row.id
    ruleForm.user = row.user
    ruleForm.que_condition_text = row.que_condition_text
    ruleForm.que_content_user2aftersaleman = row.que_content_user2aftersaleman
    ruleForm.que_content_aftersaleman2user = row.que_content_aftersaleman2user
    ruleForm.que_content_aftersaleman2assetman = row.que_content_aftersaleman2assetman
    ruleForm.que_content_assetman2aftersaleman = row.que_content_assetman2aftersaleman
  }

  const del = (row) => {
    console.log('row==', row)
    ElMessageBox.confirm('你确定要删除当前项吗?', '温馨提示', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
      draggable: true,
    })
      .then(async () => {
        await feedbackDelete(row.id).then((r) => console.log(r.data))
        list.value = list.value.filter((item) => item.id !== row.id)
        ElMessage.success('删除成功')
        loading.value = true
        setTimeout(() => {
          loading.value = false
        }, 500)
      })
      .catch(() => {})
  }

  const reset = () => {
    loading.value = true
    setTimeout(() => {
      loading.value = false
    }, 500)
    ElMessage.success('触发重置方法')
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
