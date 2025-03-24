import request from './request'

export async function changeInventoryNum(inventory_id, data) {
    return request.patch(`inventory/${inventory_id}/`, data)
}

export async function loadInventoryNum(inventory_id) {
    return request.get(`inventorydetail/${inventory_id}/`)
}