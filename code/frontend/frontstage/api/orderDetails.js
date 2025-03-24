import api from "./api.js";

export async function getsellorderdetail(order_id) {
    return api.get((`sellorderdetail/${order_id}/`))
}

export async function getbuyorderdetail(id) {
    return api.get((`buyorderdetail/${id}/`))
}

export async function feedback(id, question) {
    return api.post(`feedback/`, {user: id, que_content_user2aftersaleman: question})
}