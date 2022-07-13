<script setup>
import {ref} from 'vue'

let large_volume=ref([])
let top=ref([])
let Highlight=ref([])
let price_usd

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min) + min); 
}

async function getData() {
  
 await fetch('https://data.messari.io/api/v1/assets?fields=id,slug,symbol,metrics/market_data/price_usd')
 .then(res=>res.json())
  .then(data=>{
    price_usd=data.data
    for(let i=0;i<3;i++){
      large_volume.value.push(price_usd[i].metrics.market_data.price_usd)
    }

    for (let i = 0; i < 3; i++) {
      let temp=getRandomInt(4,19)
      top.value.push({id:i,name:price_usd[temp].slug,value:price_usd[temp].metrics.market_data.price_usd})
    }

    for (let i = 0; i < 3; i++) {
      let temp=getRandomInt(4,19)
      let price=price_usd[temp].metrics.market_data.price_usd
      Highlight.value.push({id:i,name:price_usd[temp].slug,value:price_usd[temp].metrics.market_data.price_usd})
    }
  })
}

getData()
</script>

<template>
<section class="main-container-market">
  <div class="top-market">
    <div class="market-1 box">
      <h2 class="market-1-txt placeholder-txt">Top Gainer</h2>
      <ul class="names-container-1">
        <li class="list-name-1" v-for="i in top" :key="i.id">
          {{i.name}} <div class="list-coin-name">{{i.value}}</div>
        </li>
      </ul>
   </div>

    <div class="market-2 box">
      <h2 class="market-2-txt placeholder-txt">Larg Volume</h2>
      <ul class="names-container-1">
        <li class="list-name-1">BTC <div class="list-coin-name"> {{large_volume[0]}}</div>   </li>
        <li class="list-name-1">ETH  <div class="list-coin-name">{{large_volume[1]}}</div></li>
        <li class="list-name-1">USDT<div class="list-coin-name">{{large_volume[2]}}</div></li>
      </ul>
    </div>

    <div class="market-3 box">
     <h2 class="market-3-txt placeholder-txt">Highlight coin</h2> 
     <div class="names-container-1">
      <li class="list-name-1" v-for="i in Highlight" :key="i.id">
        {{i.name}} <div class="list-coin-name">{{i.value}}</div>
      </li>
     </div>
    </div>
 </div>
</section>
</template>

<style scoped>
:root{
  --allview:100vw;
  --topmargin:50px;
}
*{
  margin: 0;
  padding: 0;
}
.main-container-market{
  width: var(--allview);
  height: 400px ;
}
.top-market{
  width: var(--allview);
  height: 335px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: flex-start;
}
.market-1,.market-2,.market-3{
  width: 370px;
  height: 270px;
  margin-top: var(--topmargin);
  margin-top: 60px;
}

.market-2{
 margin-left: 40px;
 margin-right: 40px;
}

.placeholder-txt{
  font-size: large;
}

.names-container-1{
  list-style-type: none;
  margin-top: 30px;
  margin-left: 7px;
  font-size: 1.3rem;
}
.list-name-1{
  padding: 10px;
  display:  flex;
  flex-direction: row;
  align-items: flex-start;
}
.list-coin-name{
  padding-left: 37px;
}
</style>


