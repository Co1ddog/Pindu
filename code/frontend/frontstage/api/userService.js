import api from "./api";

export async function userDetail(user_id) {
    return api.get(`userdetail/${user_id}`)
}

export async function userModify(user_id, data) {
    return api.patch(`userdetail/${user_id}/`, data)
}

export async function userCPassword(data) {
    return api.post('userchangepassword/', data)
}

export async function userTPassword(data) {
    return api.post('userverifypw/', data)
}

