<template>
  <main class="home">
    <div class="content">
      <img src="@/assets/Rust.svg" alt="Rust Logo" class="rust-logo" />
      <h1 class="title">Welcome to My Rust-themed Site</h1>
      <p class="description">Explore the power and elegance of Rust.</p>
      <router-link to="/intro" class="cta-button">Get Started</router-link>
    </div>
  </main>
</template>

<script setup>
// Component logic goes here
</script>

<style>
.home {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #000000;
  color: #ffffff;
}

.content {
  text-align: center;
}

.rust-logo {
  width: 200px;
  height: 200px;
  margin-bottom: 20px;
}

.title {
  font-size: 36px;
  margin-bottom: 20px;
}

.description {
  font-size: 18px;
  margin-bottom: 30px;
}

.cta-button {
  padding: 10px 20px;
  font-size: 16px;
  background-color: #e95420;
  color: #ffffff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
  position: relative;
  overflow: hidden;
  animation: pulsate 1.5s ease-in-out infinite;
  transition: background-color 0.3s ease-in-out;
}

.cta-button:hover {
  background-color: #c43c00;
}

@keyframes pulsate {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.05);
  }
  100% {
    transform: scale(1);
  }
}
</style>
