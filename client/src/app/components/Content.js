import './Content.module.css';
import ListItem from './ListItem';
import ListPane from './ListPane';
import ViewPane from './ViewPane';

const Content = ({ listings }) => {
  return (
    <div className="flex h-screen">
      <ListPane listings={listings} />
      <ViewPane />
    </div>
  )
}

export default Content