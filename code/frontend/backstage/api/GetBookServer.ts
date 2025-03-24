import api from './request'
import outApi from './isbnapi'
import { toRaw } from 'vue'

export async function getdbbook(isbn: any): Promise<any> {
  console.log(isbn)
  const data = toRaw(isbn)
  return api.get(`book/${isbn}/`)
}

export async function deldbbook(isbn: any): Promise<any> {
  console.log(isbn)
  const data = toRaw(isbn)
  return api.delete(`book/${isbn}/`)
}

// export async function getdbbook(isbn: any, bookinfo: any): Promise<any> {
//   console.log(isbn)
//   const data = toRaw(isbn)
//   console.log({ book: api.get(`book/${isbn}/`), pra: bookinfo })
//   return { book: api.get(`book/${isbn}/`), pra: bookinfo }
// }
// export async function getdbbook(isbn: any, bookinfo: any): Promise<any> {
//   console.log(isbn)
//   const data = toRaw(isbn)
//   console.log("api里先",bookinfo)
//   const bookData = await api.get(`book/${isbn}/`).then((response) => response.data)
//   console.log({ book: bookData, pra: bookinfo })
//   console.log("api里后",{ book: bookData, pra: bookinfo })
//   return { book: bookData, pra: bookinfo }
// }

// export async function getdbbook(isbn: any, bookinfo: any, sta: any): Promise<any> {
//   console.log(isbn)
//   console.log(bookinfo)
//   const data1 = toRaw(bookinfo)
//   console.log(data1)
//   try {
//     const response = await api.get(`book/${isbn}/`)
//     if ((!response.data.status) && (sta)) {
//       console.log('post嗷嗷嗷')
//       console.log(response.data.status && (sta))
//       console.log(data1)
//       await postbooktobook(data1)
//       return response
//     } else {
//       console.log('没post嗷嗷')
//       console.log(response.data.status && sta)
//
//       return response
//     }
//     // 如果获取到了数据，直接返回
//   } catch (error) {
//     // 如果没有获取到数据，则调用postbooktobook函数进行添加新书的操作
//     const response = await postbooktobook(bookinfo)
//     return response
//   }
// }
// export async function getdbbook(isbn: any, bookinfo: any, sta: any): Promise<any> {
//   console.log(isbn)
//   console.log(bookinfo)
//   const data1 = toRaw(bookinfo)
//   console.log(data1)
//   try {
//     const response = await api.get(`book/${isbn}/`)
//     console.log('Data in try:', data1) // 在try中输出data1里的数据
//     console.log(bookinfo)
//
//     if (!response.data.status && sta) {
//       console.log('post嗷嗷嗷')
//       console.log(response.data.status && sta)
//       console.log(data1)
//       postbooktobook(data1)
//       return response
//     } else {
//       console.log('没post嗷嗷')
//       console.log(response.data.status && sta)
//
//       return response
//     }
//   } catch (error) {
//     console.log('Data in catch:', data1) // 在catch中输出data1里的数据
//     console.log(bookinfo)
//
//     postbooktobook(bookinfo)
//     const response = await api.get(`book/${isbn}/`)
//
//     return response
//   }
// }
// export async function getdbbook(isbn: any, bookinfo: any, sta: any, sta2 :any): Promise<any> {
//   console.log(isbn)
//   console.log(bookinfo)
//   const data1 = toRaw(bookinfo)
//   console.log(data1)
//   console.log('Data in try:', data1) // 在try中输出data1里的数据
//   console.log(bookinfo)
//   if (sta&&sta2) {
//     console.log('post嗷嗷嗷')
//     console.log(data1)
//     await postbooktobook(data1)
//     return api.get(`book/${isbn}/`)
//   } else {
//     console.log('没post嗷嗷')
//
//     return api.get(`book/${isbn}/`)
//   }
// }

export async function getdballbook(): Promise<any> {
  return api.get('book/')
}

export async function postbooktobook(info: any): Promise<any> {
  return api.post('book/', info)
}
export async function putbooktobook(isbn: any, info: any): Promise<any> {
  return api.put(`book/${isbn}/`, info)
}

export function getoutbook(isbn: string): Promise<any> {
  console.log('获取外部', isbn)
  return outApi.get(`isbn?isbn=${isbn}&uKey=33b4c461da6946eca5c7fae235c5da9e`)
  // .then((response) => {
  //   const bookInfo: BookInfo = response.data
  //   console.log('haole')
  //   return bookInfo
  // })
}

export function getBookIsFlow(): Promise<any> {
  return api.get('bookisflow')
}
