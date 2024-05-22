<template>
    <nav class="navbar">
      <ul>
        <li>绝句</li>
        <li>风格绝句</li>
        <li>藏头诗</li>
        <li>集句诗</li>
        <li>律诗</li>
        <li>词</li>
        <li>对对子</li>
        <li>美文句搜索</li>
      </ul>
    </nav>
  </template>
  
  <script>
  export default {
    name: 'NavBar'
  }
  </script>
  
  <style>
  .navbar {
    background-color: #9c2e33;
    color: white;
    padding: 1rem;
  }
  .navbar ul {
    list-style-type: none;
    display: flex;
    justify-content: space-around;
  }
  .navbar li {
    cursor: pointer;
  }
  </style>
  