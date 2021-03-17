import { useState } from 'react';

const Header = () => {
    return (
        <div className="text-center">
        <img
          src="../NBA-logo.png"
          width="300"
          className="img-thumbnail"
          alt='NBA Logo'
          style={{ marginTop: "20px" }}
        />
        <hr />
        <h1>NBA Stats</h1>
      </div>
    );
}

export default Header