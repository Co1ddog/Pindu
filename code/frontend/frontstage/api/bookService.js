import api from "./api";



// export async function getBookCondition(isbn) {
//     return api.get((`bookinfo/${isbn}/`))
// }

export async function postBookCart(info) {
    return api.post('bookinfo/', info)
}