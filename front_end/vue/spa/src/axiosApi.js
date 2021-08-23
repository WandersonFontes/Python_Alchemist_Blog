import axios from 'axios'

const blogApi = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/v1/homologation',
    timeout: 1000,
})

export{ blogApi }
