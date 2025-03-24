<template>
  <div style="background-color: #282828;">
    <div style="height: auto;width: 100%; display: flex; align-items: center; justify-content: center">
      <div
          style="width: 90%; height: 100%;background-color: white; padding: 20px 20px 5px;color: white; display: flex;align-items: center;justify-content: space-between">
        <h1 style="font-weight: bolder; color: black; padding-bottom: 8px;display: inline">品读 · 商店</h1>
        <div style="float: right">
          <n-input round placeholder="搜索一本书嘿嘿" :value="search" @input="search = $event" style="width: 230px"
                   @keydown.enter.native="handleSearch" clearable>
            <template #suffix>
              <n-icon :component="FlashOutline"/>
            </template>
          </n-input>
        </div>
      </div>
    </div>

    <div style="height:auto;width: 100%; display: flex; align-items: center; justify-content: center;">
      <div style="width: 90%; height: 100%;background-color: white; padding: 0 40px;color: white; ">

        <p style="font-weight: bold; color: black; margin: 2px -5px 2px 5px">图书类别：</p>
        <p style="white-space: nowrap;color: #cb3b3b;font-weight: bold; margin-right: 15px">({{ selected.cate }}) </p>
        <RouterLink @click="changeSelectedCate('-')" style="margin:0" to>
          <p style="white-space: nowrap;margin: 0;">
            全部
          </p>
          <p style="margin: 0 10px 0 0; color: deeppink">
            ({{ books.length }})
          </p>
        </RouterLink>
        <RouterLink v-for="(value, key) in category" style="margin:0"
                    @click="changeSelectedCate(value.category)" to>
          <p style="white-space: nowrap;margin: 0;">
            {{ value.category }}
          </p>
          <p style="margin: 0 10px 0 0; color: deeppink">
            ({{ value.total }})
          </p>
        </RouterLink>
        <br>

        <p style="font-weight: bold; color: black;margin: 2px -5px 2px 5px">出版社：</p>

        <p style="white-space: nowrap;color: #cb3b3b;font-weight: bold; margin-right: 15px">({{
            selected.press
          }}) </p>
        <RouterLink @click="changeSelectedPress('-')" style="margin:0" to>
          <p style="white-space: nowrap;margin: 0;">
            全部
          </p>
          <p style="margin: 0 10px 0 0; color: deeppink">
            ({{ books.length }})
          </p>
        </RouterLink>
        <RouterLink v-for="(value, key) in presshouse" style="margin:0"
                    @click="changeSelectedPress(value.presshouse)" to>
          <p style="white-space: nowrap;margin: 0;">
            {{ value.presshouse }}
          </p>
          <p style="margin: 0 10px 0 0; color: deeppink">
            ({{ value.total }})
          </p>
        </RouterLink>
        <br>

        <p style="font-weight: bold; color: black;margin: 2px -5px 2px 5px">价格：</p>
        <p style="white-space: nowrap;color: #cb3b3b;font-weight: bold; margin-right: 15px">({{ selected.price }}) </p>
        <RouterLink @click="changeSelectedPrice('-')" style="margin:0" to>
          <p style="white-space: nowrap;margin: 0;">
            全部
          </p>
          <p style="margin: 0 10px 0 0; color: deeppink">
            ({{ books.length }})
          </p>
        </RouterLink>
        <RouterLink v-for="(value, key) in price" style="margin:0" @click="changeSelectedPrice(value.price)" to>
          <p style="white-space: nowrap;margin: 0 20px 0 0;">
            {{ value.name }}
          </p>
        </RouterLink>
        <br>

        <p style="font-weight: bold; color: black;margin: 2px -5px 2px 5px">其他筛选：</p>
        <p style="white-space: nowrap;color: #cb3b3b;font-weight: bold; margin-right: 15px">({{ selected.havinv }}) </p>
        <RouterLink @click="changeSelectedHavinv('-')" style="margin:0" to>
          <p style="white-space: nowrap;margin: 0;">
            全部
          </p>
          <p style="margin: 0 10px 0 0; color: deeppink">
            ({{ books.length }})
          </p>
        </RouterLink>
        <RouterLink style="margin:0" @click="changeSelectedHavinv('只看有货')" to>
          <p style="white-space: nowrap;margin: 0;">
            只看有货
          </p>
        </RouterLink>

      </div>
    </div>

    <div style="width: 100%;display: flex;align-items: center;justify-content: center; ">
      <div style="height: 90%; width: 90%; background-color: white; padding: 20px 20px; ">
        <el-row v-for="(page, index) of page_num" :key="index" :gutter="20" justify="space-evenly" align="middle"
                style="padding-bottom: 20px">
          <el-col :span="4" v-for="(item, innerindex) of page" :key="item.isbn">
            <BookItemShop :book-isbn="item.isbn" :book-cover="item.picture" :book-title="item.name"
                          :book-introduction="item.intro" :book-price="item.price"/>
          </el-col>
        </el-row>
        <div style="background-color: #ffffff; height:auto;display: flex;align-items: center;justify-content: center;">
          <el-pagination v-model="currentPage" :page-size="18" :total="books.length" @size-change="handleSizeChange"
                         @current-change="handleCurrentChange" style="background-color: white" size="large"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import {FlashOutline} from "@vicons/ionicons5";
