import request from './request'

export function login(data) {
  return request.post('adminlogin/', data)
}

export function getAdminInfo(adminid) {}
