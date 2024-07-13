<script setup>
import { items } from "./movies.json";
/*
 This is an Icon that you can use to represent the stars if you like
 otherwise you could just use a simple ⭐️ emoji, or * character.
*/
//import { StarIcon } from "@heroicons/vue/24/solid";
</script>

<template>
  <div class="container">
    <div v-for="item in items" :key="item.id" class="movie">
      <img :src="item.image" :alt="item.name" class="movie-image">
      <div class="content">
        <h2 class="title">{{ item.name }}</h2>
        <div class="genres">
          <span v-for="genre in item.genres" :key="genre" class="genre">{{ genre }}</span>
        </div>
        <p class="description">{{ item.description }}</p>
        <div class="card-rating">
          <span>Rating: ({{ item.rating }}/5)</span>
          <span>{{ '⭐️'.repeat(item.rating) }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';

const items = ref([]);

onMounted(() => {
  fetchMovies();
});

const fetchMovies = () => {
  axios.get('http://localhost:8000/api/peliculas/')
    .then(response => {
      items.value = response.data;
    })
    .catch(error => {
      console.error('Error fetching movies:', error);
    });
};
</script>
<style scoped>
body {
  background-color: #351c75;
  color: #211e7d;
  font-family: Arial, sans-serif;
}

.container {
  background-color: #050515;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
  padding: 20px;
}

.movie {
  background-color: #ffffff;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  overflow: hidden;
  width: 300px;
  margin-bottom: 20px;
  color: #351c75;
  display: grid;
  grid-template-rows: auto 1fr auto; /* Define the layout: image, flexible description, rating */
}

.movie-image {
  width: 100%;
  height: 450px;
  object-fit: cover;
}

.content {
  padding: 15px;
  display: flex;
  flex-direction: column;
}

.title {
  font-size: 1.2em;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  margin: 10px 0;
}

.genres {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
  margin-bottom: 10px;
}

.genre {
  background-color: #6129ba;
  color: #ffffff;
  border-radius: 5px;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  padding: 2px 8px;
  font-size: 0.8em;
}

.description {
  font-size: 0.9em;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  margin-bottom: 15px;
  flex-grow: 1; /* Make the description take available space */
}

.rating {
  display: flex;
  justify-content: space-between;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  align-items: center;
  font-size: 1em;
}
</style>
