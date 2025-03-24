import axios from "axios";
import Cookies from "js-cookie"

const api = axios.create({
    baseURL: 'http://localhost:8000/api',
    timeout: 50000,
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': Cookies.get('csrftoken'),
    }
})

api.interceptors.request.use(function (config) {
    if (!window.sessionStorage.getItem('token'))
        return config
    config.headers['Authorization'] = "Token " + window.sessionStorage.getItem('token')
    return config
})

export default api
