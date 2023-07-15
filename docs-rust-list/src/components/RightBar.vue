<template>
    <div class="sidebar">
      <div class="sidebar-content">
        <!-- Sidebar content goes here -->
        <h3 class="sidebar-heading">Table of Contents</h3>
        <ul class="sidebar-menu">
          <li><a href="#section-1">Section 1</a></li>
          <li><a href="#section-2">Section 2</a></li>
          <li><a href="#section-3">Section 3</a></li>
        </ul>
      </div>
    </div>
</template>

<style scoped>
.sidebar {
position: fixed;
top: 0;
right: 0; /* Adjusted to align the sidebar to the right */
bottom: 0;
width: 200px;
padding: 20px;
background-color: #392d2d;
color: #ffffff;
transition: transform 0.3s ease-in-out;
}

.sidebar-hidden {
transform: translateX(200px); /* Changed to positive value to hide the sidebar to the right */
}

.sidebar-content {
display: flex;
flex-direction: column;
}

.sidebar-heading {
font-size: 18px;
margin-bottom: 10px;
}

.sidebar-menu {
list-style-type: none;
padding: 0;
margin: 0;
}

.sidebar-menu li {
margin-bottom: 5px;
}

.sidebar-menu li a {
color: #ffffff;
text-decoration: none;
}

.sidebar-menu li a:hover {
text-decoration: underline;
}
</style>
  