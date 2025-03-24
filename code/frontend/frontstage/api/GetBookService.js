import api from "./api.js";
import outApi from '@/api/isbnapi'

export async function getdbbook(isbn) {
    return api.get((`book/${isbn}/`))
}

export async function getdballbook() {
    return api.get((`book/`))
}

export async function getbuyrate(info){
    return api.get(`conditionrate/`,info)
}

export async function postbooktobook(info) {
    return api.post('book/', info)
}

export async function postbooktowarehouse(info) {
    return api.post('warehouse/', info)
}

export function getBookIsFlow() {
    return api.get('bookisflow')
}

export async function getBookCondition() {
    return api.get('conditionrate/')
}
export async function getBookInventory(isbn) {
    return api.get(`inventory/${isbn}`)
}

export async function getCartNum(user_id,isbn,condition) {
    return api.get(`cartinventorynum/${user_id}/${isbn}/${condition}`)
}
export async function getBookCategory(cate, press, price, search, havinv) {
    let s = '-'
    if (search !== '')
        s = search
    return api.get(`bookcate/${cate}/${press}/${price}/${s}/${havinv}/`)
}

export async function getBookPresshouse(cate, press, price, search, havinv) {
    let s = '-'
    if (search !== '')
        s = search
    return api.get(`bookpress/${cate}/${press}/${price}/${s}/${havinv}/`)
}

export async function getBookByCategoryPresshousePriceSearchHaveinv(cate, press, price, search, havinv) {
    let s = '-'
    if (search !== '')
        s = search
    return api.get(`bookcatepresspricesearch/${cate}/${press}/${price}/${s}/${havinv}/`)
}
