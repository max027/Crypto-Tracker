<template>
  <div class="main-container-order box">
   <h1 class="title-text-order">BTC</h1> 
    <div class="content-data-order ">
      <div class="content-container-1">
        
      <ul>
        <li>
          <div class="content-data1 coin_name">price</div>
          <div class="content-data2 coin_name">Volume</div>
          <div class="content-data3 coin_name">marketcap</div>
        </li>
       
      </ul>
      </div>

      <div class="content-container-2">
      <ul>
        <li>
          <div class="content-data1 coin_name">{{coin_data.current_price}}</div>
          <div class="content-data2 coin_name">{{coin_data.volume}}</div>
          <div class="content-data3 coin_name">{{coin_data.market_cap}}</div>
        </li>
      </ul>
      </div>

      <div class="content-container-3">
        
      <ul>
        <li>
          <div class="content-data1 coin_name">change</div>
          <div class="content-data2 coin_name">all time high</div>
          <div class="content-data3 coin_name">all time low</div>
        </li>
       
      </ul>
      </div>

 
      <div class="content-container-2">
      <ul>
        <li>
          <div class="content-data1 coin_name">{{coin_data.percentage_change}}</div>
          <div class="content-data2 coin_name">{{coin_data.alltime_high}}</div>
          <div class="content-data3 coin_name">{{coin_data.alltime_low}}</div>
        </li>
      </ul>
      </div>

      <div class="content-container-3">
        
      <ul>
        <li>
          <div class="content-data1 coin_name">Circulation</div>
          <div class="content-data2 coin_name">all time high</div>
          <div class="content-data3 coin_name">all time low</div>
        </li>
       
      </ul>
      </div>
      <div class="content-container-2">
      <ul>
        <li>
          <div class="content-data1 coin_name">{{coin_data.circulating_supply}}</div>
          <div class="content-data2 coin_name">9000</div>
          <div class="content-data3 coin_name">2999</div>
        </li>
      </ul>
      </div>




    </div>
  </div>
</template>

<script setup>
import {reactive} from 'vue'

let props = defineProps({ coin_name: String });
let assetKey=props.coin_name

let coin_data=reactive({
  current_price:0,
  market_cap:0,
 volume:0,
 circulating_supply:0,
 alltime_high:0,
 alltime_low:0,
 percentage_change:0
})

const fetch_coin= async()=>{
 await  fetch(`https://data.messari.io/api/v1/assets/${assetKey}/metrics`)
  .then(res=>res.json())
  .then(data=>{
    coin_data.current_price=data.data.market_data.price_usd
    coin_data.market_cap=data.data.marketcap.marketcap_dominance_percent
    coin_data.volume=data.data.market_data.volume_last_24_hours
    coin_data.circulating_supply=data.data.supply.circulating
    coin_data.alltime_high=data.data.all_time_high.price
    coin_data.percentage_change=data.data.market_data.percent_change_btc_last_24_hours
    coin_data.alltime_low=data.data.cycle_low.price

  })
}
fetch_coin()

</script>
<style scoped>

*{
  margin: 0;
  padding: 0;
}
.main-container-order{
  width: 1400px;
  height: 500px;
  margin: 50px;  
}
.title-text-order{
  font-size: 30px;
  padding-left: 50px;
  padding-top: 23px;
  margin-bottom: 9px;
}

.content-data-order{
  width: 95%;
  height: 390px;
  border: 1px solid grey;
  margin-left:43px;
  display: flex;
}
.content-container-1{
  width: 120px;
  height: 300px;
  margin: 10px;
}
.coin_name{
  font-size: 20px;
  padding: 30px;
}
.content-container-2{
  width: 300px;
  height: 300px;
  margin: 10px;
}
.content-container-3{
 width: 300px;
  height: 300px;
  margin: 10px;
} 
</style>