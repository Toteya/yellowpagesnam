import NavLink from './NavLink';
import SearchBar from './SearchBar';

const Nav = ({ setSearchQuery }) => {
  return (
    <nav className="w-full bg-slate-800 text-white flex items-center justify-between sticky top-0 z-50">
      <ul className="flex space-x-2 pl-2">
        <NavLink
          text="Home"
          href="/"
        />
        <NavLink
          text="About"
          href="/about"
        />
        <SearchBar setSearchQuery={setSearchQuery}/>
      </ul>
    </nav>
  );
};

export default Nav;
