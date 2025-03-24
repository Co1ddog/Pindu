import api from './api';

export async function addUserAddress(data) {
    return api.post('useraddress/', data)
}

export async function loadUserAddress(uid) {
    return api.get(`useraddress/${uid}`)
}

export async function modifyUserAddress(id, data) {
    return api.patch(`useraddress/${id}/`, data)
}

export async function deleteUserAddress(id) {
    return api.delete(`useraddress/${id}/`)
}