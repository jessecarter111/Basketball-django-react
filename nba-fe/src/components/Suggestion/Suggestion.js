import React from 'react';
import styled from 'styled-components';

const Suggestion = ({
    searchValue,
    suggestion, 
    index,
    isSelected,
    ...delegated
}) => {
    console.log(suggestion.model_type)
    let key;
    suggestion.model_type === 'player'
    ? key = suggestion.player_name
    : key = suggestion.team_name

    const matchIndex = key.toLowerCase().indexOf(searchValue.toLowerCase())
    const matchEnd = matchIndex + searchValue.length
    const firstHalf = key.slice(0, matchEnd);
    const secondHalf = key.slice(matchEnd); 
        
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
