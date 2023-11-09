import '../assets/Header-test.css';



function Header() {
    return(
    

<header>

  <nav class="navbar navbar-expand-lg fixed-top navbar-scroll">
    <div class="container-fluid">
      <button
              class="navbar-toggler ps-0"
              type="button"
              data-mdb-toggle="collapse"
              data-mdb-target="#navbarExample01"
              aria-controls="navbarExample01"
              aria-expanded="false"
              aria-label="Toggle navigation"
              >
        <span
              class="d-flex justify-content-start align-items-center"
              >
          <i class="fas fa-bars"></i>
        </span>
      </button>
      <div class="collapse navbar-collapse" id="navbarExample01">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item active">
            <a class="nav-link" aria-current="page" href="#intro">Home</a>
          </li>
          <li class="nav-item">
            <a
               class="nav-link"
               href="https://www.youtube.com/channel/UC5CF7mLQZhvx8O5GODZAhdA"
               rel="nofollow"
               target="_blank"
               >Learn Bootstrap 5</a
              >
          </li>
          <li class="nav-item">
            <a
               class="nav-link"
               href="https://mdbootstrap.com/docs/standard/"
               target="_blank"
               >Download MDB UI KIT</a
              >
          </li>
        </ul>

        <ul class="navbar-nav flex-row">
          <li class="nav-item">
            <a
               class="nav-link pe-2"
               href="https://www.youtube.com/channel/UC5CF7mLQZhvx8O5GODZAhdA"
               rel="nofollow"
               target="_blank"
               >
              <i class="fab fa-youtube"></i>
            </a>
          </li>
          <li class="nav-item">
            <a
               class="nav-link px-2"
               href="https://www.facebook.com/mdbootstrap"
               rel="nofollow"
               target="_blank"
               >
              <i class="fab fa-facebook-f"></i>
            </a>
          </li>
          <li class="nav-item">
            <a
               class="nav-link px-2"
               href="https://twitter.com/MDBootstrap"
               rel="nofollow"
               target="_blank"
               >
              <i class="fab fa-twitter"></i>
            </a>
          </li>
          <li class="nav-item">
            <a
               class="nav-link ps-2"
               href="https://github.com/mdbootstrap/mdb-ui-kit"
               rel="nofollow"
               target="_blank"
               >
              <i class="fab fa-github"></i>
            </a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <div
       id="intro"
       class="bg-image"

       >
    <div class="mask text-white" >
      <div class="container d-flex align-items-center text-center h-100">
        <div>
          <h1 class="mb-5">This is title</h1>
          <p>
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Officiis molestiae
            laboriosam numquam expedita ullam saepe ipsam, deserunt provident corporis,
            sit non accusamus maxime, magni nulla quasi iste ipsa architecto? Autem!
          </p>
        </div>
      </div>
    </div>
  </div>

</header>



    )


}


export default Header;

