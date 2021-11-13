let library = [];
// Default book data
const defaultBook1 = new Book("Red Rising", "Pierce Brown", 416, "read");
const defaultBook2 = new Book("Golden Sun", "Pierce Brown", 464, "not read");
const defaultBook3 = new Book("Morning Star", "Pierce Brown", 544, "not read");
const defaultBooks = [defaultBook1, defaultBook2, defaultBook3];
insertRow(defaultBook1);

// Event listener for Add Book button
const addBookButton = document.getElementById("add-book-button");
addBookButton.addEventListener("click", function() {
    addBookToLibrary();
});

function Book(title, author, pages, read) {
    this.title = title;
    this.author = author;
    this.pages = pages;
    this.read = read;
}

// Takes data from form, creates book and adds book to library array
function addBookToLibrary() {
    console.log("added");
    let form = new FormData();
    form.append("title", document.getElementById("title").value);
    form.append("author", document.getElementById("author").value);
    form.append("pages", document.getElementById("pages").value);
    form.append("read", document.getElementById("read").value);
    const newBook = new Book(form.get("title"), form.get("author"), 
            form.get("pages"), form.get("read"))
    insertRow(newBook);
}

// Inserts a books data into table
// Depends upon: 
//     toggleRead(book, cell4)
//     removeBook(book, row)
function insertRow(book) {
    library.push(book);
    let index = library.indexOf(book);
    console.log(library);
    
    // Create row and row cells
    let table = document.getElementById("library-table");
    let row = table.insertRow();
    row.id = "row" + index;
    let cell0 = row.insertCell(0);
    let cell1 = row.insertCell(1);
    let cell2 = row.insertCell(2);
    let cell3 = row.insertCell(3);
    let cell4 = row.insertCell(4);
    let cell5 = row.insertCell(5);

    // Set cell values
    // Attach event listeners to buttons in cells
    cell0.innerHTML = book.title;
    cell1.innerHTML = book.author;
    cell2.innerHTML = book.pages;
    cell3.innerHTML = (book.read === "read") ? "read" : "not read";
    let removalButtonId = "remove-book-button" + index;
    cell4.innerHTML = "<button id=" + removalButtonId + 
            " data=" + index + ">Remove</button>";
    const removeBookButton = document.getElementById(removalButtonId);
    removeBookButton.addEventListener("click", function() {
        removeBook(index, row);
    });
    let toggleButtonId = "toggle-read-button" + index;
    cell5.innerHTML = "<button id=" + toggleButtonId + 
            " data=" + index + ">Toggle Read</button>";
    const toggleButton = document.getElementById(toggleButtonId);
    toggleButton.addEventListener("click", function() {
        toggleRead(book, cell3);
    });    
}

// Remove book from library and from user view
function removeBook(index, row) {
    row.remove();
    library.splice(index, 1);
}

// Toggle book read status in object and in user view
function toggleRead(book, cell4) {
    if(book.read === "read") {
        book.read = "not read";
        cell4.innerHTML = "not read";
    }
    else if (book.read === "not read"){
        book.read = "read";
        cell4.innerHTML = "read";
    }
}