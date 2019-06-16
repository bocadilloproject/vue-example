# Roadmap

## [x] Project definition

Build an URL shortener based on the following user stories:

- (A: Anonymous URL shortening) As an anonymous user, I want to get a shorter URL for an URL of my choice so that I can share it with other people.
- (B: Authenticated URL list) As a logged in user, I want to see all the URLs I have previously shortened so that I can share them again.
- (C: Authenticated URL removal) As a logged in user, I want to delete an existing shortened URL so that people cannot access it anymore.

Relevant resources:

- [Polr](https://polrproject.org/): open source link shortener.
- [Polr demo instance](https://demo.polr.me/)

## [x] Frontend and backend app setup.

Relevant resources:

- [Bocadillo CLI](https://github.com/bocadilloproject/bocadillo-cli)
- [Vue CLI: Creating a project](https://cli.vuejs.org/guide/creating-a-project.html#vue-create)

## [ ] A: Anonymous URL shortening

- [x] Create basic URL form
- [x] Tie "Submit" button to a `fetch()` call.
- [x] Implement basic form of the endpoint in backend.
- [x] Add [CORS](https://bocadilloproject.github.io/guide/builtin-middleware.html#cors).
- [x] Creation of link hashes: [hashids](https://github.com/davidaurelio/hashids-python).
- [x] Storage of links: [Bocadillo + orm](https://bocadilloproject.github.io/how-to/orm.html).
- [ ] Display link hash in frontend

## [ ] B: Authenticated URL view

TODO

## [ ] C: Authenticated URL removal

TODO

## Ideas for future development

- Allow users to provide a custom URL hash (e.g. `my-url`) and check for its availability.
