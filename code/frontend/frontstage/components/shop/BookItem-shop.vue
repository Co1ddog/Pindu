<template>
  <RouterLink :to="{name:'bookinfo',params:{isbn:bookIsbn}}" style="text-decoration-line: none">
    <n-card class="n-card" size="small">
      <template #cover>
        <div style="height: 200px; width: 100% ; display: flex; align-items: center; justify-content: center">
          <img :src="bookCover" :alt="bookCover" style="width: auto;height: auto;max-width: 100%;max-height: 100%;">
        </div>
      </template>
      <h4 class="booktitle">
        {{ bookTitle }}
      </h4>
      <p>{{ bookIntroduction }}</p>
      <div style="height: 100%; width: 100%">
        <n-space align="center" style="float: right; padding-top: 10px">
          <h3 style="display: inline; margin: auto 0;color: black">{{ bookPrice }} 元</h3>
          <n-button circle ghost color="red" size="medium">
            <template #icon>
              <n-icon>
                <IconAddToCart/>
              </n-icon>
            </template>
          </n-button>
        </n-space>

      </div>
    </n-card>
  </RouterLink>
</template>

<script setup>
import IconAddToCart from "@/components/icons/IconAddToCart.vue";

defineProps(['bookIsbn','bookCover', 'bookTitle', 'bookIntroduction', 'bookPrice'])


</script>

<style scoped>
.booktitle {
  color: black;
  margin-top: 8px;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
  overflow: hidden;
}

.booktitle:hover {
  color: orangered;
}

.n-card {
  border-width: 3px;
  width: 100%;
  height: 400px;
  /*display:inline;*/
}

.n-card:hover {
  border-color: #fc5185;
  filter: brightness(1.1);
  box-shadow: 0 0 15px #43dde6;
  /*padding: 10px*/
}

p {
  color: dimgray;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 4;
  overflow: hidden;
}
</style>