<template>
<div class="sidebar">
  <div class="side-title">
    Account
  </div>
  <div class="side-contents">
   <div class="side-section">
    <div class="side-section-name">Section</div> 

    <button class="btn-1 btn">Dashboard</button>

    <button class="btn-2 btn">Market</button>
    <button class="btn-3 btn">Report</button>
    </div> 
  </div>
</div>
</template>

<style>
:root{
  --WIDTH:240px;
  --COLOR:#ffffff;
  --FONTSIZE:20px;
  --FONTHEIGHT:50px;
}
.sidebar{
  width: var(--WIDTH);
  height: 100vh;
}

.side-title{
  display: flex;
  justify-content: center;
  align-items: center;
  color: var(--COLOR);
  height:50px ;
  font-size: 30px;
  background-color: #0066ff ;
}

.side-contents{
width: var(--WIDTH);
height: 92%;
background-color: #3385ff;
}

.side-section{
  padding-top:40px ;
  width: var(--WIDTH);
  color: var(--COLOR);
  font-size: var(--FONTSIZE);
}
.side-section-name{
  padding-left: 12px;
}
.btn{
  width: var(--WIDTH);
  height:var(--FONTHEIGHT);
  background-color:#3385ff ;
  color: var(--COLOR);
  border: none;
  font-size: var(--FONTSIZE);
margin-top: 4px;
}

.btn-1{
  padding-right: 100px;
}

.btn-2{
  padding-right: 130px;
}

.btn-3{
  padding-right: 134px;
}

.btn:hover{
  background-color: #0066ff;
}
.image-1{
  width: 50px;
  height: 50px;
}
</style>


