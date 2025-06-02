import { FaPhone } from 'react-icons/fa6';
import { MdMail } from 'react-icons/md';
import { FaGlobeAfrica as FaGlobe } from 'react-icons/fa';

const ViewPane = ({ currentListing }) => {
  return (
    <div className="w-auto p-2">
      {currentListing ? (
        <>
          <h3 className="m-2 font-semibold group-hover:text-blue-600 group-focus:text-blue-600">
            {currentListing.name}
          </h3>
          <p className='m-2'>{currentListing.category}</p>
          <p className='m-2 flex items-center gap-2'>
            <MdMail />
            {currentListing.email}
          </p>
          <p className='m-2 flex items-center gap-2'>
            <FaGlobe />
            {currentListing.website}
          </p>
          <p className='m-2 flex items-center gap-2'>
            <FaPhone />
            {currentListing.phone_number1}
          </p>
        </>
      ) : (
        <p className="m-2 italic text-gray-500">Select a business for more information</p>
      )}
    </div>
  )
}

export default ViewPane