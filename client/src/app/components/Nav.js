import Link from 'next/link';

const Nav = () => {
  return (
    <nav className="w-full bg-slate-800 text-white flex items-center justify-between sticky top-0 z-50">
      <ul className="flex space-x-2 pl-2">
        <li className="group p-2 hover:bg-gray-200 hover:text-gray-800 focus:bg-gray-200 focus:text-gray-800 cursor-pointer">
          <Link href="/" className="text-white no-underline group-hover:text-gray-800 group-focus:text-gray-800">
            Home
          </Link>
        </li>
        <li className="group p-2 hover:bg-gray-200 hover:text-gray-800 focus:bg-gray-200 focus:text-gray-800 cursor-pointer">
          <Link href="/about" className="text-white no-underline group-hover:text-gray-800 group-focus:text-gray-800">
            About
          </Link>
        </li>
      </ul>
    </nav>
  );
};

export default Nav;
