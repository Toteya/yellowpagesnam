import { FaPhone } from 'react-icons/fa6';
import { MdMail } from 'react-icons/md';
import { FaGlobeAfrica as FaGlobe } from 'react-icons/fa';

const ViewPane = ({ currentListing }) => {
  return (
    <div className="w-auto p-2">
      {currentListing ? (
        <div className="w-full h-96">
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
          <iframe
            src="https://www.google.com/maps/embed?pb=!1m17!1m12!1m3!1d3798.8258493181497!2d15.779907074758682!3d-17.799879983159368!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m2!1m1!2zMTfCsDQ3JzU5LjYiUyAxNcKwNDYnNTYuOSJF!5e0!3m2!1sen!2sna!4v1749146089945!5m2!1sen!2sna"
            width="400"
            height="300"
            style={{border: 0}}
            allowFullScreen=""
            loading="lazy"
            referrerPolicy="no-referrer-when-downgrade"
          >
          </iframe>
        </div>
      ) : (
        <p className="m-2 italic text-gray-500">Select a business for more information</p>
      )}
    </div>
  )
}

export default ViewPane