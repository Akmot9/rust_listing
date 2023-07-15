<template>
  <div class="bg">
    <header class="navbar">
      <NavBar />
      <RightBar />
      <Sidebar />
    </header>

    <main class="main-content">
      <div class="sidebar-wrapper">
        
      </div>

      <div class="content-wrapper">
        <router-view></router-view>
      </div>
    </main>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue'
import Sidebar from './components/Sidebar.vue'
import RightBar from './components/RightBar.vue';
</script>

<style scoped>
/* Your existing styles for NavBar, Introduction, and Home views */

/* Additional styles for the sidebar */
.sidebar-wrapper {
  position: fixed;
  top: 50px; /* Adjust the top value to align the sidebar below the navbar */
  left: 0;
  bottom: 0;
  width: 200px;
  z-index: 1000; /* Increase the z-index to ensure the sidebar appears above the main content */
}

.main-content {
  padding-top: 50px; /* Add padding to the top of the main content area to prevent overlap with the navbar */
  display: flex;
}

.content-wrapper {
  flex: 1; /* Expand the content wrapper to fill the remaining width */
  padding: 20px;
  background-color:black;
}

.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 2000; /* Increase the z-index to ensure the navbar appears above the sidebar */
}
</style>
