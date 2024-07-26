import React from 'react';
import MovieList from './components/MovieList';
import MovieDetail from './components/MovieDetail';
import AddMovie from './components/AddMovie';

function App() {
  return (
    <div>
      <h1>Movie App</h1>
      <MovieList />
      <hr />
      <AddMovie />
    </div>
  );
}

export default App;