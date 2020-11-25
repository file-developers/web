# Contribute to the File-Developers Website

So you want to contribute to the File-Developers Website? Perfect, for everything to go well you have to follow some **standards**.

---

## Standars

### Before starting

Before contributing, **identify what type of contribution you want to make to the project**. The we will accept the following types of contributions:

* **New characteristics**: Contributions that add things to the web.
* **Internal contributions**: Contributions to the internal structure of the project.
* **Troubleshooting**: Have you found any type of error in the website, maybe a link is not working or something like that.
* **Updating content**: You can contribute to VMG to update something about the project itself.
* **Typos**: Contributions to solve typos in the project.
* **Others**: You can contribute in any other thing, any administrator of the File developers organization will read and consider your pull request.

---

### Steps to contribute

To contribute, follow this steps:

* Fork the repository in your profile.
* Clone the repository to your local machine.

```sh
git clone https://github.com/<your name>/web
```

* Move inside the repository.

```sh
cd web
```

* Activate the enviroment.
* Install the requirements

```sh
pip install -r requirements.txt
```

* Make your contribution.
* Commit your changes.
* Push the changes **to the dev branch**

**Remember that the repository is configured to automatically deploy the server from the** `main` **branch, so check that the code you write does not break anything once an administrator pulls the dev branch.**
Remember to follow the pull request template when creating the pull request itself.

#### NOTE: It will be a good idea to follow the [conventional commits](https://conventionalcommits.org) standard in your pull request

#### Thanks for wanting to contribute to the repository
