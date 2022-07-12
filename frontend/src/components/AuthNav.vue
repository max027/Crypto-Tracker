<template>
<nav class="navbar" role="navigation" aria-label="main navigation">
  <div class="navbar-brand">
    <router-link to="/my-account" class="navbar-item">Crypto Tracker</router-link>
    </div>

    <div class="navbar-item">
      <router-link to="/portfolio">Portfolio</router-link>
      <router-link to="/market" class="market">Market</router-link>
      <router-link to="/order">Order history</router-link>
    </div>
    <div class="navbar-end">
      <div class="navbar-item">
        <div class="buttons">
            <button class="button is-danger">Log out</button>
        </div>
      </div>
    </div>
</nav>
</template>


<style >
.market{
  margin: 9px;
}
</style>