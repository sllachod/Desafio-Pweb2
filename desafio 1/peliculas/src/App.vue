<script setup>
import { items } from "./movies.json";
/*
 This is an Icon that you can use to represent the stars if you like
 otherwise you could just use a simple ⭐️ emoji, or * character.
*/
// import { StarIcon } from "@heroicons/vue/24/solid";
</script>

<template>
  <!-- This is where your template goes	-->
  <div>
    <h1>Movie List</h1>
    <ul>
      <li v-for="movie in movies" :key="movie.title">
        {{ movie.title }} ({{ movie.year }})
      </li>
    </ul>
  </div>
</template>