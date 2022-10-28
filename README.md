<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">HTTP Server Python</h3>

  <p align="center">
    A basic Python server so you don’t start from scratch
    <br />
    <br />
    <a href="https://github.com/andreaaazo/http-server-python">View Demo</a>
    ·
    <a href="https://github.com/andreaaazo/http-server-python/issues">Report Bug</a>
    ·
    <a href="https://github.com/andreaaazo/http-server-python/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#-about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#-getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#-usage">Usage</a></li>
    <li><a href="#-roadmap">Roadmap</a></li>
    <li><a href="#-contributing">Contributing</a></li>
    <li><a href="#-license">License</a></li>
    <li><a href="#-contact">Contact</a></li>
    <li><a href="#-acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## ❔ About The Project

The simplicity of this project makes it **perfect for beginners**, and for those who want to learn the basics of an HTTP server.

This is a **basic HTTP Server with a HTTP Request Handler**, and some **features**:
- Cookies
- Retrieve CGI Forms 
- User authentication
- Custom Database
- Build-in home, authentication, registration and 404 error HTML pages (with Bootstrap)

_Start with this server, and build yours more faster!_. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With
[![Bootstrap][Bootstrap.com]][Bootstrap-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## 📥 Getting Started

Start from here, and set up your local project correctly.


### Prerequisites

* pipenv
  ```zsh
  pip install --user pipenv
  ```
  
* git  

    _with Homebrew package_
    ```zsh
    brew install git
    ```
  
### Installation

_Install correctly the project._

1. Clone the repo
   ```sh
   git clone https://github.com/andreaaazo/http-server-python.git
   ```
3. Open a terminal in the main folder, and start the env
   ```zsh
   pipenv shell
   ```
   
4. Start the server
   ```zsh
   python main.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## 🔨 Usage

This is a **Python Request Handler and Server**.  

Initially, the website is presented with an introductory page, where you can choose to register or access a profile already registered.
Once you have successfully logged in, the server will redirect you to a user page, where will be shown 3 tests that you can take. Below you can find the grade assigned to the test and the number of questions answered correctly.


The server works through cookies, which allow you to keep the session active. So even if you open a new window on your browser and want to access your account, the server will log in automatically, without having to re-enter your credentials in a totally reactive way.


To facilitate the proper execution of the code I took the liberty of adding a virtual python environment.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## 📍 Roadmap

- [x] Finish Project
- [ ] Refine code 
- [ ] Modify cookies auth to avoid cookies injections

See the [open issues](https://github.com/andreaaazo/http-server-python/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## 🤝 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## 📝 License

Distributed under the MIT License. See [`LICENSE.txt`](https://github.com/andreaaazo/http-server-python/blob/main/LICENSE) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## 📞 Contact

Andrea Zorzi - [@andreaaa.zo](https://twitter.com/your_username) - zorzi.andrea@outlook.com

Project Link: [https://github.com/andreaaazo/http-server-python](https://github.com/andreaaazo/http-server-python)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## 📑 Acknowledgments

A list of some useful Python libraries:

* [HTTP](https://docs.python.org/3/library/http.server.html#)

I suggest you to try to replicate this project from scratch, and add your custom features.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/andreaaazo/http-server-python.svg?style=for-the-badge
[contributors-url]: https://github.com/andreaaazo/http-server-python/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/andreaaazo/http-server-python.svg?style=for-the-badge
[forks-url]: https://github.com/andreaaazo/http-server-python/network/members
[stars-shield]: https://img.shields.io/github/stars/andreaaazo/http-server-python.svg?style=for-the-badge
[stars-url]: https://github.com/andreaaazo/http-server-python/stargazers
[issues-shield]: https://img.shields.io/github/issues/andreaaazo/http-server-python.svg?style=for-the-badge
[issues-url]: https://github.com/andreaaazo/http-server-python/issues
[license-shield]: https://img.shields.io/github/license/andreaaazo/http-server-python.svg?style=for-the-badge
[license-url]: https://github.com/andreaaazo/http-server-python/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
