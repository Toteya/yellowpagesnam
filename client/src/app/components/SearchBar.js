import React from 'react'

const SearchBar = ({ setSearchQuery }) => {
  const handleInputChange = (e) => {
    setSearchQuery(e.target.value);
  }

  return (
    <form className="flex items-center" onSubmit={(e) => e.preventDefault()}>
      <label htmlFor='search' className='sr-only'>Search</label>
      <input
        type="text"
        placeholder="Search..."
        className="m-1 p-2 rounded-md border border-gray-400 bg-slate-600 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
        onChange={handleInputChange}
      />
    </form>
  );
};

export default SearchBar;
