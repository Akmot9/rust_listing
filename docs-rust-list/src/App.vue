<script setup>
import { RouterLink, RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue'
</script>

<template class="bg">
  <header>
    <NavBar />

  </header>

  <RouterView />
</template>

<style scoped>
.bg {
  background-color: black;
}
</style>
