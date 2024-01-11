import React from 'react';

function search(player: String, start_game: String, end_game: String){
    fetch('http://localhost:4269/search?start_game='+start_game+'&end_game='+end_game+'&data='+player)

}


export function blah() {
    return (
        <div className="App">
        <header className="App-header">
            <p>
            Search
            </p>
        </header>
        </div>
    );
    }