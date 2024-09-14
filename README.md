<a id="readme-top"></a>



<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/AJSahagun/CS414-KNN-Activity1">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Students' Employability KNN Classification and Prediction</h3>

  <p align="center">
    Classification and prediction of students' employability from the Philippines using K-Nearest Neighbors algorithm.
    <br />
    <a href="https://github.com/AJSahagun/CS414-KNN-Activity1"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/AJSahagun/CS414-KNN-Activity1">View Demo</a>
    ·
    <a href="https://github.com/AJSahagun/CS414-KNN-Activity1/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/AJSahagun/CS414-KNN-Activity1/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Product Name Screen Shot][product-screenshot]

Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `github_username`, `repo_name`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description`

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

[![Python][Python]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

Before you begin, ensure you have met the following requirements:
* Python 3.7 or higher
* pip (Python package installer)

### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/AJSahagun/CS414-KNN-Activity1.git
   ```

2. Navigate to the project directory
   ```sh
   cd CS414-KNN-Activity1
   ```

3. Install the required packages
   ```sh
   pip install -r requirements.txt
   ```

   Note: If `requirements.txt` doesn't exist, you can create one with the following content:
   ```
   pandas
   scikit-learn
   openpyxl
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

To run the KNN analysis:

1. Open a terminal or command prompt
2. Navigate to the project directory
3. Run the Python script:
   ```sh
   python KNN.py
   ```

The script will output:
- Confusion Matrix
- Classification Report
- Classification Accuracy
- Regression Mean Squared Error
- Sample of Actual vs. Predicted values for regression

_For detailed explanation, please refer to the [Documentation](https://example.com)_

## Customization

You can customize the following parameters in the code:
- Number of neighbors for classification (`n_neighbors` in `KNeighborsClassifier`)
- Number of neighbors for regression (`n_neighbors` in `KNeighborsRegressor`)
- Features used for analysis (currently 'GENERAL APPEARANCE', 'MANNER OF SPEAKING', 'SELF-CONFIDENCE')
- Test set size (currently 20%)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Data Collection
- [x] KNN Algorithm Implementation
    - [x] KNN Testing
    - [ ] Data Visualization
- [ ] Documentation
    - [ ] Introduction
    - [ ] Data with Citation
    - [ ] Process
    - [ ] Testing Procedure
    - [ ] Results
    - [ ] Conclusion

See the [open issues](https://github.com/AJSahagun/CS414-KNN-Activity1/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/github_username/repo_name/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=AJSahagun/CS414-KNN-Activity1" alt="contrib.rocks image" />
</a>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

AJ Sahagun - aajsahagun@gmail.com

Project Link: [https://github.com/AJSahagun/CS414-KNN-Activity1](https://github.com/AJSahagun/CS414-KNN-Activity1)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/AJSahagun/CS414-KNN-Activity1.svg?style=for-the-badge
[contributors-url]: https://github.com/AJSahagun/CS414-KNN-Activity1/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/AJSahagun/CS414-KNN-Activity1.svg?style=for-the-badge
[forks-url]: https://github.com/AJSahagun/CS414-KNN-Activity1/network/members
[stars-shield]: https://img.shields.io/github/stars/AJSahagun/CS414-KNN-Activity1.svg?style=for-the-badge
[stars-url]: https://github.com/AJSahagun/CS414-KNN-Activity1/stargazers
[issues-shield]: https://img.shields.io/github/issues/AJSahagun/CS414-KNN-Activity1.svg?style=for-the-badge
[issues-url]: https://github.com/AJSahagun/CS414-KNN-Activity1/issues
[license-shield]: https://img.shields.io/github/license/AJSahagun/CS414-KNN-Activity1.svg?style=for-the-badge
[license-url]: https://github.com/AJSahagun/CS414-KNN-Activity1/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.png

[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/