<template>
    <div>
        <el-container class="container">
            <el-header>
        <span class="tittle">
          基本信息
        </span>
            </el-header>
            <el-main>
                <el-row class="row-bg" justify="center">
                    <el-col :span="6">
                        <el-avatar class="portrait" :icon="UserFilled"/>
                    </el-col>
                </el-row>
                <br>
                <el-row>
                    <el-col :span="3" :offset="6">
                        <span style="color: #FFFFFF">名字</span>
                    </el-col>
                    <el-col span="7" offset="7">
                        <!--                        <el-label disabled="T" style="width: 220px" v-model="name" placeholder="Please input"/>-->
                        <p style="color: white">{{ name }}</p>
                    </el-col>
                </el-row>
                <br>
                <el-row>
                    <el-col :span="3" :offset="6">
                        <span style="color: #FFFFFF">性别</span>
                    </el-col>
                    <el-col span="7" offset="7">
                        <!--            <el-select disabled="T" v-model="value" style="width: 220px" class="m-2" placeholder="Select">-->
                        <!--&lt;!&ndash;              <el-option&ndash;&gt;-->
                        <!--&lt;!&ndash;                  v-for="item in options"&ndash;&gt;-->
                        <!--&lt;!&ndash;                  :key="item.value"&ndash;&gt;-->
                        <!--&lt;!&ndash;                  :label="item.label"&ndash;&gt;-->
                        <!--&lt;!&ndash;                  :value="item.value"&ndash;&gt;-->
                        <!--&lt;!&ndash;              />&ndash;&gt;-->
                        <!--            </el-select>-->
                        <p>{{ gender }}</p>
                    </el-col>
                </el-row>
                <br>
                <el-row>
                    <el-col :span="3" :offset="6">
                        <span style="color: #FFFFFF">生日</span>
                    </el-col>
                    <el-col span="7" offset="7">
                        <div class="block">
                            <!--              <el-date-picker-->
                            <!--                  v-model="value1"-->
                            <!--                  type="date"-->
                            <!--                  placeholder="Pick a day"-->
                            <!--                  :size="size"-->
                            <!--                  disabled="T"-->
                            <!--              />-->
                            <p>{{ birth }}</p>
                        </div>
                    </el-col>
                </el-row>
                <br>
                <el-row justify="center">
                    <el-col span="5" :pull="2">
                        <router-link :to="{name: 'changeself'}">
                            <el-button>修改个人信息</el-button>
                        </router-link>
                    </el-col>
                </el-row>
            </el-main>
        </el-container>
    </div>
</template>

<script  setup>
import {UserFilled} from "@element-plus/icons-vue";
import {onBeforeMount, onBeforeUpdate, onMounted, ref} from 'vue'
import {userDetail, userModify} from "../../api/userService";

// onBeforeMount(() => {
//   name.value = window.sessionStorage.getItem('username')
//   gender.value = window.sessionStorage.getItem('gender')
//   birth.value = window.sessionStorage.getItem('phone')
// })



let name = ref()
let gender = ref()
let birth = ref()
const user_id = ref()
onMounted(() => {
    user_id.value = window.sessionStorage.getItem("id")
    userDetail(user_id.value).then((r) => {
        console.log(r.data)
        name.value = r.data.first_name
        gender.value= r.data.gender
        birth.value = r.data.birth
        console.log(name)
        birth.value = r.data.birth
    })

})


</script>

<style scoped>
p {
    color: white;
}

.tittle {
    color: aqua;
    font-size: 16px;
}

.portrait {

}


</style>