import React from 'react'
import { Input, Button } from "reactstrap"

const SearchBar = (props) => {

    // const search = () => {
    //     props.onSearch()
    // }

    // const handleChange = ({target}) => {
    //     props.updateSearchTerm(target.value)
    // }

    return (
        <div className="SearchBar">
            <Input placeholder="Enter a player or team name"/>
            <Button className="SearchButton">Search</Button>
        </div>
    );
}

export default SearchBar