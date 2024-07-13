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
        <div class="actions">
          <button class="edit-button" @click="editMovie(item)">Edit</button>
          <button class="delete-button" @click="deleteMovie(item.id)">Delete</button>
        </div>
      </div>
    </div>
  </div>
  <div v-if="selectedMovie" class="modal">
    <div class="modal-content">
      <h2>Edit Movie</h2>
      <form @submit.prevent="updateMovie">
        <label for="name">Name:</label>
        <input v-model="selectedMovie.name" id="name" type="text" />
        
        <label for="genres">Genres (comma separated):</label>
        <input v-model="selectedMovie.genres" id="genres" type="text" />

        <label for="description">Description:</label>
        <textarea v-model="selectedMovie.description" id="description"></textarea>

        <label for="rating">Rating:</label>
        <input v-model="selectedMovie.rating" id="rating" type="number" min="1" max="5" />

        <div class="modal-actions">
          <button type="submit" class="save-button">Save</button>
          <button type="button" class="cancel-button" @click="selectedMovie = null">Cancel</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const items = ref([]);
const selectedMovie = ref(null);

onMounted(() => {
  fetchMovies();
});

const fetchMovies = () => {
  axios.get('http://localhost:8000/api/peliculas/')
    .then(response => {
      items.value = response.data.map(movie => {
        if (typeof movie.genres === 'string') {
          movie.genres = movie.genres.split(','); // Divide la cadena en una lista
        }
        return movie;
      });
    })
    .catch(error => {
      console.error('Error fetching movies:', error);
    });
};

const deleteMovie = (id) => {
  axios.delete(`http://localhost:8000/api/peliculas/${id}/`)
    .then(() => {
      fetchMovies();
    })
    .catch(error => {
      console.error('Error deleting movie:', error);
    });
};

const editMovie = (movie) => {
  selectedMovie.value = { ...movie }; // Make a copy of the movie object
};

const updateMovie = () => {
  axios.put(`http://localhost:8000/api/peliculas/${selectedMovie.value.id}/`, selectedMovie.value)
    .then(() => {
      selectedMovie.value = null;
      fetchMovies();
    })
    .catch(error => {
      console.error('Error updating movie:', error);
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

.actions {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
}

.edit-button, .delete-button {
  padding: 8px 12px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 0.9em;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}

.edit-button {
  background-color: #ff9800;
  color: white;
}

.delete-button {
  background-color: #f44336;
  color: white;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background: rgba(0, 0, 0, 0.7);
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 10px;
  width: 400px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.modal-actions {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

.save-button, .cancel-button {
  padding: 10px 15px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1em;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}

.save-button {
  background-color: #4caf50;
  color: white;
}

.cancel-button {
  background-color: #9e9e9e;
  color: white;
}
</style>