import BookItemShop from "@/components/shop/BookItem-shop.vue";
import {computed, onMounted, reactive, ref, watch} from "vue";
import {
  getBookByCategoryPresshousePriceSearchHaveinv,
  getBookCategory,
  getBookIsFlow,
  getBookPresshouse,
} from "../api/GetBookService";

const currentPage = ref(1);
const handleSizeChange = (pageSize) => {
  currentPage.value = 1
}

const handleCurrentChange = (page) => {
  currentPage.value = page
}

const cur_page = ref(1)
const page_num = computed(() => {
  const rows = []
  const start = (currentPage.value - 1) * 18
  const end = start + 18
  books.slice(start, end).forEach((item, index) => {
    const row = Math.floor(index / 6)
    if (!rows[row]) {
      rows[row] = []
    }
    rows[row].push(item)
  })
  return rows
})


const onPageChange = (val) => {
  cur_page.value = val
}

const selected = reactive({
  cate: '-',
  press: '-',
  price: '-',
  havinv: '-'
})

const search = ref('')

const handleSearch = () => {
  console.log(selected.cate, selected.press, selected.price, search.value, selected.havinv)
  getBookByCategoryPresshousePriceSearchHaveinv(selected.cate, selected.press, selected.price, search.value, selected.havinv).then(r => {
    books.splice(0)
    r.data.forEach((element, index) => {
      books.push(element)
    })
    getBookCategory(selected.cate, selected.press, selected.price, search.value, selected.havinv).then(r => {
      category.splice(0)
      r.data.forEach((element, index) => {
        category.push(element)
      })
      getBookPresshouse(selected.cate, selected.press, selected.price, search.value, selected.havinv).then(r => {
        presshouse.splice(0)
        r.data.forEach((element, index) => {
          presshouse.push(element)
        })

        // getBookCategory(selected.cate, selected.press, selected.price, search.value).then(r => {
        //   category.splice(0)
        //   r.data.forEach((element, index) => {
        //     category.push(element)
        //   })
        //
        //   getBookPresshouse(selected.cate, selected.press, selected.price, search.value).then(r => {
        //     presshouse.splice(0)
        //     r.data.forEach((element, index) => {
        //       presshouse.push(element)
        //     })
        //   })
        // })
      })
    })
  })
}


const price = reactive([
  {name: '小于30', price: '0,30'},
  {name: '30-50', price: '30,50'},
  {name: '50-100', price: '50,100'},
  {name: '100以上', price: '100,999'},
])


