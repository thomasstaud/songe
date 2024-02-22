<template>
  <header class="navbar bg-base-100">
    <router-link to="/" class="btn btn-ghost text-xl">HOME</router-link>
    <router-link to="/artists" class="btn btn-ghost text-xl">ARTISTS</router-link>
    <router-link to="/tracks" class="btn btn-ghost text-xl">TRACKS</router-link>
  </header>

  <main>
    <router-view></router-view>
  </main>
</template>
