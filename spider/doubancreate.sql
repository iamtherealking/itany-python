
use python;
CREATE TABLE t_book_tag(

  id VARCHAR(200) PRIMARY KEY,
  tagName varchar(200),
  parentId VARCHAR(200)

)ENGINE  = Innodb DEFAULT CHARSET utf8;


CREATE TABLE t_book(
  id VARCHAR(100) PRIMARY KEY ,
  name VARCHAR(100),
  book_url VARCHAR(100),
  author VARCHAR(100),
  publisher VARCHAR(100),
  publishDate VARCHAR(100),
  price VARCHAR(100),
  rate VARCHAR(100)
)ENGINE  = Innodb DEFAULT CHARSET utf8;


