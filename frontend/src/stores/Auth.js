import { defineStore } from "pinia";

export const useAuthStore=defineStore({
    id:'Auth',
    state:()=>{
        isAuthenticated:false
        token:''
    },

})