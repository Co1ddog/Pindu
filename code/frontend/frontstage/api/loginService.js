import router from "@/router";
import api from '@/api/api'

export default {
    Register(username, password, nickname) {
        return api.post('/userregister/', {username: username, password: password, nickname: nickname})
    },

    Login(username, password) {
        return api.post('/userlogin/', {username: username, password: password})
    },

    GetUserInformation(user_id) {
        return api.get(`/userdetail/${user_id}`)
    },


}

//
// export function Login(username, password) {
//     return api.post('/login/', {username: username, password: password})
// }