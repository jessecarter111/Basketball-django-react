import React from 'react';
import styled from 'styled-components';

const Suggestion = ({
    searchValue,
    suggestion,
    type, 
    index,
    isSelected,
    ...delegated
}) => {
    let matchIndex;
    let firstHalf;
    let secondHalf;
    //Differentiate between player and team objects
    if (type === 'player') {
        matchIndex = suggestion
        .player_name.toLowerCase()
        .indexOf(searchValue.toLowerCase())
        //Determine the index from which the match begins
        const matchEnd = matchIndex + searchValue.length
        firstHalf = suggestion.player_name.slice(0, matchEnd);
        secondHalf = suggestion.player_name.slice(matchEnd);
    } else {
        matchIndex = suggestion
        .team_name.toLowerCase()
        .indexOf(searchValue.toLowerCase())
        const matchEnd = matchIndex + searchValue.length
        firstHalf = suggestion.team_name.slice(0, matchEnd);
        secondHalf = suggestion.team_name.slice(matchEnd);
    }
        
    return (
        <Wrapper
            className={isSelected ? 'selected' : undefined}
            id={`option-${suggestion.id}`}
            // These settings are important for accessibility
            role="option"
            aria-selected={isSelected}
            tabindex={-1}
            {...delegated}
        >
            {firstHalf}
            <Prediction>{secondHalf}</Prediction>{' '}
        </Wrapper>
    )
}

const Wrapper = styled.dd`
    display: block;
    width: 100%;
    padding: 10px;
    font-size: 18px;
    border-bottom: 1px solid rgba(0, 0, 0, 0.1);
    text-decoration: none;
    color: black;
    line-height: 1.25;
    border: none;
    background: transparent;
    text-align: left;
    cursor: pointer;
    &:last-of-type {
        border-bottom: none;
        margin-bottom: 0;
    }
    &.selected {
        background: hsla(50deg, 100%, 80%, 0.6);
    }
`;

const Prediction = styled.span`
    font-weight: bold;
`;

const CategoryName = styled.span`
    color: purple;
`;

const Caption = styled.em`
    opacity: 0.75;
    font-size: 0.8em;
`;

export default Suggestion;
