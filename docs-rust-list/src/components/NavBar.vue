<template>
  <div class="navbar">
    <div class="logo">
      <img alt="Vue logo" class="logo-image" src="@/assets/Rust 1.svg" width="50" height="50" />
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
export default {
  // Component logic goes here
}
</script>

<style>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background-color: #f0f0f0;
}

.logo {
  color: black; /* Style your logo here */
}

.logo-image {
  vertical-align: middle;
}

.links {
  color: black; /* Style your links here */
}

.nav-link {
  margin-left: 10px;
}

.github-link {
  color: black; /* Style your GitHub link here */
}

.github-link-text {
  text-decoration: none;
  font-weight: bold;
}
</style>
