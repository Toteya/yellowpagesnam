import './Content.module.css';
import ListItem from './ListItem';
import ListPane from './ListPane';
import ViewPane from './ViewPane';

const Content = ({ listings, currentListing, setCurrentListing }) => {
  return (
    <div className="flex h-screen mt-1">
      <ListPane
        listings={listings}
        setCurrentListing={setCurrentListing}
      />
      <ViewPane currentListing={currentListing}/>
    </div>
  )
}

export default Content