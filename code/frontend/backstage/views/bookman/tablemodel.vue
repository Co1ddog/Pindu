<template>
  <div class="app-container" ref="appContainer">
    <PropTable
      :loading="loading"
      @selection-change="selectionChange"
      :columns="column"
      :data="list"
      @reset="reset"
      @onSubmit="onSubmit"
    >
      <template v-slot:btn>
        <div style="display: flex; justify-content: flex-end">
          <el-button type="primary" @click="getbookinfo">
            <el-icon>
              <plus />
            </el-icon>
            ISBN获取
          </el-button>
          <!--          <el-button type="primary" @click="add">-->
          <!--            <el-icon>-->
          <!--              <plus />-->
          <!--            </el-icon>-->
          <!--            添加-->
          <!--          </el-button>-->
          <el-button type="danger" @click="batchDelete">
            <el-icon>
              <delete />
            </el-icon>
            删除
          </el-button>
        </div>
      </template>
      <template v-slot:isflow="scope">{{ scope.row.isflow ? '是' : '否' }}</template>
      <template v-slot:operation="scope">
        <el-button type="primary" size="small" icon="Edit" @click="edit(scope.row)">
          编辑
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
        :rules="rules"
        label-width="120px"
        class="demo-ruleForm"
        :size="formSize"
      >
        <el-form-item label="书名" prop="name">
          <el-input v-model="ruleForm.name" />
        </el-form-item>
        <el-form-item label="是否流通" prop="fl">
          <el-radio-group v-model="ruleForm.fl">
            <el-radio :label="1">是</el-radio>
            <el-radio :label="0">否</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="价格" prop="price">
          <el-input v-model="ruleForm.price" />
        </el-form-item>
        <el-form-item label="作者" prop="author">
          <el-input v-model="ruleForm.author" />
        </el-form-item>
        <el-form-item label="isbn号" prop="isbn" :disabled="true">
          <el-input v-model="ruleForm.isbn" />
        </el-form-item>
        <el-form-item label="出版社" prop="publisher">
          <el-input v-model="ruleForm.publisher" />
        </el-form-item>
        <el-form-item label="出版时间" prop="pubdate">
          <el-input v-model="ruleForm.pubdate" />
        </el-form-item>
        <el-form-item label="类别" prop="category">
          <el-input v-model="ruleForm.category" />
        </el-form-item>
        <el-form-item label="图书简介" prop="summary">
          <el-input v-model="ruleForm.summary" />
        </el-form-item>
        <el-form-item label="图书图片链接" prop="summary">
          <el-input v-model="ruleForm.img" />
        </el-form-item>
        <el-form-item label="图书图片" prop="summary">
          <img :src="ruleForm.img" />
        </el-form-item>
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="dialogVisible = false">取消</el-button>
          <el-button type="primary" @click="handleClose(ruleFormRef)">确定</el-button>
        </span>
      </template>
    </el-dialog>

    <el-dialog v-model="dialogVisible2" :title="title" width="50%">
      <!--      <el-form label-width="120px" :size="formSize">-->
      <el-form
        :model="bookinfo"
        ref="ruleFormRef"
        :rules="rules"
        label-width="120px"
        :size="formSize"
      >
        <el-form-item label="请输入ISBN号">
          <div style="display: flex; align-items: center">
            <el-input type="text" v-model="isbnInput" :rules="rulesisbn" />
            <el-button @click="handleShowbookdetail()">显示</el-button>
            <el-tooltip
              v-if="isbnInput && !is13DigitISBN"
              class="item"
              effect="dark"
              content="请输入13位数字的ISBN号"
              placement="top"
            >
              <i class="el-icon-warning"></i>
            </el-tooltip>
          </div>
        </el-form-item>
        <!--      </el-form>-->

        <!--      <el-form :model="bookinfo" ref="ruleFormRef" :rules="rules" label-width="120px" :size="formSize">-->
        <el-form-item v-show="show" label="isbn号" prop="isbn">
          <el-input v-model="bookinfo.isbn" :disabled="true" />
        </el-form-item>
        <el-form-item v-show="show" label="书名" prop="name">
          <el-input v-model="bookinfo.name" />
        </el-form-item>
        <el-form-item v-show="show" label="价格" prop="price">
          <el-input v-model="bookinfo.price" />
        </el-form-item>
        <el-form-item v-show="show" label="作者" prop="author">
          <el-input v-model="bookinfo.writer" />
        </el-form-item>
        <el-form-item v-show="show" label="出版社" prop="publisher">
          <el-input v-model="bookinfo.presshouse" />
        </el-form-item>
        <el-form-item v-show="show" label="出版时间" prop="pubdate">
          <el-input v-model="bookinfo.pressdate" />
        </el-form-item>

        <el-form-item v-show="show" label="类别" prop="category">
          <el-input v-model="bookinfo.category" />
        </el-form-item>
        <el-form-item v-show="show" label="图书简介" prop="summary">
          <el-input v-model="bookinfo.intro" />
        </el-form-item>
        <el-form-item v-show="show" label="图片" prop="summary">
          <img :src="bookinfo.picture" width="300" height="300" />
        </el-form-item>
        <el-form-item v-show="show" label="图片链接" prop="summary">
          <el-input v-model="bookinfo.picture" />
        </el-form-item>
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="closeisbnDialog()">取消</el-button>
          <el-button type="primary" @click="insertbook()">添加</el-button>
        </span>
      </template>
    </el-dialog>

    <el-dialog v-model="dialogVisible3" :title="title" width="50%">
      <el-form
        ref="ruleFormRef"
        :model="ruleForm"
        :rules="rules"
        label-width="120px"
        class="demo-ruleForm"
        :size="formSize"
      >
        <el-form-item label="isbn号" prop="isbn">
          <el-input v-model="ruleForm.isbn" :disabled="true" />
        </el-form-item>
        <el-form-item label="书名" prop="name">
          <el-input v-model="ruleForm.name" />
        </el-form-item>
        <el-form-item label="是否流通" prop="fl">
          <el-radio-group v-model="ruleForm.isflow">
            <el-radio :label="true">是</el-radio>
            <el-radio :label="false">否</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="价格" prop="price">
          <el-input v-model="ruleForm.price" />
        </el-form-item>
        <el-form-item label="作者" prop="author">
          <el-input v-model="ruleForm.writer" />
        </el-form-item>

        <el-form-item label="出版社" prop="publisher">
          <el-input v-model="ruleForm.presshouse" />
        </el-form-item>
        <el-form-item label="出版时间" prop="pubdate">
          <el-input v-model="ruleForm.pressdate" />
        </el-form-item>
        <el-form-item label="类别" prop="category">
          <el-input v-model="ruleForm.category" />
        </el-form-item>
        <el-form-item label="图书简介(精简)" prop="summary">
          <el-input v-model="ruleForm.intro" />
        </el-form-item>
        <el-form-item label="图书图片链接" prop="summary">
          <el-input v-model="ruleForm.picture" />
        </el-form-item>
         <el-form-item label="图书图片" prop="summary">
          <img :src="ruleForm.picture" width="300" height="300"/>
        </el-form-item>
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="closeisbnDialogy3()">取消</el-button>
          <el-button type="primary" @click="handleClose(ruleFormRef)">确定</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>
