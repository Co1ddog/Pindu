<template>
  <div v-if="display">
    <!--    <GuessYouLike/>-->
    <div style="background-color: #181818; padding: 0 10px; height: 480px">
      <h1 style="color: white;font-weight: bold;padding-left: 30px;padding-top: 15px">猜你喜欢</h1>
      <el-carousel height="360px" indicator-position="outside" autoplay >
        <el-carousel-item >
          <div class="outer">
            <div v-for="(val, ind) in page1" class="middle">
              <div class="inner">
                <img :src="val.picture" alt="">
              </div>
              <p class="name">{{ val.name }}</p>
              <p>{{ val.intro }}</p>
            </div>
          </div>
        </el-carousel-item>

        <el-carousel-item>
          <div class="outer">
            <div v-for="(val, ind) in page2" class="middle">
              <div class="inner">
                <img :src="val.picture" alt="">
              </div>
              <p class="name">{{ val.name }}</p>
              <p>{{ val.intro }}</p>
            </div>
          </div>
        </el-carousel-item>

        <el-carousel-item>
          <div class="outer">
            <div v-for="(val, ind) in page3" class="middle">
              <div class="inner">
                <img :src="val.picture" alt="">
              </div>
              <p class="name">{{ val.name }}</p>
              <p>{{ val.intro }}</p>
            </div>
          </div>
        </el-carousel-item>

        <el-carousel-item>
          <div class="outer">
            <div v-for="(val, ind) in page4" class="middle">
              <div class="inner">
                <img :src="val.picture" alt="">
              </div>
              <p class="name">{{ val.name }}</p>
              <p>{{ val.intro }}</p>
            </div>
          </div>
        </el-carousel-item>
      </el-carousel>
    </div>
  </div>
</template>

<script setup>
import {onBeforeMount, onMounted, reactive, ref} from "vue";
import {getBookIsFlow} from "../../api/GetBookService";

const display = ref(false)
const books = []
let shuffled_books = reactive([])

let page1 = reactive([])
let page2 = reactive([])
let page3 = reactive([])
let page4 = reactive([])

const shuffle = (arr) => {
  let l = arr.length;
  let index, temp;
  while (l > 0) {
    index = Math.floor(Math.random() * l)
    temp = arr[l - 1]
    arr[l - 1] = arr[index]
    arr[index] = temp
    l--
  }
  return arr
}

onBeforeMount(async () => {
  await getBookIsFlow().then(r => {
    r.data.forEach((e, i) => books.push(e))
  })

  shuffled_books = shuffle(books)
  page1 = shuffled_books.slice(0, 5)
  page2 = shuffled_books.slice(5, 10)
  page3 = shuffled_books.slice(10, 15)
  page4 = shuffled_books.slice(15, 20)
  display.value = true
  console.log(page1)
})
</script>

<style scoped>
img {
  width: auto;
  height: 200px;
}

p {
  padding: 3px 15px;
  color: white;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 4;
  overflow: hidden;
}


.outer {
  display: -webkit-flex;
  display: flex;
  -webkit-justify-content: space-around;
  justify-content: space-around;
  padding: 15px 10px;
}

.middle {
  height: 350px;
  width: 370px;
  background-color: #282828;
}

.inner {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 96%;
  margin-left: 2%;
  background-color: white;
}

.bookintro {
  color: #f2f2f2;
  font-weight: bold;
  padding: 0 15px;
  margin: 0;
}

.name {
  color: #f2f2f2;
  font-size: large;
  font-weight: bold;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 1;
  overflow: hidden;
  padding-bottom: 0;
  padding-top: 6px;
}

</style>