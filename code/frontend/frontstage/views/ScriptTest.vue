<template>
  <div style="height: 500px;display: flex;align-items: center;justify-content: center;">
    <div>
      <!--      <h1 style="color: white; font-weight: bolder">这是ShopView</h1>-->

      <form>
        <input type="text" name="todo" v-model="todo_text">
        <br>
        <input type="submit" value="subm" @click="handleSubmit">
      </form>

      <ul>
        <li v-for="todo in state.todos">
          {{ todo.todo_id }} ------> {{ todo.todo_text }}
        </li>
      </ul>

      <button autofocus @click="loadTodos">Load</button>
      <p style="color: #181818">{{ state }}</p>
    </div>
  </div>
</template>

<script setup>
import todoService from "@/api/old/todoService";
import {onMounted, reactive, ref} from "vue";

const state = reactive({
  todos: []
})

const loadTodos = () => {
  console.log("点了按钮")
  todoService.getTodos().then(r => {
    state.todos = r.data
  })
}

const todo_text = ref()
const handleSubmit = (e) => {
  // 防止闪屏
  e.preventDefault()
  console.log("点了subm")
  todoService.addTodo({todo_id: 0, todo_text: todo_text.value}).then(r => {
    console.log(r)
    loadTodos()
    todo_text.value = ''
  })
}

onMounted(() => {
  loadTodos()
})
</script>


<!--<script>
import todo from '@/api/todoService'

export default {
  name: 'ShopView',
  data() {
    return {
      test: 'test',
      todos: null,
      todo_create: '',
    }
  },
  methods: {
    refreshTodo() {
      todo.getTodos()
          .then(resp => {
            console.log(resp)
            this.todos = resp.data
          })
    },
    handleSubmit(e) {
      e.preventDefault()
      const text = this.todo_create
      console.log(text)
      todo.addTodo({'todo_text': text})
          .then(resp => {
            this.todo_create = ''
            this.refreshTodo()
          })
    },
    handleDelete(id) {
      todo.deleteTodo(id).then(resp => {
        this.refreshTodo()
      })
      console.log(id)
    }
  },
  mounted() {
    this.refreshTodo()
  },
}
</script>-->

<style scoped>
li {
  color: black;
}
</style>