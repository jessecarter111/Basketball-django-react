import {useState} from "react"
import './TypeAhead.css'
import Suggestion from '../Suggestion/Suggestion'
import styled from 'styled-components'

const TypeAhead = ({TeamData, PlayerData, handleSelect, toggleIsDataTableVisible}) => {
    const [searchTerm, setSearchTerm] = useState('')
    const [isVisible, setIsVisible] = useState(false)
    const [selectedSuggestionIndex, setSelectedSuggestionIndex] = useState(0)

    //Sort through TeamData,PlayerData to determine searchterm matches if term length >= 2
    const rgx = new RegExp(searchTerm.toLowerCase(), "g")
    const hasEnteredEnoughCharacters = searchTerm.length >= 2;
    const teamSuggestions = TeamData.filter(team => {
        const matchesValue = team.franchise_name.toLowerCase().match(rgx);
        return hasEnteredEnoughCharacters && matchesValue;
    })
    console.log("TypeAhead: ")
    console.log(teamSuggestions)
    const playerSuggestions = PlayerData.filter(player => {
        const matchesValue = player.player_name.toLowerCase().match(rgx);
        return hasEnteredEnoughCharacters && matchesValue;
    }).slice(0, 8)
    
    const totalSuggestions = teamSuggestions.concat(playerSuggestions)
    const shouldShowSuggestions = totalSuggestions.length > 0 && isVisible
    const numSuggestions = totalSuggestions.length - 1

    const selectedSuggestion = totalSuggestions[selectedSuggestionIndex]
        
    return (
        <Wrapper>
                <Input
                    type='text'
                    value={searchTerm}
                    onChange={ev => {
                        setSearchTerm(ev.target.value);
                    }}
                    onFocus={() => {
                        setIsVisible(true)
                        toggleIsDataTableVisible(false)
                    }}
                    onKeyDown={ev => {
                        switch (ev.key) {
                            case 'Enter': {
                                handleSelect(selectedSuggestion);
                                return;
                            }

                            case 'Escape': {
                                setIsVisible(false);
                                return;
                            }

                            case 'ArrowUp':
                            case 'ArrowDown': {
                                ev.preventDefault()

                                if(!teamSuggestions && !playerSuggestions) {
                                    return
                                }

                                const direction = ev.key === 'ArrowDown' ? 'down' : 'up';

                                let nextSuggestionIndex = selectedSuggestionIndex;

                                nextSuggestionIndex = 
                                    direction === 'down'
                                    ? nextSuggestionIndex + 1
                                    : nextSuggestionIndex - 1
                                
                                if (nextSuggestionIndex < 0)
                                    nextSuggestionIndex = 0
                                else if (nextSuggestionIndex > numSuggestions)
                                    nextSuggestionIndex = numSuggestions
                                
                                setSelectedSuggestionIndex(nextSuggestionIndex)
                                return
                            }

                            default: {
                                setIsVisible(true)
                                return
                            }
                        }
                    }}
                    aria-expanded={isVisible}
                    aria-owns="results"
                    aria-label="Search for a team or player"
                    aria-describedby="typeahead-instructions"
                    aria-activedescendant={
                        selectedSuggestion ? `option-${selectedSuggestion.id}` : undefined
                    }
                />
            {(shouldShowSuggestions) && (
                <Suggestions id='results'>
                    {totalSuggestions.map((suggestion, index) => {
                        const isSelected = index === selectedSuggestionIndex;
                        const suggestion_data = (<Suggestion
                            key={ suggestion.id }
                            suggestion={ suggestion }
                            index={ index }
                            isSelected={ isSelected }
                            searchValue={ searchTerm }
                            onMouseEnter={() => {
                                setSelectedSuggestionIndex(index);
                            }}
                            onMouseDown={() => {
                                setIsVisible(false)
                                toggleIsDataTableVisible(true)
                                handleSelect(suggestion);
                            }}
                        />)
                        if (teamSuggestions.length > 0 && index === 0) {
                            return (
                                <>
                                <dt>Teams</dt>
                                {suggestion_data}
                                </>
                            )
                        } else if (playerSuggestions && index === teamSuggestions.length) {
                            return (
                                <>
                                <dt>Players</dt>
                                {suggestion_data}
                                </>
                            ) 
                        } else {
                            return (
                                suggestion_data
                            )
                        }
                    })}
                </Suggestions>
            )}
            <ForScreenReaders id="typeahead-instructions">
                When autocomplete results are available use up and down arrows to review
                and enter to select. Touch device users, explore by touch or with swipe
                gestures.
            </ForScreenReaders>
        </Wrapper>
    )
}

const Wrapper = styled.div`
    position: relative;
    display: flex;
    justify-content: center;
`;

const Input = styled.input`
    width: 25%;
    height: 40px;
    padding: 0 12px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 18px;
`;

const Suggestions = styled.div`
    position: absolute;
    width: 25%;
    bottom: -10px;
    padding: 10px;
    border-radius: 4px;
    box-shadow: 1px 5px 10px rgba(0, 0, 0, 0.2);
    transform: translateY(100%);
`;

const ForScreenReaders = styled.span`
    display: none;
`;

export default TypeAhead