import axios from "axios";
import Cookies from "js-cookie"

export default axios.create({
    baseURL: 'https://api.ibook.tech/v1/book',
    timeout: 5000,
    headers: {
        'Content-Type': 'application/json',
        // 'X-CSRFToken': Cookies.get('csrftoken'),
        // 'Access-Control-Allow-Origin' : "*",
        // 'Access-Control-Allow-Methods' : "GET, POST, PATCH, PUT, DELETE, OPTIONS",
        // 'Access-Control-Allow-Headers' : "Origin, X-Requested-With, Content-Type, Accept, X-Auth-Token, access-control-allow-origin, Authorization",
        // 'Access-Control-Allow-Credentials' : "true",
    },
    // devServer: {
    //     proxy: {
    //         '/api': {
    //             target: 'http://localhost:8000',
    //             changeOrigin: true,
    //             pathRewrite: {
    //                 '/api': ''
    //             }
    //         }
    //     }
    // }

})
