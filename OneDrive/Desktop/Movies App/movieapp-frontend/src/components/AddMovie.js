import React, { useState } from 'react';
import axios from 'axios';

function AddMovie() {
  const [tmdbId, setTmdbId] = useState('');
  const [rank, setRank] = useState(0);

  const handleSubmit = (event) => {
    event.preventDefault();
    axios.post('http://localhost:8000/api/add/movie/', { tmdb_id: tmdbId, rank })
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  };

  return (
    <div>
      <h2>Add Movie</h2>
      <form onSubmit={handleSubmit}>
        <label>
          TMDb ID:
          <input type="text" value={tmdbId} onChange={(event) => setTmdbId(event.target.value)} />
        </label>
        <br/>
        <label>
          Rank:
          <input type="number" value={rank} onChange={(event) => setRank(event.target.value)} />
        </label>
        <br />
        <button type="submit">Add Movie</button>
      </form>
    </div>
  );
}

export default AddMovie;