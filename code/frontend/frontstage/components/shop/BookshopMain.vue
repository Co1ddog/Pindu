<template>
  <div style="width: 100%;display: flex;align-items: center;justify-content: center">
    <div style="height: 90%; width: 90%; background-color: white; padding: 0 20px 20px;">
      <p>asdasd</p>
      <el-row v-for="(page, index) of row_num" :key="index" :gutter="20" justify="space-evenly" align="middle">
        <el-col :span="4" v-for="(item, innerindex) of page" :key="item.isbn">
          <BookItemShop :book-isbn="item.isbn" :book-cover="item.picture" :book-title="item.name"
                        :book-introduction="item.intro"
                        :book-price="item.price"/>
        </el-col>
      </el-row>

    </div>
  </div>
</template>

<script setup>
import BookItemShop from "@/components/shop/BookItem-shop.vue";
import {computed, onMounted, onUpdated, reactive, ref, toRefs, watch, watchEffect} from "vue";
import {getBookByCategory, getBookIsFlow} from "../../api/GetBookService";

const props = defineProps(['selected_cate'])
let books = reactive([])
let s = ref(props.selected_cate)

console.log(props.selected_cate)

watch(
    () => props.selected_cate,
    (newVal) => {
      getBookByCategory(newVal).then(r => {
        books = []
        r.data.forEach((element, index) => {
          books.push(element)
        })
        console.log("books:", books)
        row_num = computed(() => {
          const rows = []
          books.forEach((item, index) => {
            const row = Math.floor(index / 6)
            if (!rows[row]) {
              rows[row] = []
            }
            rows[row].push(item)
          })
          return rows
        })
        console.log(row_num.value)
      })
    }
);

onMounted(async () => {
  const response = await getBookIsFlow()
  books.push(...response.data)
  // s.value = '1'
  console.log(books)
})

let row_num = computed(() => {
  const rows = []
  books.forEach((item, index) => {
    const row = Math.floor(index / 6)
    if (!rows[row]) {
      rows[row] = []
    }
    rows[row].push(item)
  })
  return rows
})

</script>

<style scoped>
.el-row {
  margin-bottom: 20px;
}

.el-row:last-child {
  margin-bottom: 0;
}

.el-col {
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
  background-color: red;
}
</style>