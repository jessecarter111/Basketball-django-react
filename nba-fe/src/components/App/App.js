import { useEffect, useState } from 'react';
import { API_PLAYERS_URL, API_TEAMS_URL } from "../../constants"
import Header from "../Header/Header"
import TypeAhead from "../TypeAhead/TypeAhead"
import TeamData from "../TeamData/TeamData"

const App = () => {
    const [teamData, setTeamData] = useState([])
    const [playerData, setPlayerData] = useState([])
    const [selectedData, setSelectedData] = useState({})
    const [isDataVisible, setIsDataVisible] = useState(false)

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

    const display_data = () => {
        return selectedData.model_type === 'team'
        ?  (<TeamData team={ selectedData }/>)
        : (<></>)    
    }
    
    const is_data_visible = ( truthy ) => {
        setIsDataVisible(truthy)
    }

    return (
        <div>
            <Header/>
            <TypeAhead TeamData={ teamData }
                PlayerData={ playerData }
                handleSelect={ suggestion => { 
                   setSelectedData(suggestion)}
                }
                is_data_visible={is_data_visible}
            />
            {selectedData && isDataVisible && (
                display_data()
            )}
        </div>
    )
}

export default App;