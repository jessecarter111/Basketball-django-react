import { useEffect, useState } from 'react';
import { API_PLAYERS_URL, API_TEAMS_URL } from "../../constants"
import Header from "../Header/Header"
import TypeAhead from "../TypeAhead/TypeAhead"
import TeamData from "../TeamData/TeamData"
import PlayerData from "../PlayerData/PlayerData"
import styled from 'styled-components'

const App = () => {
    const [teamData, setTeamData] = useState([])
    const [playerData, setPlayerData] = useState([])
    const [selectedData, setSelectedData] = useState({})
    const [isDataTableVisible, setIsDataTableVisible] = useState(false)

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

    const displayData = () => {
        switch(selectedData.model_type) {
            case "player":
                return (<PlayerData player={ selectedData }/>)
                
            case "team":
                return (<TeamData team={ selectedData }/>)

            default:
                return
        }     
    }
    
    const toggleIsDataTableVisible = ( truthy ) => {
        setIsDataTableVisible(truthy)
    }

    return (
        <div className="main">
            <Header/>
            <TypeAhead TeamData={ teamData }
                PlayerData={ playerData }
                handleSelect={ suggestion => { 
                   setSelectedData(suggestion)}
                }
                toggleIsDataTableVisible={ toggleIsDataTableVisible }
            />
            {selectedData && isDataTableVisible && (
                displayData()
            )}
        </div>
    )
}

export default App;