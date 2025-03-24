import request from './request'

export async function updaterate(id, buyrate, sellrate) {
    return request.patch(`conditionrate/${id}/`, {buy_rate: buyrate, sell_rate: sellrate})
}

export async function updatebuyrate(id, buyrate) {
    return request.patch(`conditionrate/${id}/`, {buy_rate: buyrate})
}

export async function updatesellrate(id, sellrate) {
    return request.patch(`conditionrate/${id}/`, {sell_rate: sellrate})
}

export async function getrate() {
    return request.get(`conditionrate/`)
}
