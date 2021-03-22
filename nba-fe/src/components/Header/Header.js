import NBAlogo from '../Header/nbalogo.webp'

const Header = () => {
    return (
        <div className="text-center">
        <img
          src={NBAlogo}
          width="300"
          alt='NBA Logo'
          style={{ marginTop: "20px", marginBottom: "15px"}}
        />
        <h1>NBA Stats</h1>
      </div>
    );
}

export default Header