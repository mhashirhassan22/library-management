# Django Library Management

A comprehensive Django RESTful API for managing books and authors, featuring user authentication, search functionality, and a recommendation system.

## Running the App Locally

**Note:** If you're building the Docker image for the first time, ensure you copy the appropriate `requirements-{ENV}.txt` file from `packaging/requirements/` to the project's root.

### 1. Copy Requirements File

```sh
cp packaging/requirements/requirements.{ENV}.txt requirements.txt
```

### 2. Copy Environment File

```shell
cp packaging/environment/env.{ENV}.example .env
```

If needed, fill in the values in the `.env` file.

### 3. Run the Project

```shell
make run
```

### 4. Apply Database Migrations

Open a separate terminal tab and run:

```sh
make apply-migrations
```

### 5. Run Tests

In another terminal tab, execute:

```sh
make tests
```

### 6. View the Application

Once the application is running, you can view it at [http://localhost:8000](http://localhost:8000).

## Project Details

This project provides a robust platform for managing a library's collection of books and authors. It includes the following key features:

### Features

- **User Authentication:** Secure JWT-based authentication.
- **Book Management:** CRUD operations for books.
- **Author Management:** Manage authors with full CRUD functionality.
- **Search Functionality:** Case-insensitive search by book title or author name.
- **Recommendation System:** Suggest books based on user preferences and favorites.
- **RESTful API:** Structured endpoints for easy integration.

### API Endpoints

#### Authentication

- `POST /api/token/`: Obtain JWT token.
- `POST /api/token/refresh/`: Refresh JWT token.

#### Books

- `GET /api/books/`: Retrieve a list of all books.
- `GET /api/books/:id/`: Retrieve a specific book by ID.
- `POST /api/books/`: Create a new book (protected).
- `PUT /api/books/:id/`: Update an existing book (protected).
- `DELETE /api/books/:id/`: Delete a book (protected).

#### Authors

- `GET /api/authors/`: Retrieve a list of all authors.
- `GET /api/authors/:id/`: Retrieve a specific author by ID.
- `POST /api/authors/`: Create a new author (protected).
- `PUT /api/authors/:id/`: Update an existing author (protected).
- `DELETE /api/authors/:id/`: Delete an author (protected).

#### Search

- `GET /api/books?search=query`: Search books by title or author name.

#### Recommendations

- `GET /api/recommendations/`: Get book recommendations based on user favorites.


## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new feature branch: `git checkout -b feature/YourFeature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/YourFeature`.
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

**Your Name**  
[My Email](mhashirhassan22@gmail.com)  
[Portfolio](https://www.devswall.com/portfolio/hashir/)  
[My GitHub](https://github.com/mhashirhassan22/)
