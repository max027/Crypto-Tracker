<script setup>
import {ref} from 'vue'

let content=ref([])
let temp

async function fetchData() {
 await fetch('https://data.messari.io/api/v1/assets?fields=id,slug,symbol,metrics/market_data/price_usd,metrics/market_data/volume_last_24_hours,metrics/market_data/percent_change_btc_last_24_hours')

 .then(res=>res.json())
  .then(data=>{
    temp=data.data
    for (let i = 0; i <10; i++) {
      content.value.push({id:i,name:temp[i].slug,value:temp[i].metrics.market_data.price_usd,volume:temp[i].metrics.market_data.volume_last_24_hours,change:temp[i].metrics.market_data.percent_change_btc_last_24_hours}) 
    }
    console.log(temp)
  }
  )
}

fetchData()
  
</script>

<template>
<section class="main-cointainer-bottom">
 <div class="title-cointainer-bottom">
  <h3 class="title-name">Name</h3> 
  <h3 class="title-price">Price</h3>
  <h3 class="title-volume">Volume</h3>
  <h3 class="title-change">Change</h3>
  </div> 
  <div class="seperator-bottom"/>
  <div class="main-content-data">
    <ul>
      <li v-for="i in content" :key="i.id" class="content-wrapper box">

        <div class="content-name">{{i.name}}</div>
        <div class="content-price">{{i.value}}</div>

        <div class="volume-coin">{{i.volume}}</div>
        <div class="change-coin">{{i.change}}</div>

        <div class="button is-primary">Buy</div>
        <div class="button is-danger btn-sell">Sell</div>
      </li>
    </ul>
  </div>
</section>
</template>

<style scoped>
@import "https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css";
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
  margin-left: 15%;
}
.title-volume{
  margin-left: 15%;
}
.title-change{
  margin-left: 15%;
}
.seperator-bottom{
  border: 1px solid rgb(150, 138, 138);
}
ul{
  position: relative;
  box-sizing: border-box;
}
li :nth-child(1){
width: 200px;
}

.content-wrapper{
  display: flex;
}
.content-wrapper :nth-child(2){
  width: 300px;
}
.content-wrapper :nth-child(3){
  width: 300px;
}
.content-wrapper :nth-child(4){
  width: 200px;
}
.btn-sell{
  margin-left: 5px;
}
</style>