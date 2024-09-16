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

This project implements a K-Nearest Neighbors (KNN) algorithm for predicting and classifying student employability based on various features. The dataset used is "Students' Employability from the Philippines" obtained from Kaggle.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

[![Python][Python]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

The project consists of three main Python scripts:

1. `testing_attr.py`: Tests different feature combinations to find the most accurate set of features for prediction.
2. `KNN.py`: Implements the KNN algorithm for both classification and regression tasks.
3. `Visualizer.py`: Provides data visualization capabilities, including 2D and 3D plots of the classification results.

To get a local copy up and running follow these simple example steps.

### Prerequisites

Before you begin, ensure you have met the following requirements:
* Python 3.7 or higher
* pip (Python package installer)

### Dataset

The dataset used in this project is ["Student-Employability-Datasets.xlsx"](https://www.kaggle.com/datasets/anashamoutni/students-employability-dataset), which should be placed in a "Dataset" folder in the project root directory.

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
   matplotlib
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

1. Run `testing_attr.py` to determine the best features for prediction:
   ```
   python testing_attr.py
   ```
   This script will output the best combination of features and their corresponding accuracy.

2. Run `KNN.py` to perform KNN classification and regression:
   ```
   python KNN.py
   ```
   This script will output the classification report, confusion matrix, and regression results.

3. Run `Visualizer.py` for interactive data visualization:
   ```
   python Visualizer.py
   ```
   This script provides a menu-driven interface to view classification and regression results, as well as 2D and 3D visualizations of the data.

_For detailed explanation, please refer to the [Documentation](https://example.com)_

## Customization

You can customize the following parameters in the code:
- Number of neighbors for classification (`n_neighbors` in `KNeighborsClassifier`)
- Number of neighbors for regression (`n_neighbors` in `KNeighborsRegressor`)
- Features used for analysis (currently 'GENERAL APPEARANCE', 'MANNER OF SPEAKING', 'SELF-CONFIDENCE')
- Test set size (currently 20%)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Features

- Feature selection: The project tests various combinations of features to find the most accurate set for prediction.
- KNN Classification: Predicts whether a student is "Employable" or "Less Employable" based on selected features.
- KNN Regression: Predicts the "Student Performance Rating" based on the same features.
- Data Visualization: Provides 2D and 3D visualizations of the classification results, helping to understand the decision boundaries and data distribution.

## Project Structure

```
project_root/
│
├── Dataset/
│   └── Student-Employability-Datasets.xlsx
│
└── Dataset/
    ├── testing_attr.py
    ├── KNN.py
    └── Visualizer.py
```

<!-- ROADMAP -->
## Roadmap

- [x] Data Collection
- [x] KNN Algorithm Implementation
    - [x] KNN Testing
    - [x] Data Visualization
- [ ] Documentation
    - [ ] Introduction
    - [ ] Data with Citation
    - [x] Process
    - [x] Testing Procedure
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



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Students' Employability Dataset - Philippines](https://www.kaggle.com/datasets/anashamoutni/students-employability-dataset)
* [K-Nearest Neighbors (KNN) Classification with scikit-learn](https://www.datacamp.com/tutorial/k-nearest-neighbor-classification-scikit-learn)
* [Data Visualization using Matplotlib in Python](https://www.datacamp.com/tutorial/k-nearest-neighbor-classification-scikit-learn)

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