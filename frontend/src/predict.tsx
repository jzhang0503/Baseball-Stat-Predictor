import React, { useEffect } from "react";
import { useState, Dispatch, SetStateAction } from "react";

function get_prediction(player: string, first_game: string, last_game: string) {


return fetch('http://localhost:6942/predict?player='+player+'&start_game='+first_game +'&end_game='+ last_game).then(r => r.json()).then(data => data.avg)

}

interface ControlledInputProps {
    value: string,
    set_value: Dispatch<SetStateAction<string>>
}

function ControlledInput({ value, set_value }: ControlledInputProps) {
    return (
        <input
            type="text"
            value={value}
            onChange={e => set_value(e.target.value)}
            aria-label="input Box"
        />
    );
}

interface InputProps {
    initial_value: (input: string) => any
}

function Input({ initial_value }: InputProps) {
    const [term, setTerm] = useState('')
    return (
        <div>
            <div>
                <ControlledInput value={term} set_value={setTerm} />
            </div>
            <div>
                <button onClick={() => initial_value(term)}>Predict</button>
            </div>
        </div>

    );
}


// export funtion that uses tha above to create a page with a search box and a button that returns the avg from the backend

export function Predict() {
    const [prediction, setPrediction] = useState(0)
    const [player, setPlayer] = useState('')
    const [first_game, setFirstGame] = useState('')
    const [last_game, setLastGame] = useState('')
    useEffect(() => {
        get_prediction(player, first_game, last_game).then(r => { setPrediction(r)})
    }, [player, first_game, last_game])
    return (
        <div>
            <div>
                <Input initial_value={setPlayer} />
                <Input initial_value={setFirstGame} />
                <Input initial_value={setLastGame} />
            </div>
            <div>
                <p>Prediction: {prediction}</p>
            </div>
        </div>
    );
}