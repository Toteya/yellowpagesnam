import ListItem from "./ListItem"

const ListPane = ({ listings, setViewContent }) => {
  const handleClick = (listing) => {
    setViewContent(listing.name);
  }
  return (
    <div className="w-1/2 p-4 bg-gray-100 border-r overflow-y-scroll">
      <ul>
        {listings.map((listing) => (
          <ListItem
            key={listing.id}
            listing={listing}
            handleClick={handleClick}
          />
        ))}
      </ul>
    </div>
  )
}


export default ListPane