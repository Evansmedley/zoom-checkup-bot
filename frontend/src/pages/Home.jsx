const Home = () => {
  return (
    <div className="page-content">
      <div className="text">
        <div id="mainText">Your Remote Doctor is here to assist</div>
        <div id="subText">
          Get your hands-on doctors appointment from the convenience of your
          home.
        </div>
      </div>
      <img src={"/assets/images/arm.png"} className="robot-pic" alt="arm" />

      <div className="bg-sphere">
        <div className="bg-square"></div>
      </div>
    </div>
  );
};

export default Home;
