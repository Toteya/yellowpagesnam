import { FaPhone } from 'react-icons/fa6';
import { MdMail } from 'react-icons/md';
import { FaGlobeAfrica as FaGlobe } from 'react-icons/fa';
import MapLocation from './MapLocation';
import PhoneNumbers from './PhoneNumbers';

const ViewPane = ({ currentListing: listing }) => {
  return (
    <div className="w-auto p-2">
      {listing ? (
        <div className="w-full h-96">
          <h3 className="m-2 font-semibold group-hover:text-blue-600 group-focus:text-blue-600">
            {listing.name}
          </h3>
          <p className='m-2'>{listing.category}</p>
          <p className='m-2 flex items-center gap-2'>
            <MdMail />
            {listing.email}
          </p>
          {listing.website && (
            <p className="m-2 flex items-center gap-2">
              <FaGlobe />
              <a
                href={listing.website}
                target="_blank"
                rel="noopener noreferrer"
                className="text-blue-500 underline hover:text-blue-700"
              >
                {listing.website}
              </a>
            </p>
          )}
          <PhoneNumbers phoneNumbers={listing.phone_numbers} />
          {listing.location && (
            <MapLocation
              lat={listing.latitude}
              lng={listing.longitude}
            />
          )}
        </div>
      ) : (
        <p className="m-2 italic text-gray-500">Select a business for more information</p>
      )}
    </div>
  )
}

export default ViewPane