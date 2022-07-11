import { defineStore } from "pinia";

export const useAuthStore=defineStore({
    id:'Auth',
    state:()=>{
        isAuthenticated:false
        token:''
    },
   actions:{
        initializeStore(){
            if(localStorage.getItem('token')){
                this.token=localStorage.getItem('token')
                this.isAuthenticated=true
            }else{
                this.token='' 
                this.isAuthenticated=false
            }
        },
        setToken(token){
            this.token=token
            this.isAuthenticated=true
        } ,
        removeToken(){
            this.token=''
            this.isAuthenticated=false
        }
        
     } 
})