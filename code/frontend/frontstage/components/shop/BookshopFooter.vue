<template>
  <div
      style="background-color: #282828; height:auto;display: flex;align-items: end;justify-content: center;">
    <div
        style="width: 90%;display: flex;align-items: center;justify-content: center; background-color: white;border-bottom: 20px solid white;">
<!--      <Pagination />-->
<!--      <Pagination v-model="page" :page-size="6" :total="books.length" style="background-color: white" size="large"/>-->
    </div>
  </div>
</template>

<script>
import Pagination from "@/components/shop/Pagination.vue";
import {onMounted, reactive, ref} from "vue";
import {getBookIsFlow} from "../../api/GetBookService";

const page = ref(1);

export default {
  name: "BookshopFooter",
  components: {Pagination}
}
const books = reactive([])

onMounted(async () => {
  const response = await getBookIsFlow()
  books.push(...response.data)
  console.log(books)
})
</script>

<style scoped>

</style>