<script lang="ts" setup name="comprehensive">
  import { ref, reactive, onMounted, nextTick, computed } from 'vue'
  import { defineComponent } from 'vue'
  import { ElForm, ElFormItem, ElInput, ElButton, ElDialog, ElTooltip } from 'element-plus'
  import * as dayjs from 'dayjs'
  import { ElMessage, ElMessageBox } from 'element-plus'
  import type { FormInstance } from 'element-plus'
  import {
    deldbbook,
    getdballbook,
    getdbbook,
    getoutbook,
    postbooktobook,
    putbooktobook,
  } from '../../api/GetBookServer'

  const loading = ref(true)
  const appContainer = ref(null)
  import PropTable from '@/components/Table/PropTable/index3.vue'

  // const data= []
  let data = ref<any[]>([])
  // const data = reactive({
  //   pubdate: '',
  //   name: '',
  //   price: '',
  //   isbn: '',
  //   publisher: '',
  //   // sex: i % 2 ? 1 : 0,
  //   checked: true,
  //   id: '',
  //   author: '',
  //   summary: '',
  //   category: '',
  //   fl: '',
  //   img: '',
  // })

  // for (let i = 0; i < 100; i++) {
  //   data.push({
  //     date: '2016-05-02',
  //     name: '王五' + i,
  //     price: 1 + i,
  //     province: '上海',
  //     admin: 'admin',
  //     sex: i % 2 ? 1 : 0,
  //     checked: true,
  //     id: i + 1,
  //     age: 0,
  //     city: '普陀区',
  //     address: '上海市普上海',
  //     zip: 200333,
  //   })
  // }

  // for (let i = 0; i < 100; i++) {
  //   data.push({
  //     pubdate: '2016-05-02',
  //     name: '王五' + i,
  //     price: 1 + i,
  //     isbn: '123456' + i + i,
  //     publisher: 'Bjut 11 B105',
  //     // sex: i % 2 ? 1 : 0,
  //     checked: true,
  //     id: i + 1,
  //     author: 'ljw' + i,
  //     summary: '书非常好' + i,
  //     category: '文学' + 1,
  //     fl: i % 2 ? 1 : 0,
  //     img: '图片' + i,
  //   })
  // }
  const simpydata = ref<any[]>([])

  // const simpydata = ref({
  //   pubdate: '',
  //   name: '',
  //   price: '',
  //   isbn: '',
  //   publisher: '',
  //   // sex: i % 2 ? 1 : 0,
  //   checked: true,
  //   id: '',
  //   author: '',
  //   summary: '',
  //   category: '',
  //   fl: '',
  //   img: '',
  // })

  onMounted(() => {
    getdballbook().then((res) => {
      const i = 1
      console.log(res.data)
      simpydata.value = res.data.map((item) => {
        return {
          pressdate: item['pressdate'],
          name: item['name'],
          price: item['price'],
          isbn: item['isbn'],
          presshouse: item['presshouse'],
          // sex: i % 2 ? 1 : 0,
          checked: true,
          id: i + 1,
          writer: item['writer'],
          intro: item['intro'],
          category: item['category'],
          isflow: item['isflow'],
          picture: item['picture'],
        }
      })
      console.log(simpydata.value)
      data.value = simpydata.value.map((item) => {
        return {
          pressdate: item['pressdate'],
          name: item['name'],
          price: item['price'],
          isbn: item['isbn'],
          presshouse: item['presshouse'],
          // sex: i % 2 ? 1 : 0,
          checked: true,
          id: item['id'],
          writer: item['writer'],
          intro: item['intro'],
          category: item['category'],
          isflow: item['isflow'],
          picture: item['picture'],
        }
      })
      // simpydata.value.forEach((item) => {
      //   console.log(item)
      //   console.log(item.summary)
      //   data.value.push({
      //     summary: item.summary.subString(50),
      //     pubdate: item.pubdate,
      //     publisher: item.publisher,
      //     img: item.img,
      //     fl: item.fl,
      //     category: item.category,
      //     isbn: item.isbn,
      //     price: item.price,
      //     name: item.name,
      //     checked: item.checked,
      //     id: item.id,
      //     author: item.author,
      //   })

      //   data.value.summary = item.summary.subString(50)
      //   data.value.pubdate = item.pubdate
      //   data.value.publisher = item.publisher
      //   data.value.img = item.img
      //   data.value.fl = item.fl
      //   data.value.category = item.category
      //   data.value.isbn = item.isbn
      //   data.value.price = item.price
      //   data.value.name = item.name
      //   data.value.checked = item.checked
      //   data.value.id = item.id
      //   data.value.author = item.author
      // })
      console.log(data)
    })
  })

  //     const books = res.data.map(
  //       (function (id) {
  //         return function (item) {
  //           const book = {
  //             // pubdate: item['pressdate'],
  //             // name: item['book_name'],
  //             // price: item['price'],
  //             isbn: item['book_isbn'],
  //             // publisher: item['presshome'],
  //             checked: true,
  //             id,
  //             // author: item['book_writer'],
  //             // summary: item['book_intro'],
  //             // category: item['book_category'],
  //             fl: 1,
  //             // img: item['book_pic'],
  //           }
  //           id++
  //           return book
  //         }
  //       })(i),
  //     )
  //     data.value.push(...books)
  //   })
  // })

  // const column = [
  //   { type: 'selection', width: 60, fixed: 'left' },
  //   { name: 'name', label: '名字', inSearch: true, valueType: 'input', width: 80 },
  //   { name: 'age', label: '年龄', align: 'right' },
  //   {
  //     name: 'sex',
  //     label: '性别',
  //     slot: true,
  //     inSearch: true,
  //     options: [
  //       {
  //         value: 1,
  //         label: '男',
  //       },
  //       {
  //         value: 0,
  //         label: '女',
  //       },
  //     ],
  //     valueType: 'select',
  //   },
  //   { name: 'price', label: '价格', inSearch: true, valueType: 'input' },
  //   { name: 'admin', label: '账号', inSearch: true, valueType: 'input' },
  //   { name: 'address', label: '地址', inSearch: true, valueType: 'input', width: 180 },
  //   { name: 'date', label: '日期', sorter: true, inSearch: true, valueType: 'input', width: 180 },
  //   { name: 'province', label: '省份', width: 100 },
  //   { name: 'city', label: '城市' },
  //   { name: 'zip', label: '邮编' },
  //   { name: 'operation', slot: true, fixed: 'right', width: 200, label: '操作' },
  // ]

  const column = [
    { type: 'selection', width: 40, fixed: 'left',align: 'center' },
    { name: 'name', label: '书名', inSearch: true, valueType: 'input', width: 160, align: 'center' },
    { name: 'writer', label: '作者', align: 'center', width: 90},
    {
      name: 'isflow',
      label: '是否流通',
      slot: true,
      inSearch: true,
      options: [
        {
          value: true,
          label: '是',
        },
        {
          value: false,
          label: '否',
        },
      ],
      width: 60,
      valueType: 'select',
    },
    { name: 'price', label: '价格', inSearch: true, valueType: 'input',width: 60},
    { name: 'category', label: '类别', inSearch: true, valueType: 'input', width: 140 },
    { name: 'isbn', label: 'ISBN号', inSearch: true, valueType: 'input', width: 140 },
    { name: 'presshouse', label: '出版社', inSearch: true, valueType: 'input', width: 140 },

    {
      name: 'pressdate',
      label: '出版时间',
      sorter: true,
      valueType: 'input',
      width: 120,
    },

    { name: 'intro', label: '简介' ,width: 240},
    { name: 'picture', label: '图片',width: 200 },
    // {
    //   name: 'fl',
    //   label: '是否流通',
    //   slot: true,
    //   inSearch: true,
    //   options: [
    //     {
    //       value: 1,
    //       label: '是',
    //     },
    //     {
    //       value: 0,
    //       label: '否',
    //     },
    //   ],
    //   valueType: 'select',
    // },
    { name: 'operation', slot: true, fixed: 'right', width: 200, label: '操作' },
  ]
  let list = ref(data)

  const formSize = ref('default')
  const ruleFormRef = ref<FormInstance>()
  const ruleForm = reactive({
    name: '',
    isflow: null,
    price: null,
    writer: '',
    intro: '',
    presshouse: '',
    isbn: '',
    category: '',
    pressdate: '',
    picture: '',
  })
  const bookinfo = reactive({
    name: '',
    isflow: null,
    price: null,
    writer: '',
    intro: '',
    presshouse: '',
    isbn: '',
    category: '',
    pressdate: '',
    translator: '',
    picture: '',
  })
  const ruleFormforbianji = reactive({
    name: '',
    fl: null,
    price: null,
    author: '',
    summary: '',
    publisher: '',
    isbn: '',
    category: '',
    pubdate: '',
    img: '',
  })
  const isbnInput = ref()

  // const isbnInput = reactive<string>('')
  const is13DigitISBN = /^[0-9]{13}$/.test(isbnInput.value)

  const rulesisbn = [
    {
      required: true,
      message: '请输入ISBN号',
      trigger: 'blur',
    },
    {
      pattern: /^[0-9]{13}$/,
      message: '请输入13位数字的ISBN号',
      trigger: 'blur',
    },
  ]
  function closeisbnDialog() {
    isbnInput.value = ''
    show.value = false
    resetForm()
  }

  function resetForm() {
    bookinfo.name = ''
    bookinfo.price = ''
    bookinfo.writer = ''
    bookinfo.presshouse = ''
    bookinfo.pressdate = ''
    bookinfo.isbn = ''
    bookinfo.category = ''
    bookinfo.intro = ''
    bookinfo.picture = ''
  }
  function handleShowbookdetail() {
    // 判断是否为13位数字的ISBN号
    console.log(isbnInput.value, /^[0-9]{13}$/.test(isbnInput.value))
    const is13DigitISBN = /^[0-9]{13}$/.test(isbnInput)

    if (/^[0-9]{13}$/.test(isbnInput.value)) {
      console.log('进来啦啊')
      // 获取书籍详情等操作
      showbookdetail()
      show.value = true
    } else {
      show.value = false
      alert('需要13位isbn号')
    }
  }
  const rules = reactive({
    name: [
      { required: true, message: '请输入书名', trigger: 'blur' },
      { min: 1, max: 15, message: '长度在 1 到 15 个字符', trigger: 'blur' },
    ],
    price: [{ required: true, message: '请输入价格', trigger: 'blur' }],
    isflow: [
      {
        required: true,
        message: '请选择是否流通',
        trigger: 'change',
      },
    ],
    writer: [{ required: true, message: '请输入作者', trigger: 'blur' }],
    isbn: [{ required: true, message: '请输入isbn号', trigger: 'blur' }],
    presshouse: [{ required: true, message: '请输入出版社', trigger: 'blur' }],
    pressdate: [
      {
        required: true,
        pattern: /^[0-9]{4}-[0-9]{2}-[0-9]{2}$/,
        message: '输入格式为2023-01-01类型',
        trigger: 'blur',
      },
    ],

    category: [{ required: false, message: '请输入图书类别', trigger: 'blur' }],
    intro: [{ required: false, message: '请输入图书简介', trigger: 'blur' }],
    picture: [{ required: false, message: '请输入图书图片链接', trigger: 'blur' }],
  })
  const dialogVisible = ref(false)
  const dialogVisible2 = ref(false)
  const dialogVisible3 = ref(false)

  const title = ref('新增')
  const rowObj = ref({})
  const selectObj = ref([])

  const handleClose = async (done: () => void) => {
         await getdballbook().then((res) => {
      const i = 1
      console.log(res.data)
      simpydata.value = res.data.map((item) => {
        return {
          pressdate: item['pressdate'],
          name: item['name'],
          price: item['price'],
          isbn: item['isbn'],
          presshouse: item['presshouse'],
          // sex: i % 2 ? 1 : 0,
          checked: true,
          id: i + 1,
          writer: item['writer'],
          intro: item['intro'],
          category: item['category'],
          isflow: item['isflow'],
          picture: item['picture'],
        }
      })
      console.log("编辑后simpydata",simpydata.value)
      data.value = simpydata.value.map((item) => {
        return {
          pressdate: item['pressdate'],
          name: item['name'],
          price: item['price'],
          isbn: item['isbn'],
          presshouse: item['presshouse'],
          // sex: i % 2 ? 1 : 0,
          checked: true,
          id: item['id'],
          writer: item['writer'],
          intro: item['intro'],
          category: item['category'],
          isflow: item['isflow'],
          picture: item['picture'],
        }
      })
      console.log("编辑后data",data)
    })

    await ruleFormRef.value.validate(async (valid, fields) => {
      if (valid) {
        let obj = {
          // id: Date.now(),
          ...ruleForm,
          // author: 0,
          // summary: '我不牛逼',
          // publisher: 'Bjut 11 B105',
          // fl: 1,
          // isbn: '123456321',
          // category: '不是文学',
          // date: dayjs().format('YYYY-MM-DD'),
        }
        if (title.value === '新增') {
          list.value = [obj, ...list.value]
          ElMessage.success('添加成功')
        } else {
          let i =0
          data.value.forEach((item) => {
            if (item.isbn === rowObj.value.isbn) {
              console.log(item.isbn)
              console.log(rowObj.value.isbn)
              console.log(data.value[i])
              item.name = obj.name
              item.isflow = obj.isflow
              item.price = obj.price
              item.writer = obj.writer
              item.intro = obj.intro
              item.presshouse = obj.presshouse
              item.isbn = obj.isbn
              item.category = obj.category
              item.pressdate = obj.pressdate
              item.picture = obj.picture
              console.log(data.value[i])
            }
            i=i+1
          })
                    console.log("循环外data",data)
          console.log("循环外list",list.value)
          console.log("循环外data",data)
          console.log("循环外listi",list.value[i],i)
          console.log("循环外datai",data[i])

        }
        // putbooktobook()
        dialogVisible3.value = false
        console.log('submit!', obj)
        console.log("编辑前data",data)
        await putbooktobook(obj.isbn, obj)

      } else {
        console.log('error submit!', fields)
      }
    })
     await getdballbook().then((res) => {
      const i = 1
      console.log(res.data)
      simpydata.value = res.data.map((item) => {
        return {
          pressdate: item['pressdate'],
          name: item['name'],
          price: item['price'],
          isbn: item['isbn'],
          presshouse: item['presshouse'],
          // sex: i % 2 ? 1 : 0,
          checked: true,
          id: i + 1,
          writer: item['writer'],
          intro: item['intro'],
          category: item['category'],
          isflow: item['isflow'],
          picture: item['picture'],
        }
      })
      console.log("编辑后simpydata",simpydata.value)
      data.value = simpydata.value.map((item) => {
        return {
          pressdate: item['pressdate'],
          name: item['name'],
          price: item['price'],
          isbn: item['isbn'],
          presshouse: item['presshouse'],
          // sex: i % 2 ? 1 : 0,
          checked: true,
          id: item['id'],
          writer: item['writer'],
          intro: item['intro'],
          category: item['category'],
          isflow: item['isflow'],
          picture: item['picture'],
        }
      })
      console.log("编辑后data",data)
    })

  }
  const handleClose2 = async (done: () => void) => {
    console.log('加表')
    console.log(bookinfo)
    console.log(ruleFormRef)
    await ruleFormRef.value.validate((valid, fields) => {
      if (valid) {
        let obj = {
          // id: Date.now(),
          ...bookinfo,
          // author: 0,
          // summary: '我不牛逼',
          // publisher: 'Bjut 11 B105',
          // fl: 1,
          // isbn: '123456321',
          // category: '不是文学',
          // date: dayjs().format('YYYY-MM-DD'),
        }
        console.log(obj)
        console.log(title)
        if (title.value === '获取书目') {
          list.value = [obj, ...list.value]
          ElMessage.success('添加成功')
        } else {
          list.value.forEach((item) => {
            if (item.id === rowObj.value.id) {
              item.name = obj.name
              item.isflow = obj.isflow
              item.price = obj.price
              item.writer = obj.writer
              item.intro = obj.intro
              item.presshouse = obj.presshouse
              item.isbn = obj.isbn
              item.category = obj.category
              item.pressdate = obj.pressdate
              item.picture = obj.picture
            }
          })
        }
        // putbooktobook()
        dialogVisible3.value = false
        console.log('submit!', obj)
      } else {
        console.log('error submit!', fields)
      }
    })
  }
  // const closeisbnDialogy2 = () => {
  //   console.log(show.value)
  //   dialogVisible2.value = false
  //   isbnInput.value = ''
  //   bookinfo.title = ''
  //   bookinfo.fl = null
  //   bookinfo.price = null
  //   bookinfo.author = ''
  //   bookinfo.summary = ''
  //   bookinfo.publisher = ''
  //   bookinfo.isbn = ''
  //   bookinfo.category = ''
  //   bookinfo.pubdate = ''
  //   bookinfo.translator = ''
  //   bookinfo.img = ''
  // }
  const closeisbnDialogy3 = () => {
    console.log(show.value)
    dialogVisible3.value = false
  }

  const insertbook = async () => {
    // handleClose2(ruleFormRef2)
    show.value = false
    console.log(show.value)
    dialogVisible2.value = false
    console.log(bookinfo)
    getdbbook(bookinfo.isbn).then((res) => {
      console.log(bookinfo.isbn)
      console.log(res)
      console.log(res.data.isbn)
      if (res.data.status) {
        alert('图书库里已有')
      } else {
        console.log('图书库没有的添加isbn', res.data.isbn)
        getoutbook(res.data.isbn).then(async (res2) => {
          const bookinfo2 = reactive({
            name: '',
            isflow: null,
            price: null,
            writer: '',
            intro: '',
            presshouse: '',
            isbn: '',
            category: '',
            pressdate: '',
            translator: '',
            picture: '',
          })
          bookinfo2.intro = res2.data.data.summary
          bookinfo2.name = res2.data.data.title
          bookinfo2.translator = res2.data.data.translator
          bookinfo2.writer = res2.data.data.author
          bookinfo2.isbn = res2.data.data.isbn
          bookinfo2.category = res2.data.data.category
          bookinfo2.pressdate = res2.data.data.pubdate
          bookinfo2.presshouse = res2.data.data.publisher
          bookinfo2.price = res2.data.data.price
          bookinfo2.picture = res2.data.data.img
          bookinfo2.isflow = true
          bookinfo2.price = bookinfo2.price.toString().substring(0, 5)
          console.log(bookinfo2)
          await postbooktobook(bookinfo2)
          await getdballbook().then((res) => {
            const i = 1
            console.log(res.data)
            simpydata.value = res.data.map((item) => {
              return {
                pressdate: item['pressdate'],
                name: item['name'],
                price: item['price'],
                isbn: item['isbn'],
                presshouse: item['presshouse'],
                // sex: i % 2 ? 1 : 0,
                checked: true,
                id: i + 1,
                writer: item['writer'],
                intro: item['intro'],
                category: item['category'],
                isflow: item['isflow'],
                picture: item['picture'],
              }
            })
            console.log(simpydata.value)
            data.value = simpydata.value.map((item) => {
              return {
                pressdate: item['pressdate'],
                name: item['name'],
                price: item['price'],
                isbn: item['isbn'],
                presshouse: item['presshouse'],
                // sex: i % 2 ? 1 : 0,
                checked: true,
                id: item['id'],
                writer: item['writer'],
                intro: item['intro'],
                category: item['category'],
                isflow: item['isflow'],
                picture: item['picture'],
              }
            })
            console.log('提交获取所有数据', data)
          })

          // location.reload()
        })
        // postbooktobook(bookinfo)
        // postbooktobook(res.pra)
      }
    })
    isbnInput.value = ''
    bookinfo.name = ''
    bookinfo.isflow = null
    bookinfo.price = null
    bookinfo.writer = ''
    bookinfo.intro = ''
    bookinfo.presshouse = ''
    bookinfo.isbn = ''
    bookinfo.category = ''
    bookinfo.pressdate = ''
    bookinfo.translator = ''
    bookinfo.picture = ''
    // getdballbook().then((res) => {
    //   const i = 1
    //   console.log('重新传之前', data)
    //   console.log(res.data)
    //   simpydata.value = res.data.map((item) => {
    //     return {
    //       pressdate: item['pressdate'],
    //       name: item['name'],
    //       price: item['price'],
    //       isbn: item['isbn'],
    //       presshouse: item['presshouse'],
    //       // sex: i % 2 ? 1 : 0,
    //       checked: true,
    //       id: i + 1,
    //       writer: item['writer'],
    //       intro: item['intro'],
    //       category: item['category'],
    //       isflow: item['isflow'],
    //       picture: item['picture'],
    //     }
    //   })
    //   // simpydata.value = newData;
    //   console.log(simpydata.value)
    //   // const data = computed(() => {
    //   //   return simpydata.value.map((item) => {
    //   //     return {
    //   //       pressdate: item['pressdate'],
    //   //       name: item['name'],
    //   //       price: item['price'],
    //   //       isbn: item['isbn'],
    //   //       presshouse: item['presshouse'],
    //   //       checked: true,
    //   //       id: item['id'],
    //   //       writer: item['writer'],
    //   //       intro: item['intro'],
    //   //       category: item['category'],
    //   //       isflow: item['isflow'],
    //   //       picture: item['picture'],
    //   //     }
    //   //   })
    //   data.value = simpydata.value.map((item) => {
    //     return {
    //       pressdate: item['pressdate'],
    //       name: item['name'],
    //       price: item['price'],
    //       isbn: item['isbn'],
    //       presshouse: item['presshouse'],
    //       // sex: i % 2 ? 1 : 0,
    //       checked: true,
    //       id: item['id'],
    //       writer: item['writer'],
    //       intro: item['intro'],
    //       category: item['category'],
    //       isflow: item['isflow'],
    //       picture: item['picture'],
    //     }
    //   })
    //   console.log('重新传之后', data)
    //   // location.reload()
    // })
    // })
    // location.reload()
  }
  // const async function getallbook = (r2) => {
  //   getdballbook().then((res) => {
  //     const i = 1
  //     console.log(res.data)
  //     simpydata.value = res.data.map((item) => {
  //       return {
  //         pressdate: item['pressdate'],
  //         name: item['name'],
  //         price: item['price'],
  //         isbn: item['isbn'],
  //         presshouse: item['presshouse'],
  //         // sex: i % 2 ? 1 : 0,
  //         checked: true,
  //         id: i + 1,
  //         writer: item['writer'],
  //         intro: item['intro'],
  //         category: item['category'],
  //         isflow: item['isflow'],
  //         picture: item['picture'],
  //       }
  //     })
  //     console.log(simpydata.value)
  //     data.value = simpydata.value.map((item) => {
  //       return {
  //         pressdate: item['pressdate'],
  //         name: item['name'],
  //         price: item['price'],
  //         isbn: item['isbn'],
  //         presshouse: item['presshouse'],
  //         // sex: i % 2 ? 1 : 0,
  //         checked: true,
  //         id: item['id'],
  //         writer: item['writer'],
  //         intro: item['intro'],
  //         category: item['category'],
  //         isflow: item['isflow'],
  //         picture: item['picture'],
  //       }
  //     })
  //     console.log(data)
  //     return data
  //   })
  // }

  const add = () => {
    title.value = '新增'
    dialogVisible.value = true
  }
  const getbookinfo = () => {
    title.value = '获取书目'
    dialogVisible2.value = true
  }
  import { fetchbookinfo } from '../../api/test'

  function showbookdetail() {
    console.log(isbnInput.value)
    getdbbook(isbnInput.value).then((res1) => {
      console.log(res1)
      if (res1.data.status) {
        console.log('图书库里有')
        bookinfo.intro = res1.data.intro
        bookinfo.name = res1.data.name
        bookinfo.translator = ''
        bookinfo.writer = res1.data.writer
        bookinfo.isbn = res1.data.isbn
        bookinfo.category = res1.data.category
        bookinfo.pressdate = res1.data.pressdate
        bookinfo.presshouse = res1.data.presshouse
        bookinfo.price = res1.data.price
        bookinfo.picture = res1.data.picture
      } else {
        getoutbook(isbnInput.value).then((res2) => {
          console.log('图书库里没有')
          bookinfo.intro = res2.data.data.summary
          bookinfo.name = res2.data.data.title
          bookinfo.translator = res2.data.data.translator
          bookinfo.writer = res2.data.data.author
          bookinfo.isbn = res2.data.data.isbn
          bookinfo.category = res2.data.data.category
          bookinfo.pressdate = res2.data.data.pubdate
          bookinfo.presshouse = res2.data.data.publisher
          bookinfo.price = res2.data.data.price
          bookinfo.picture = res2.data.data.img
        })
      }
    })
    // fetchbookinfo(isbnInput.value).then((res) => {
    //   console.log(res.data)
    //   let res1 = res
    //   console.log(res1.data.data.summary)
    //   console.log(res1.data.data.title)
    //   console.log(res1.data.data.author)
    //   console.log(res1.data.data.isbn)
    //   console.log(res1.data.data.price)
    //   console.log(res1.data.data.publisher)
    //   console.log(res1.data.data.pubdate)
    //   console.log(res1.data.data.category)
    //   console.log(res1.data.data)
    //   console.log(res1.data)
    //
    //   bookinfo.summary = res1.data.data.summary
    //   bookinfo.title = res1.data.data.title
    //   bookinfo.translator = res1.data.data.translator
    //   bookinfo.author = res1.data.data.author
    //   bookinfo.isbn = res1.data.data.isbn
    //   bookinfo.category = res1.data.data.category
    //   bookinfo.pubdate = res1.data.data.pubdate
    //   bookinfo.publisher = res1.data.data.publisher
    //   bookinfo.price = res1.data.data.price
    //   bookinfo.img = res1.data.data.img
    // })
    show.value = true
    console.log(show.value)
  }

  const batchDelete = () => {
    if (!selectObj.value.length) {
      return ElMessage.error('未选中任何行')
    }
    ElMessageBox.confirm('你确定要删除选中项吗?', '温馨提示', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
      draggable: true,
    })
      .then(() => {
        console.log(list.value, '删除行')
        console.log(selectObj.value, '选中数据')
        selectObj.value.forEach((item) => {
          list.value = list.value.filter((item1) => item1.isbn !== item.isbn)
          deldbbook(item.isbn)
        })
        console.log(list.value)
        ElMessage.success('模拟删除成功')
        list.value = list.value.concat([])
      })
      .catch(() => {})
  }
  const selectionChange = (val) => {
    selectObj.value = val
  }

  const edit = (row) => {
    title.value = '编辑'
    rowObj.value = row
    dialogVisible3.value = true
    ruleForm.name = row.name
    ruleForm.isflow = row.isflow
    ruleForm.price = row.price
    ruleForm.writer = row.writer
    ruleForm.intro = row.intro
    ruleForm.presshouse = row.presshouse
    ruleForm.isbn = row.isbn
    ruleForm.category = row.category
    ruleForm.pressdate = row.pressdate
    ruleForm.picture = row.picture
  }

  const del = (row) => {
    console.log('row==', row)
    ElMessageBox.confirm('你确定要删除当前项吗?', '温馨提示', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
      draggable: true,
    }).then(() => {
      console.log(list.value, '删除')
      list.value = list.value.filter((item) => item.isbn !== row.isbn)
      ElMessage.success('删除成功')
      console.log(list.value)
      deldbbook(row.isbn)

      loading.value = true
      setTimeout(() => {
        loading.value = false
      }, 500)
    })
    // .catch(() => {})
  }

  const reset = () => {
    loading.value = true
    setTimeout(() => {
      loading.value = false
    }, 500)
    getdballbook().then((res) => {
      const i = 1
      console.log(res.data)
      simpydata.value = res.data.map((item) => {
        return {
          pressdate: item['pressdate'],
          name: item['name'],
          price: item['price'],
          isbn: item['isbn'],
          presshouse: item['presshouse'],
          // sex: i % 2 ? 1 : 0,
          checked: true,
          id: i + 1,
          writer: item['writer'],
          intro: item['intro'],
          category: item['category'],
          isflow: item['isflow'],
          picture: item['picture'],
        }
      })
      console.log(simpydata.value)
      data.value = simpydata.value.map((item) => {
        return {
          pressdate: item['pressdate'],
          name: item['name'],
          price: item['price'],
          isbn: item['isbn'],
          presshouse: item['presshouse'],
          // sex: i % 2 ? 1 : 0,
          checked: true,
          id: item['id'],
          writer: item['writer'],
          intro: item['intro'],
          category: item['category'],
          isflow: item['isflow'],
          picture: item['picture'],
        }
      })
      console.log('提交获取所有数据', data)
    })
    ElMessage.success('触发重置方法')
  }
  const show = ref(false)

  const onSubmit = async (val) => {
    await getdballbook().then((res) => {
      const i = 1
      console.log(res.data)
      simpydata.value = res.data.map((item) => {
        return {
          pressdate: item['pressdate'],
          name: item['name'],
          price: item['price'],
          isbn: item['isbn'],
          presshouse: item['presshouse'],
          // sex: i % 2 ? 1 : 0,
          checked: true,
          id: i + 1,
          writer: item['writer'],
          intro: item['intro'],
          category: item['category'],
          isflow: item['isflow'],
          picture: item['picture'],
        }
      })
      console.log(simpydata.value)
      data.value = simpydata.value.map((item) => {
        return {
          pressdate: item['pressdate'],
          name: item['name'],
          price: item['price'],
          isbn: item['isbn'],
          presshouse: item['presshouse'],
          // sex: i % 2 ? 1 : 0,
          checked: true,
          id: item['id'],
          writer: item['writer'],
          intro: item['intro'],
          category: item['category'],
          isflow: item['isflow'],
          picture: item['picture'],
        }
      })
      console.log('提交获取所有数据', data)
    })
    console.log('val===', val)
    console.log(typeof val.name)
    console.log(typeof data.value[0].name)
    console.log(val.name)
    console.log(data.value[0].name)
    data.value = data.value.filter((item) => {
      let result = true
      if (val.name && String(item.name) !== String(val.name)) {
        result = false
      }
      if (val.isbn && String(item.isbn) !== String(val.isbn)) {
        result = false
      }
      if (val.isflow && item.isflow !== val.isflow) {
        result = false
      }
      if (val.price && String(item.price) !== String(val.price)) {
        result = false
      }
      if (val.category && String(item.category) !== String(val.category)) {
        result = false
      }
      if (val.presshouse && String(item.presshouse) !== String(val.presshouse)) {
        result = false
      }
      return result
    })

    console.log('筛选数据', data)

    ElMessage.success('触发查询方法')
    loading.value = true
    setTimeout(() => {
      loading.value = false
    }, 500)
  }

  const getHeight = () => {}

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
