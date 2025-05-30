const ListItem = ({ listing, handleClick }) => {
  return (
    <li
      className="group p-4 bg-white border rounded-md shadow-sm cursor-pointer focus:bg-gray-200 hover:bg-gray-100 transition-colors"
      onClick={() => handleClick(listing)}
    >
      <h3 className="font-semibold group-hover:text-blue-600 group-focus:text-blue-600">
        {listing.name}
      </h3>
      <p>{listing.category}</p>
      <p className="text-sm">{listing.email}</p>
      <p className="text-sm">{listing.website}</p>
      <p className="text-sm">{listing.phone_number1}</p>
    </li>
  );
};

export default ListItem
