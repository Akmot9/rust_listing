<template>
  <div class="intro">
    <h1 class="intro-title">Introduction</h1>
    <p class="intro-text">We want to list all the files on a computer and write them to a file.</p>
    <p class="intro-text">Several acceptance criteria are required:</p>
    <ul class="intro-list">
      <li class="intro-list-item">Listing time</li>
      <li class="intro-list-item">Number of listed files</li>
      <li class="intro-list-item">Types of listed files</li>
    </ul>
  </div>
</template>

<style>
.intro {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: #000000;
  border-radius: 10px;
  text-align: center;
  color: #ffffff;
}

.intro-title {
  font-size: 24px;
  margin-bottom: 10px;
}

.intro-text {
  font-size: 16px;
  margin-bottom: 10px;
}

.intro-list {
  list-style-type: disc;
  text-align: left;
  margin-left: 20px;
}

.intro-list-item {
  margin-bottom: 5px;
}

.intro-list-item::before {
  content: '•';
  color: #e95420;
  font-weight: bold;
  display: inline-block;
  width: 1em;
  margin-left: -1em;
}
</style>
