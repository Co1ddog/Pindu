import api from "./api.js";
import outApi from '@/api/isbnapi'


export async function getCartbook(uid) {
    return api.get(`cart/${uid}/`)
}
export async function getCartbookdetail(inventry) {
    return api.get(`inventorydetail/${inventry}/`)
}

export async function postbooktoCart(info) {
    return api.post('cart/', info)
}
//
// export async function getbuyrate(info) {
//     return api.post('conditionrate/', info)
// }

export async function patchreducebooktoCart(uid,inventory) {
    return api.post(`cartminus/`,{user_id:uid,inventory:inventory})
}

export async function patchbooktoCart(uid,isbn,pinxiang) {
    return api.post(`cart/`,{user_id:uid,inventory_book_isbn:isbn,inventory_conditionrate_name:pinxiang,book_num:1})
}
export async function deleteCartBook(id) {
    return api.delete(`cart/${id}/`)
}
