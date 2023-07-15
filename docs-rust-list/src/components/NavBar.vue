<template>
  <div class="navbar">
    <div class="logo">
      <img alt="Rust logo" class="logo-image rotate" src="@/assets/Rust.svg" width="50" height="50" />
    </div>
    <div class="links">
      <router-link to="/" class="nav-link">Home</router-link>
      <router-link to="/intro" class="nav-link">Intro</router-link>
    </div>
    <div class="github-link">
      <a href="https://github.com/Akmot9" class="github-link-text">GitHub</a>
    </div>
  </div>
</template>

<script>

</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background-color: #2b2b2b;
  border-inline-width: 1px;
  border-color: #ffffff;
}

.logo {
  display: flex;
  align-items: center;
}

.logo-image {
  margin-right: 10px;
}

.rotate {
  animation: rotate 10s infinite linear;
}

.links {
  display: flex;
  gap: 10px;
  
}

.nav-link {
  text-decoration: none;
  color: #e95420;
  font-size: 16px;
  font: large;
}

.toggle-button {
  background: none;
  border: none;
  color: #ffffff;
  cursor: pointer;
  font-size: 14px;
}

.github-link-text {
  text-decoration: none;
  font-weight: bold;
  color: #ffffff;
}

.github-link-text:hover {
  text-decoration: underline;
}

@keyframes rotate {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
