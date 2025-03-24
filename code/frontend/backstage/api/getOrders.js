import request from "./request";

//用户买卖和平台相反
export async function getsellorders() {
    return request.get(`buyorder/`)
}


export async function getbuyorders() {
    return request.get(`sellorder/`)
}