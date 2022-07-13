<template>
    <div >
        <div class="main-cont-order">
        <div class="title-container-order">
            <div class="title-name-order">
                Name
            </div>
            <div class="title-ordertype-order">
                Order Type
            </div>
            <div class="title-price-order">
                Price
            </div>
            <div class="title-date-order">
                Date
            </div>
            <div class="title-qty-order">
                qty
            </div>
        </div>

        <h1>price:{{order_history}}</h1>
        </div>
    </div>
</template>

<script setup>
import {ref} from 'vue'
let order_history=ref([])
fetch('http://127.0.0.1:8000/api/v1/orderhistory').then(res=>res.json()).then(data=>{
    
})
</script>

<style>
.main-cont-order{
    width: 100vw;
    height: 70px;
    background-color: #cccccc;
}
</style>