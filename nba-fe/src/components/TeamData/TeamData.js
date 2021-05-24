import { Table } from 'reactstrap'
import styled from 'styled-components'

const TeamData = ({ team }) => {
    return (
        <Container>
            <Table dark hover responsive>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>League</th>
                        <th>Inaug. Season</th>
                        <th>Years</th>
                        <th>Games</th>
                        <th>Wins</th>
                        <th>Losses</th>
                        <th>Win/Loss%</th>
                        <th>Playoffs</th>
                        <th>Division</th>
                        <th>Conference</th>
                        <th>Titles</th>
                    </tr>
                </thead>
                <tbody>
                    {!team
                    ? ( <tr> 
                            <td colSpan="6" align="center">
                                <b>Oops, no data here yet!</b>
                            </td>
                        </tr> 
                    ) : ( 
                        <tr key={team.franchise_name}>
                            <td>{team.franchise_name}</td>
                            <td>{team.league}</td>
                            <td>{team.inaug}</td>
                            <td>{team.years}</td>
                            <td>{team.games}</td>
                            <td>{team.wins}</td>
                            <td>{team.losses}</td>
                            <td>{team.w_l_pct}</td>
                            <td>{team.playoffs}</td>
                            <td>{team.division}</td>
                            <td>{team.conference}</td>
                            <td>{team.championships}</td>
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

export default TeamData