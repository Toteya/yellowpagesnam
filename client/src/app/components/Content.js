import './Content.module.css';
import ListItem from './ListItem';
import ListPane from './ListPane';
import ViewPane from './ViewPane';

const Content = ({ listings, viewContent, setViewContent }) => {
  return (
    <div className="flex h-screen">
      <ListPane
        listings={listings}
        setViewContent={setViewContent}
      />
      <ViewPane viewContent={viewContent}/>
    </div>
  )
}

export default Content