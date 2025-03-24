<template>
  <BookshopNavigator/>
  <BookshopFilter v-on="$attrs"/>

</template>

<script setup>
import BookshopNavigator from "@/components/shop/BookshopNavigator.vue";
import BookshopFilter from "@/components/shop/BookshopFilter.vue";


</script>

<style scoped>

</style>