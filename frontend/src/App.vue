<script setup>
import Nav from '@/components/Nav.vue'
import AuthNav from '@/components/AuthNav.vue'
import { onMounted, ref } from 'vue'
import {useAuthStore} from '@/stores/Auth.js'
import axios from 'axios'

const store=useAuthStore()
let auth=ref(false)

onMounted(() => {
store.initializeStore()
const token=store.token

if(token){
    auth.value=store.isAuthenticated
    axios.defaults.headers.common['Authorization']="Token "+token

}else{

    axios.defaults.headers.common['Authorization']=''
}
})


</script>

<template>
<div>
    <div v-if="auth" >
        <AuthNav/>
    </div>

    <div v-else>
    <Nav/>
    </div>
    <router-view/>
</div>
</template>

<style>
@import "https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css";
</style>