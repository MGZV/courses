"""
CREATE book
(book_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
title VARCHAR(30),
amount INT);


CREATE author
(author_id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(30));


CREATE book_author,
author_id IN PRIMARY KEY,
book_id IN PRIMARY KEY,

FOREING KEY (author_id) REFERENCES author (au,tor_id)
FOREING KEY (book_id) REFERENCES author (book_id);

"""