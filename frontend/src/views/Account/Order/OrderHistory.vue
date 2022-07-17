<template>
    <div >
        <div class="main-cont-order">
        <div class="title-container-order">
        <div class="title-cointainer-bottom">
            <h3 class="title-name">Name</h3> 
            <div class="title-qty">Qty</div>
            <h3 class="title-price">Price</h3>
            <h3 class="title-change">Order-Type</h3>
        </div> 
        <div class="seperator"></div>
                <div class="main-content-data">
            <ul>
                <li class="box order_history content-wrapper" v-for="i in order_history" :key="i.id">
                    <div class="coin-id">{{i.id}}</div>
                    <div class="coin-name">{{i.coin_name}}</div> 
                    <div class="coin-qty">{{i.order_qty}}</div>
                    <div class="coin-price">{{i.order_price}}</div>
                    <div class="order-type">{{i.order_type}}</div>
                </li>
            </ul>
        </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import {ref} from 'vue'
import axios from 'axios'
let order_history=ref([])

axios.get('/api/v1/getorder/')
.then(res=>{
    order_history.value=res.data
})
</script>

<style scoped>
.order_history{
    display: flex;
}
.content-wrapper :nth-child(1){
    width: 20px;
}
.content-wrapper :nth-child(2){
  width: 100px;
}
.content-wrapper :nth-child(3){
  width: 100px;
}
.content-wrapper :nth-child(4){
  width: 500px;
}
.title-cointainer-bottom{
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  font-size: large;
}
.title-name{
  margin-left: 3px;
}
.title-price{
  margin-left: 13%;
}
.title-change{
  margin-left: 20%;
}
.title-qty{
    margin-left: 5%;
}
.seperator{
    border: 1px solid black;
}
</style>