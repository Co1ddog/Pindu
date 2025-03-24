import request from './request'

//用户买卖和平台相反
export async function getsellorderdetail(oid) {
    return request.get((`buyorderdetail/${oid}/`))
}

export async function getbuyorderdetail(id) {
    return request.get(`sellorderdetail/${id}/`)
}