<template>
<section class="main-container-market">
  <div class="top-market">
    <div class="market-1">
      <h2 class="market-1-txt placeholder-txt">Top Gainer</h2>
   </div>

    <div class="market-2">
      <h2 class="market-2-txt placeholder-txt">Larg Volume</h2>
      <ul class="names-container-1">
        <li class="list-name-1">BTC <div class="list-coin-name">1900</div>   </li>
        <li class="list-name-1">ETH  <div class="list-coin-name">{{price_usd}}</div></li>
        <li class="list-name-1">BNB <div class="list-coin-name">500</div></li>
      </ul>
    </div>

    <div class="market-3">
     <h2 class="market-3-txt placeholder-txt">Highlight coin</h2> 
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
  height: 100vh;
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
  width: 300px;
  height: 215px;
  margin-top: var(--topmargin);
  margin: 21px;
  margin-top: 60px;
}
.market-1{
 background-color: blue;
}
.market-2{
 background-color: yellow;
}
.market-3{
 background-color: brown;
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

<script setup>
import {ref} from 'vue'

let price_usd=ref(0)
  fetch('https://data.messari.io/api/v1/assets/eth/metrics')
 .then(res=>res.json())
  .then(data=>{
    price_usd.value=data.data.market_data.price_usd
  })

</script>

