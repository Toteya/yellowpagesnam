import Link from 'next/link';

const NavLink = ({ text, href }) => {
  return (
    <li className="group p-2 flex items-center hover:bg-gray-200 hover:text-gray-800 focus:bg-gray-200 focus:text-gray-800 cursor-pointer">
      <Link href={href} className="text-white no-underline group-hover:text-gray-800 group-focus:text-gray-800">
        {text}
      </Link>
    </li>
  );
};

export default NavLink;
