import { useEffect, useState } from 'react';
import { API_PLAYERS_URL, API_TEAMS_URL } from "../../constants"
import Header from "../Header/Header"
import SearchBar from "../SearchBar/SearchBar"
import TypeAhead from "../TypeAhead/TypeAhead"

const App = () => {
    const [searchTerm, setSearchTerm] = useState('')
    const [searchResults, setSearchResults] = useState([])
    const [teamData, setTeamData] = useState([])
    const [playerData, setPlayerData] = useState([])

    useEffect(() => {
        getTeams()
        getPlayers()
    }, [])

    const getTeams = async () => {
        const response = await fetch(API_TEAMS_URL)
        const data = await response.json()
        setTeamData(data)
    }

    const getPlayers = async () => {
        const response = await fetch(API_PLAYERS_URL)
        const data = await response.json()
        setPlayerData(data)
    }

    return (
        <div>
            <Header/>
            <TypeAhead TeamData={teamData}
                PlayerData={playerData}
                handleSelect={ suggestion => { window.alert(suggestion) }}/>
        </div>
    )
}

export default App;