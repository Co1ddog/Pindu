import api from './api';

export async function createBuyOrder(data) {
    return api.post('buyorder/', data)
}

export async function createBuyOrderDetail(data) {
    return api.post('buyorderdetail/', data)
}

export async function loadBuyOrder(uid) {
    return api.get(`buyorder/${uid}`)
}

export async function loadBuyOrderDetail(uid) {
    return api.get(`buyorderdetail/${uid}`)
}

export async function createSellOrder(data) {
    return api.post('sellorder/', data)
}

export async function createSellOrderDetail(data) {
    return api.post('sellorderdetail/', data)
}

export async function loadSellOrder(uid) {
    return api.get(`sellorder/${uid}`)
}

export async function loadSellOrderDetail(uid) {
    return api.get(`sellorderdetail/${uid}`)
}
