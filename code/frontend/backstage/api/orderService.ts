import request from './request'

export async function loadBuyOrder() {
    return request.get('buyorder/')
}

export async function changeBuyOrder(oid, data) {
    return request.patch(`buyorder/${oid}/`, data)
}

export async function loadBuyOrderDetail(oid) {
    return request.get(`buyorderdetail/${oid}/`)
}


export async function sellOrders() {
  return request.get('sellorder/')
}
export async function sellOrderByUser(User_id) {
  return request.get(`sellorder/${User_id}`)
}
export async function sellOrder0() {
  return request.get(`sellorder/status=0`)
}
export async function sellOrder1() {
  return request.get(`sellorder/status=1`)
}
export async function sellOrderDetail(oid) {
  return request.get(`sellorderdetail/${oid}`)
}
export async function getBookCondition() {
  return request.get('conditionrate/')
}
export async function sellCheckCondition(id, form) {
  return request.patch(`sellorderdetailpatch/${id}/`, form)
}
export async function selldetailModify(id, status) {
  return request.patch(`sellorder/${id}/`, status)
}
export async function modifyBalance(user_id,balance) {
  return request.patch(`userdetail/${user_id}/`, balance)
}
export async function userDetail(user_id) {
  return request.get(`userdetail/${user_id}/`)
}
export async function addInventory(form) {
  return request.post(`inventory/`,form)
}

