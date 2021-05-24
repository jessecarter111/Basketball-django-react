import { Table } from 'reactstrap'
import styled from 'styled-components'
//TODO: Add age calculator, send full record of player games
const PlayerData = ({ player }) => {
    return (
        <Container>
            <Table dark hover responsive>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Position</th>
                        <th>Age</th>
                        <th>Team</th>
                        <th>Games</th>
                        <th>Games Started</th>
                        <th>FG</th>
                        <th>FG%</th>
                        <th>3pts</th>
                        <th>3pts%</th>
                        <th>2pts</th>
                        <th>2pts%</th>
                        <th>eFG%</th>
                        <th>Points</th>
                        <th>Free Throws</th>
                        <th>Free Throw%</th>
                        <th>Off Reb</th>
                        <th>Def Reb</th>
                        <th>Total Reb</th>
                        <th>Assists</th>
                        <th>Steals</th>
                        <th>Blocks</th>
                        <th>Turnovers</th>
                        <th>Pers Fouls</th>
                    </tr>
                </thead>
                <tbody>
                    {!player
                    ? ( <tr> 
                            <td colSpan="6" align="center">
                                <b>Oops, no data here yet!</b>
                            </td>
                        </tr> 
                    ) : ( 
                        <tr key={player.team_name}>
                            <td>{player.player_name}</td>
                            <td>{player.position}</td>
                            <td>{player.age}</td>
                            <td>{player.team}</td>
                            <td>{player.games}</td>
                            <td>{player.games_started}</td>
                            <td>{player.field_goals}</td>
                            <td>{player.field_goals_pct}</td>
                            <td>{player.three_pts}</td>
                            <td>{player.three_pts_pct}</td>
                            <td>{player.two_pts}</td>
                            <td>{player.two_pts_pct}</td>
                            <td>{player.effective_fg_pct}</td>
                            <td>{player.points}</td>
                            <td>{player.free_throws}</td>
                            <td>{player.free_throws_pct}</td>
                            <td>{player.off_reb}</td>
                            <td>{player.def_reb}</td>
                            <td>{player.total_reb}</td>
                            <td>{player.assists}</td>
                            <td>{player.steals}</td>
                            <td>{player.blocks}</td>
                            <td>{player.turnovers}</td>
                            <td>{player.pers_fouls}</td>
                        </tr>)
                    }
                </tbody>
            </Table>
        </Container>
    )
}

const Container = styled.div`
    display: flex;
    margin: 1% 5%;
    text-align: center;
    justify-content: center;
`;

export default PlayerData