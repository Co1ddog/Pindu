<template>
  <div style="height:75px;width: 100%; display: flex; align-items: center; justify-content: center;">
    <div style="width: 90%; height: 100%;background-color: white; padding: 0 20px;color: white">

      <p style="font-weight: bold; color: black">图书类别：</p>
      <RouterLink v-for="(value, key) in category" style="margin:0"
                  @click="$emit('sendSelectedCategory', value.category)" to>
        <p style="white-space: nowrap;margin: 0;color: black;">
          {{ value.category }}
        </p>
        <p style="margin: 0 10px 0 0; color: deeppink">
          ({{ value.total }}),
        </p>
      </RouterLink>


      <br>
      <p style="font-weight: bold; color: black">出版社：</p>
      <RouterLink to="">
        我我我哦我我我
      </RouterLink>
      <RouterLink to="">
        我我我哦我我我
      </RouterLink>
      <RouterLink to="">
        我我我哦我我我
      </RouterLink>
    </div>
  </div>
</template>

<script setup>
import {inject, onMounted, reactive} from "vue";
import {getBookByCategory, getBookCategory} from "../../api/GetBookService";

const category = reactive([])
onMounted(() => {
  getBookCategory().then(r => {
    console.log(r.data)
    r.data.forEach((element, index) => {
      category.push(element)
    })
    console.log(category)
    // emit('send-selected-category', 1);
  })
})

const emit = inject('$emit', null);
const sendSelectedCategory = (category) => {
  if (emit) {
    emit('send-selected-category', category);
    console.log("send了")
  } else {
    console.log("emit?:", emit)
    console.warn('Warning: $emit is not available in this component');
  }
}


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
  margin: 2px 20px;
  display: inline-block;
}
</style>