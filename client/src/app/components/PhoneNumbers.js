import { useState } from 'react';
import { FaPhone } from 'react-icons/fa6';

const PhoneNumbers = ({ phoneNumbers }) => {
  const [showAll, setShowAll] = useState(false);

  const displayedNumbers = showAll ? phoneNumbers : phoneNumbers.slice(0, 2);

  return (
    <p className='m-2 flex flex-wrap items-center gap-2'>
      <FaPhone />
      {!phoneNumbers?.length && 'No phone number available'}
      {phoneNumbers?.length > 0 && (
        <span className='flex flex-wrap gap-1'>
          {displayedNumbers.map((phone, index) => (
            <span 
              key={index}
              className='break-words'
            >
                {phone}
                {index < displayedNumbers.length - 1 ? ', ' : ''}
            </span>
          ))}
          {phoneNumbers.length > 2 && !showAll && (
            <button
              onClick={() => setShowAll(true)}
              className="ml-2 text-blue-500 underline hover:text-blue-700 focus:outline-none"
            >
              Show more
            </button>
          )}
          {showAll && (
            <button
              onClick={() => setShowAll(false)}
              className="ml-2 text-blue-500 underline hover:text-blue-700 focus:outline-none"
            >
              Show less
            </button>
          )}
        </span>
      )}
    </p>
  );
};

export default PhoneNumbers;
