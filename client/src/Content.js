import './Content.css';
import ListItem from './ListItem';

const Content = ({ listings }) => {
  return (
    <div className="Content">
      <h2>Welcome to the Business Directory Namibia</h2>
      <ul>
        {listings.map((listing) => (
          <ListItem
            key={listing.id}
            listing={listing}
          />
        ))}
      </ul>
    </div>
  )
}

export default Content