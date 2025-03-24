import api from "./api.js";
import outApi from '@/api/isbnapi'


export async function getSalebook(uid) {
    return api.get(`warehouse/uid=${uid}`)
}

export async function getoutbook(isbn) {
    return outApi.get(`isbn?isbn=${isbn}&uKey=33b4c461da6946eca5c7fae235c5da9e`)
}

export async function postbooktowarehouse(info) {
    return api.post('warehouse/', info)
}

export async function deleteWareHouseBook(id) {
    return api.delete(`warehouse/${id}`)
}



