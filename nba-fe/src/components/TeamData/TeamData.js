import React, { useState } from 'react'
import { Table } from 'reactstrap'

const TeamData = (props) => {
    const teams = props.teams
    return (
        <Table dark>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Year</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                {!teams || teams.length <= 0 
                ? ( <tr> 
                        <td colSpan="6" align="center">
                            <b>Oops, no data here yet!</b>
                        </td>
                    </tr> 
                ) : ( 
                    teams.map(team => (
                        <tr key={team.team_name}>
                            <td>{team.team_abrev}</td>
                            <td>{team.league}</td>
                            <td>{team.inaug}</td>
                            <td>{team.end}</td>
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
                    )
                )
                }
            </tbody>
        </Table>
    )
}

