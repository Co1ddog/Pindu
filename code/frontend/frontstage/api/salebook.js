import api from '@/api/api'

export default {
    getSalebook(uid) {
        return api.get(`warehouse/uid=${uid}`)
    },
    addSalebook(todo) {
        return api.post('sale/', salebook).then(response => response.data)
    },
    deleteSalebook(msgId) {
        return api.delete(`sale/${msgId}`)
            .then(response => response.data)
    },

}