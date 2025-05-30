import './Content.css';
import ListItem from './ListItem';
import ListPane from './ListPane';
import ViewPane from './ViewPane';

const Content = ({ listings }) => {
  return (
    <div className="flex h-screen">
      {/* <h2>Welcome to the Business Directory Namibia</h2> */}
      <ListPane listings={listings} />
      <ViewPane />
    </div>
  )
}

export default Content