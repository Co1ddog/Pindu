import request from './request'

export async function feedbackList() {
  return request.get('feedback/')
}

export async function feedbackUpdate(feedback_id, body) {
  return request.patch(`feedback/${feedback_id}/`, body)
}

export async function feedbackDelete(feedback_id) {
  return request.delete(`feedback/${feedback_id}/`)
}

export async function feedbackSearch(body) {
  return request.post('feedbacksearch/', body)
}

export async function feedbackListPending() {
  return request.get('feedbackpending/')
}

export async function feedbackListPendingFromAsset() {
  return request.get('feedbackpendingfromasset/')
}

export async function feedbackListFromAftersale() {
  return request.get('feedbackfromaftersale/')
}

export async function feedbackListPendingFromAftersale() {
  return request.get('feedbackpendingfromaftersale/')
}
