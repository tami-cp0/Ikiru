
# Ikiru
A portfolio project to develop a non-toxic social media for the goal of complete mental health up-keep.
> **Note:** core Information and code snippets are not included in this README because the website is not yet completely public.

## Index
- [Ikiru](#ikiru)
  - [Index](#index)
  - [Accessing the Web App](#accessing-the-web-app)
  - [Features](#features)
  - [Technology and Architecture](#technology-and-architecture)
  - [Bugs](#bugs)
  - [Contibute](#contibute)
  - [Authors](#authors)
  - [Future Plans](#future-plans)
  - [License](#license)

## Accessing the Web App
> **Note:** The Website is currently only ready for desktop/PC devices.
> 
Visit [Ikiru](http://web-01.tamilore.tech) in any browser to access the site.

## Features
> Visit the [about](http://web-01.tamilore.tech/about) page of Ikiru to get a visually better feature explanation
- User Authentication
- Infinite Scrolling
- To post
- To see the posts of others in thier profile
- To see your posts in profile
> Those are the only features for MVP 1.0, wait for updates to get more features.

## Technology and Architecture
**Architecture**:
The Web Application employs a Three-Tier Architecture, mixed with a little bit of ***Service Oriented Architecture*** **(SOA)**. It's structured as:

> Presentation Layer: The user interface that users see and interact with.
> Application Layer: This layer contains our business logic and interacts with both the Presentation and Data layers.
> Data Layer: This layer houses our Database.

The touch of SOA is introduced through the development of a separate API for our frontend. This design choice enhances our application's flexibility, maintainability, and scalability.

Our custom built **Ikiru API** employs a variation of the Model-View-Controller Architecture. Here, the Model corresponds to the data in the database, the View is represented by the Swagger UI documentation we developed, and the Controller, which contains our application logic, is represented in the routes.

**Technologies**:
- Flask
- Python
- SQLAlchemy ORM
- MySQL
- HTML 5
- CSS
- JAVASCRIPT
- JQuery
- Flask-login
- IntersectionObserverAPI
- Bcrypt
- Flask-CORS
- Swagger UI
- Flassger
- UUID
- Datetime
- IkiruAPI
- zenquotesAPI
- Wtfforms
- Flask_wtf
- Gunicorn
- NginX

## Bugs
No known bugs at this time.

## Contibute
We welcome contributions from the community to help improve the project. If you encounter any bugs or have ideas for new features, please submit a bug report or feature request through the GitHub issues page or reach out to any of the emails in the [Authors](#authors) section. Additionally, we encourage pull requests for fixes or enhancements.

## Authors
- Oluwatamilore Olugbesan <findtamilore@gmail.com>
- Huclark Vanderpuye <vhuclark@gmail.com>
- Moses Solomon Ayofemi <solomonsyofemi@gmail.com>

## Future Plans
We have exciting plans for future enhancements and features in the pipeline. Some of the planned improvements include chatting, anonymous posting and  image posting. Stay tuned for updates as we continue to evolve and enhance the app to better serve our users.

## License
This project is licensed under the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).

For details, please see the [LICENSE](LICENSE) file.
