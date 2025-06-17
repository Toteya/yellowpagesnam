import { useState } from 'react';

const MediaCarousel = () => {
  const media = [
    { type: 'image', src: '/media/photos/pic1.jpg' },
    { type: 'image', src: '/media/photos/pic2.jpg' },
    { type: 'video', src: '/media/videos/video1.mp4' },
    { type: 'image', src: '/media/photos/pic3.jpg' },
    { type: 'video', src: '/media/videos/video2.mp4' },
  ];

  const [currentIndex, setCurrentIndex] = useState(0);

  const handlePrev = () => {
    setCurrentIndex((prevIndex) =>
      prevIndex === 0 ? media.length - 1 : prevIndex - 1
    );
  };

  const handleNext = () => {
    setCurrentIndex((prevIndex) =>
      prevIndex === media.length - 1 ? 0 : prevIndex + 1
    );
  };

  return (
    <div className="relative w-full max-w-3xl mx-auto p-4">
      <h2 className="text-lg font-bold mb-4">Photos and Videos</h2>
      <div className="overflow-hidden rounded-lg shadow-lg">
        {media[currentIndex].type === 'image' ? (
          <img
            src={media[currentIndex].src}
            alt={`Slide ${currentIndex + 1}`}
            className="w-full h-64 object-cover"
          />
        ) : (
          <video
            src={media[currentIndex].src}
            controls
            className="w-full h-64 object-cover"
          ></video>
        )}
      </div>

      {/* Navigation Buttons */}
      <button
        onClick={handlePrev}
        className="absolute top-1/2 left-4 transform -translate-y-1/2 bg-gray-800 text-white p-2 rounded-full hover:bg-gray-700 focus:outline-none"
      >
        ❮
      </button>
      <button
        onClick={handleNext}
        className="absolute top-1/2 right-4 transform -translate-y-1/2 bg-gray-800 text-white p-2 rounded-full hover:bg-gray-700 focus:outline-none"
      >
        ❯
      </button>
      {/* Dots Indicator */}
      <div className="flex justify-center space-x-2 mt-4">
        {media.map((_, index) => (
          <button
            key={index}
            onClick={() => setCurrentIndex(index)}
            className={`w-3 h-3 rounded-full ${
              currentIndex === index ? 'bg-gray-800' : 'bg-gray-400'
            }`}
          ></button>
        ))}
      </div>
    </div>
  );
};

export default MediaCarousel