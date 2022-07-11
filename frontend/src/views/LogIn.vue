<template>
    <section class="hero is-primary is-fullheight">
  <div class="hero-body">
    <div class="container">
      <div class="columns is-centered">
        <div class="column is-5-tablet is-4-desktop is-3-widescreen">

          <form action="" class="box" v-on:submit.prevent="submitForm">

            <div class="field">
              <label for="" class="label">Email</label>
              <div class="control has-icons-left">
                <input type="email" v-model="username" placeholder="e.g. bobsmith@gmail.com" class="input" required>
                <span class="icon is-small is-left">
                  <i class="fa fa-envelope"></i>
                </span>
              </div>
            </div>

            <div class="field">
              <label for="" class="label">Password</label>
              <div class="control has-icons-left">
                <input type="password" placeholder="*******" v-model="password" class="input" required>
                <span class="icon is-small is-left">
                  <i class="fa fa-lock"></i>
                </span>
              </div>
            </div>

            <div class="field">
              <button class="button is-success">
               Login 
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</section>
</template>

<script setup>
import {ref} from 'vue'
import axios from 'axios'
import {useAuthStore} from '@/stores/Auth.js'
import {useRouter} from 'vue-router'

const main=useAuthStore()
const router=useRouter()
let username=ref('')
let password=ref('')

axios.defaults.headers.common['Authorization']=''
localStorage.removeItem('token')

const submitForm=()=>{
  if(username.value==''){
    alert('enter username')
  }
  else if(password.value==""){
    alert('enter password')
  }
 else{
    let formdata={
      username:username.value,
      password:password.value
    }

    axios.post('/api/v1/token/login',formdata)
    .then(res=>{

      const token=res.data.auth_token
      main.setToken(token)

      axios.defaults.headers.common['Authorization']="Token "+token
      localStorage.setItem('token',token)
      router.push('/')     

    }).catch(err=>{
      console.log(err)
    })
  }
}
</script>