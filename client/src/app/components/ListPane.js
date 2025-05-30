import ListItem from "./ListItem"

const ListPane = ({ listings }) => {
  return (
    <div className="w-1/2 p-4 bg-gray-100 border-r">
      <></>
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


export default ListPane