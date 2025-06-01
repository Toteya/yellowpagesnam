const ViewPane = ({ viewContent }) => {
  return (
    <div className="w-auto p-2">
      <h2 className='m-2'>ViewPane</h2>
      <p className='m-2 italic'>{viewContent}</p>
    </div>
  )
}

export default ViewPane