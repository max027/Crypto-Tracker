<script setup>
import {ref} from 'vue'

let content=ref([])
let temp

async function fetchData() {
 await fetch('https://data.messari.io/api/v1/assets?fields=id,slug,symbol,metrics/market_data/price_usd')
 .then(res=>res.json())
  .then(data=>{
    temp=data.data
    for (let i = 0; i <20; i++) {
      content.value.push({id:i,name:temp[i].slug,value:temp[i].metrics.market_data.price_usd}) 
    }
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
  </div> 
  <div class="seperator-bottom"/>
  <div class="main-content-data">
    <ul>
      <li v-for="i in content" :key="i.id" class="content-wrapper box">
        <div class="content-name">{{i.name}}</div>
        <div class="content-price">{{i.value}}</div>
      </li>
    </ul>
  </div>
</section>
</template>

<style scoped>
.title-cointainer-bottom{
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  font-size: large;
}
.title-name{
  margin-left: 3px;
  margin-right: 9px;
}
.seperator-bottom{
  border: 1px solid rgb(150, 138, 138);
}

.content-wrapper{
  display: flex;
  flex-direction: row;
  align-items: flex-start;
}
</style>

