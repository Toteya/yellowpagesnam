import React from 'react'

const SearchBar = () => {
  return (
    <div className="flex items-center">
      <input
        type="text"
        placeholder="Search..."
        className="m-1 p-2 rounded-md border border-gray-400 bg-slate-600 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
    </div>
  );
};

export default SearchBar;
