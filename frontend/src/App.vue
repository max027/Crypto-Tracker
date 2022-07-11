<script setup>
import Nav from '@/components/Nav.vue'
import { onMounted } from 'vue'
import {useAuthStore} from '@/stores/Auth.js'
import axios from 'axios'

const store=useAuthStore()

onMounted(() => {
store.initializeStore()
const token=store.token

if(token){

    axios.defaults.headers.common['Authorization']="Token "+token

}else{

    axios.defaults.headers.common['Authorization']=''
}
})


</script>

<template>
<div>
    <Nav/>
    <router-view/>
</div>
</template>

<style>
@import "https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css";
</style>