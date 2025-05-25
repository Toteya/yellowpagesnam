const ListItem = ({listing}) => {
  return (
    <li className='ListItem'>
      <h3>{listing.name}</h3>
      <p>{listing.category}</p>
      <p>{listing.email}</p>
      <p>{listing.website}</p>
      <p>{listing.phone_number1}</p>
    </li>
  )
}

export default ListItem
