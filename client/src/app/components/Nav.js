import './Nav.css';
// import { Link } from 'react-router-dom';
import Link from 'next/link';

const Nav = () => {
  return (
    <nav className="w-full bg-slate-800 flex flex-col justify-start items-start">
      <ul className="text-white list-none flex flex-nowrap items-center m-0">
        <li className="group p-4 hover:bg-gray-200 hover:text-gray-800 focus:bg-gray-200 focus:text-gray-800 cursor-pointer">
          <Link href="/" className="text-white no-underline group-hover:text-gray-800 group-focus:text-gray-800">
            Home
          </Link>
        </li>
        <li className="group p-4 hover:bg-gray-200 hover:text-gray-800 focus:bg-gray-200 focus:text-gray-800 cursor-pointer">
          <Link href="/" className="text-white no-underline group-hover:text-gray-800 group-focus:text-gray-800">
            About
          </Link>
        </li>
      </ul>
    </nav>
  );
};

export default Nav;