const changeSelectedCate = (s) => {
  selected.cate = s
}
const changeSelectedPress = (p) => {
  selected.press = p
}
const changeSelectedPrice = (p) => {
  selected.price = p
}
const changeSelectedHavinv = (h) => {
  selected.havinv = h
}

watch(() => selected.cate, (newVal) => {
  getBookByCategoryPresshousePriceSearchHaveinv(newVal, selected.press, selected.price, search.value, selected.havinv).then(r => {
    books.splice(0)
    r.data.forEach((element, index) => {
      books.push(element)

      getBookCategory(newVal, selected.press, selected.price, search.value, selected.havinv).then(r => {
        category.splice(0)
        r.data.forEach((element, index) => {
          category.push(element)
        })

        getBookPresshouse(newVal, selected.press, selected.price, search.value, selected.havinv).then(r => {
          presshouse.splice(0)
          r.data.forEach((element, index) => {
            presshouse.push(element)
          })
        })
      })
    })
  })
})
watch(() => selected.press, (newVal) => {
  getBookByCategoryPresshousePriceSearchHaveinv(selected.cate, newVal, selected.price, search.value, selected.havinv).then(r => {
    books.splice(0)
    r.data.forEach((element, index) => {
      books.push(element)

      getBookCategory(selected.cate, newVal, selected.price, search.value, selected.havinv).then(r => {
        category.splice(0)
        r.data.forEach((element, index) => {
          category.push(element)
        })

        getBookPresshouse(selected.cate, newVal, selected.price, search.value, selected.havinv).then(r => {
          presshouse.splice(0)
          r.data.forEach((element, index) => {
            presshouse.push(element)
          })
        })
      })
    })
  })
})
watch(() => selected.price, (newVal) => {
  getBookByCategoryPresshousePriceSearchHaveinv(selected.cate, selected.press, newVal, search.value, selected.havinv).then(r => {
    books.splice(0)
    r.data.forEach((element, index) => {
      books.push(element)

      getBookCategory(selected.cate, selected.press, newVal, search.value, selected.havinv).then(r => {
        category.splice(0)
        r.data.forEach((element, index) => {
          category.push(element)
        })

        getBookPresshouse(selected.cate, selected.press, newVal, search.value, selected.havinv).then(r => {
          presshouse.splice(0)
          r.data.forEach((element, index) => {
            presshouse.push(element)
          })
        })
      })
    })
  })
})
watch(() => selected.havinv, (newVal) => {
  getBookByCategoryPresshousePriceSearchHaveinv(selected.cate, selected.press, selected.price, search.value, newVal).then(r => {
    books.splice(0)
    r.data.forEach((element, index) => {
      books.push(element)

      getBookCategory(selected.cate, selected.press, selected.price, search.value, newVal).then(r => {
        category.splice(0)
        r.data.forEach((element, index) => {
          category.push(element)
        })

        getBookPresshouse(selected.cate, selected.press, selected.price, search.value, newVal).then(r => {
          presshouse.splice(0)
          r.data.forEach((element, index) => {
            presshouse.push(element)
          })
        })
      })
    })
  })
})


const all_books = reactive([])
let books = reactive([])
const category = reactive([])
const presshouse = reactive([])


onMounted(() => {
  getBookCategory('-', '-', '-', '-', '-').then(r => {
    r.data.forEach((element, index) => {
      category.push(element)
    })
    getBookPresshouse('-', '-', '-', '-', '-').then(r => {
      r.data.forEach((element, index) => {
        presshouse.push(element)
      })
      getBookIsFlow().then(r => {
        r.data.forEach((element, index) => {
          books.push(element)
          all_books.push(element)
        })
      })
    })
  })
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
.router-link-active {
  text-decoration-line: none;
  color: midnightblue;
  margin-right: 10px;
}

.router-link-active:hover {
  color: red;
  text-shadow: 0 0 10px greenyellow;
  /*box-shadow: 0 0 10px white;*/
}

p {
  margin: 2px 5px;
  display: inline-block;
}

</style>