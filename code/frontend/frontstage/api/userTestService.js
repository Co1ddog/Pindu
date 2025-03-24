import api from "./api";

export default {
    addUserAddress(user) {
        return api.post('usertest/', user).then(r => {
            r.data
        })
    },

    loadUserAddress() {
        return api.get('usertest/')
    }
}