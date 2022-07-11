<template>
    <section class="hero is-primary is-fullheight">
  <div class="hero-body">
    <div class="container">
      <div class="columns is-centered">
        <div class="column is-5-tablet is-4-desktop is-3-widescreen">

          <form action="" class="box" v-on:submit.prevent="submitForm">

            <div class="field">
              <label  class="label">Email</label>
              <div class="control has-icons-left">
                <input type="email" v-model="username" placeholder="e.g. bobsmith@gmail.com" class="input" required>
                <span class="icon is-small is-left">
                  <i class="fa fa-envelope"></i>
                </span>
              </div>
            </div>

            <div class="field">
              <label  class="label">Password</label>
              <div class="control has-icons-left">
                <input type="password" v-model="password" placeholder="*******" class="input" required>
                <span class="icon is-small is-left">
                  <i class="fa fa-lock"></i>
                </span>
              </div>
            </div>

            <div class="field">
              <label class="label"> Confirm Password</label>
              <div class="control has-icons-left">
                <input type="password"   v-model="password2" placeholder="*******" class="input" required>
                <span class="icon is-small is-left">
                  <i class="fa fa-lock"></i>
                </span>
              </div>
            </div>

            <div class="field">
              <button class="button is-success">
               Sign up 
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

let username=ref('')
let password=ref('')
let password2=ref('')

const submitForm=()=>{
  if(username.value==''){
    alert('enter username')
  }
  else if(password.value=='' || password.value!=password2.value){
    alert('enter password or password do not match') 
  }
  else{
    let formdata={
      username:username.value,
      password:password.value
    }

    axios.post('/api/v1/users/',formdata).then(res=>{
      this.$router.push('/login')
    }).catch(err=>{
      console.log(err)
    })
  }
}
</script>