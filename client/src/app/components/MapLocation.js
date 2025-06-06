const MapLocation = ({ latitude, longitude }) => {
  const mapSrc = `https://www.google.com/maps/embed?pb=!1m17!1m12!1m3!1d3798.8258493181497!2d${longitude}!3d${latitude}!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m2!1m1!2zMTfCsDQ3JzU5LjYiUyAxNcKwNDYnNTYuOSJF!5e0!3m2!1sen!2sna!4v1749146089945!5m2!1sen!2sna`;
  // Use this dynamic approach
  // const mapSrc = `https://www.google.com/maps/embed/v1/view?key=YOUR_API_KEY&center=${latitude},${longitude}&zoom=14`;
  return (
    <iframe
      className="m-2"
      src={mapSrc}
      width="400"
      height="300"
      style={{border: 0}}
      allowFullScreen=""
      loading="lazy"
      referrerPolicy="no-referrer-when-downgrade"
      title="Google Maps Location"
    >
    </iframe>
  )
}

export default MapLocation