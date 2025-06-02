const ViewPane = ({ currentListing }) => {
  return (
    <div className="w-auto p-2">
      {currentListing ? (
        <>
          <h3 className="m-2 font-semibold group-hover:text-blue-600 group-focus:text-blue-600">
            {currentListing.name}
          </h3>
          <p className='m-2'>{currentListing.category}</p>
          <p className='m-2'>{currentListing.email}</p>
          <p className='m-2'>{currentListing.website}</p>
          <p className='m-2'>{currentListing.phone_number1}</p>
        </>
      ) : (
        <p className="m-2 italic text-gray-500">Select a business for more information</p>
      )}
    </div>
  )
}

export default ViewPane