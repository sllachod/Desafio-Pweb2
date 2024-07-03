<template>
    <div>
      <h1 class="text-2xl font-bold mb-4">Movie List</h1>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <div v-for="movie in movies" :key="movie.id" class="border p-4 rounded shadow">
          <img :src="movie.image" :alt="movie.name" class="w-full h-64 object-cover mb-4 rounded">
          <h2 class="text-xl font-semibold">{{ movie.name }}</h2>
          <p class="text-gray-700">{{ movie.description }}</p>
          <p class="text-gray-600"><strong>Rating:</strong> {{ movie.rating }}</p>
          <p class="text-gray-600"><strong>Genres:</strong> {{ movie.genres.join(', ') }}</p>
          <p class="text-gray-600"><strong>In Theaters:</strong> {{ movie.inTheaters ? 'Yes' : 'No' }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        movies: []
      };
    },
    created() {
      this.fetchMovies();
    },
    methods: {
      async fetchMovies() {
        try {
          const response = await fetch('/movies.json');
          const data = await response.json();
          this.movies = data.items;
        } catch (error) {
          console.error('Error fetching movies:', error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  /* Aquí puedes agregar estilos específicos para este componente si es necesario */
  </style>
  